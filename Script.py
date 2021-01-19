#==================================================
#                    Groupe 15
#                 Bristol city Bike
#             Date de Rendu : 22.01.2021
#
#===================================================

from pyspark.sql import SparkSession
import configparser
from pyspark.sql.functions import col
from pyspark.sql.functions import lit
import folium
from folium.plugins import MarkerCluster
import pandas as pd

#1- Instancier Client Spark
spark=SparkSession.builder\
                  .master("local")\
                  .appName("Bristol")\
                  .getOrCreate()

#configurer les paths pour facilité l'accès aux différent dossiers
config = configparser.ConfigParser()
config.read('properties.conf')
path_to_input_data = config['Bristol-City-bike']['Input-data']
path_to_output_data = config['Bristol-City-bike']['Output-data']
num_partition_kmeans = (config['Bristol-City-bike']['Kmeans-level'])
#obliger de transformer la varible num_partition en int, considérer comme str au début
num_partition_kmeans= config.getint('Bristol-City-bike','Kmeans-level')

#importer les données bristol Park
bristol=spark.read.json(path_to_input_data)
#afficher les 3 premières valeurs de Bristol
bristol.show(3)

#selectionner les variables pertinante pour notre Kmeans
Kmean_df=bristol.select(col("latitude"),col("longitude"))
Kmean_df.show(3)

#Kmeans sur notre base de données
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
features = ("longitude","latitude")
kmeans = KMeans().setK(num_partition_kmeans).setSeed(1)
assembler = VectorAssembler(inputCols=features,outputCol="features")
dataset=assembler.transform(Kmean_df)
model = kmeans.fit(dataset)
fitted = model.transform(dataset)

fitted.columns
#fitted correponds a la sortie avec nos données + les prédiction( groupe d'appartenance)+features

fitted.groupBy("prediction").mean().show()
#affichier les moyenne par groupe
#methode sql
fitted.createOrReplaceTempView("Fit")

spark.sql("""select Avg(longitude) as Moy_Long,  Avg(latitude) as Moy_lat, Prediction From Fit Group By prediction""")\
     .show()

#Creation de la data Frame avec prédiction et les noms
tab_a=bristol.withColumn("id",col("longitude")+col("latitude")).select(col("id"),col("name"))
tab_b=fitted.withColumn("id",col("longitude")+col("latitude")).drop(col("features"))
#verifions si nos id ont des doublons
tab_a.groupBy(col("id")).count().filter(col("count")>=2).show()
tab_b.groupBy(col("id")).count().filter(col("count")>=2).show()
#pas de doublons
dt=tab_a.join(tab_b,tab_a.id==tab_b.id,how="left").drop("id")
dt.show(3)
#Crée notre Fichier Excek
dt.toPandas().to_csv(path_to_output_data+"Kmeans_dt.csv")
