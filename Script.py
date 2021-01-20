# ==================================================
#                    Groupe 15
#                 Bristol city Bike
#             Date de Rendu : 22.01.2021
#
# ===================================================


# In[2]:


from pyspark.sql import SparkSession
import configparser
from pyspark.sql.functions import col
import folium
import pandas as pd

# 1- Instancier Client Spark
spark = SparkSession.builder \
    .master("local") \
    .appName("Bristol") \
    .getOrCreate()

# 2) Creation du fichier confif + dossier(input+exported)
# configurer les paths pour facilité l'accès aux différent dossiers
config = configparser.ConfigParser()
config.read('properties.conf')
path_to_input_data = config['Bristol-City-bike']['Input-data']
path_to_output_data = config['Bristol-City-bike']['Output-data']
# obliger de transformer la varible num_partition en int, considérer comme str au début
num_partition_kmeans = config.getint('Bristol-City-bike', 'Kmeans-level')

# 3importer les données bristol sPark
bristol = spark.read.json(path_to_input_data)
# afficher les 3 premières valeurs de Bristol
bristol.show(3)

# 4selectionner les variables pertinante pour notre Kmeans
Kmean_df = bristol.select(col("latitude"), col("longitude"))
Kmean_df.show(3)

# 5 Kmeans sur notre base de données
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans

features = ("longitude", "latitude")
kmeans = KMeans().setK(num_partition_kmeans).setSeed(1)
assembler = VectorAssembler(inputCols=features, outputCol="features")
dataset = assembler.transform(Kmean_df)
model = kmeans.fit(dataset)
fitted = model.transform(dataset)

# 6)
fitted.columns
# fitted correponds a la sortie avec nos données + les prédiction( groupe d'appartenance)+features

# 7)
fitted.groupBy("prediction") \
    .mean() \
    .show()

# affichier les moyenne par groupe
# methode sql
fitted.createOrReplaceTempView("Fit")

spark.sql(
    """select Avg(longitude) as Moy_Long,  Avg(latitude) as Moy_lat, Prediction From Fit Group By prediction""").show()

# 8) Creation de la data Frame avec prédiction et les noms
tab_a = bristol.withColumn("id", col("longitude") + col("latitude")) \
    .select(col("id"), col("name"))

tab_b = fitted.withColumn("id", col("longitude") + col("latitude")) \
    .drop(col("features"))

# verifions si nos id ont des doublons
tab_a.groupBy(col("id")).count().filter(col("count") >= 2).show()
tab_b.groupBy(col("id")).count().filter(col("count") >= 2).show()
# pas de doublons
dt = tab_a.join(tab_b, tab_a.id == tab_b.id, how="left").drop("id")
dt.show(3)
# Crée notre Fichier Excek
dt.toPandas().to_csv(path_to_output_data + "Kmeans_dt.csv")

# Carte
df = pd.read_csv(path_to_output_data + "Kmeans_dt.csv", )
df.head()

# Creation de la map
lonmean = df["longitude"].mean()
latmean = df["latitude"].mean()
map_bike = folium.Map(location=[latmean, lonmean],
                      zoom_start=13)


def color(prediction):
    if prediction == 0:
        col = 'green'
    elif prediction == 1:
        col = 'blue'
    else:
        col = 'red'
    return col


for latitude, longitude, name, prediction in zip(df['latitude'], df['longitude'], df['name'], df['prediction']):
    folium.Marker(location=[latitude, longitude], popup=name,
                  icon=folium.Icon(color=color(prediction),
                                   icon_color='yellow', icon='bicycle', prefix='fa')).add_to(map_bike)

map_bike.save(path_to_output_data + "carte_bristol.html")

fitted.drop("features")\
      .toPandas().to_csv(path_to_output_data+"fitted.csv")

spark.stop()