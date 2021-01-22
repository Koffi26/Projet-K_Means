
# K-means Brisbane City's Bikes 

## Lancer Spark 

le Lancement du programme nécessite un invité de Commande. (.cmd ou .rc). 
Une fois dans l'invite de commande, il est demandé à l'utilisateur de se rendre dans le dossier où se trouve les dossiers

Enfin il est demandé à l'utilisateur de taper la commande suivante 

```spark-submit Script.py```

-------------------------------------------------------------------
## Clusterings des vélos à Brisbane City 
<p align= "center">
<img src="https://tse1.mm.bing.net/th?id=OIP.PW3NSsCb0Yl-y4xqArGerwHaFH&pid=Api"/>
  </p>

### Description des fichiers 
- Le dossier Data contient la base de données Brisbane-City-Bike
- Le dossier Exported comportent la carte Brisbane et les bases fitted et Kmeans
- Le Readme résume les résultats de notre analyse
- le fichier Properties.conf est un fichier retraçant les raccourcis de nos fichiers utilisés dans le projet
- Le Script contient le code utilisé à l'élaboration du Kmeans

### Description des Variables

La ville de Brisbane City est composée de 149 vélos. Il nous a été demandé de trouver un moyen afin de les regrouper par classe.

L'objectif principal de ce projet est de proposer un k-means clustering de Brisbane City Bike en fonction de l'emplacement des stations vélos en utilisant spark. 
Le fichier contient des informations concernant l’emplacement de chaque vélo. La base de donnée fournie est disponible dans le fichier input ([Cliquer ici](data/Bristol-city-bike.json))


-----------------------------------------------------------------------
Les 3 premières valeurs sont données par le tableau suivant :

|             address|  latitude| longitude|                name|number|
|:-------------------|:---------|:---------|:-------------------|:----:|
|Lower River Tce /...|-27.482279|153.028723|122 - LOWER RIVER...|   122|
|Main St / Darragh St| -27.47059|153.036046|91 - MAIN ST / DA...|    91|
|Sydney St Ferry T...|-27.474531|153.042728|88 - SYDNEY ST FE...|    88|

Il est composé donc des variables suivantes :
  - Adresse : lieu où se trouve les vélos
  - Latitude : Position latitude
  - Longitude : Position longitude
  - name : le numéro plus l'adresse
  - number : le numéro attribué à chaque vélo

Afin de trouver les k-means nous décidons de garder uniquement les variables longitude
ainsi que latitude. En effet, cela nous permettra de le regrouper de façon géographique.

### Résultat du K-mean

Il a été demandé de créer 3 groupes distincts.
Le k-means a permis donc de faire emerger les groupes suivants :

- un premier groupe se placant à l'est ville
- un second groupe étant au centre de la ville
- une dernier groupe à l'ouest de ville. 

un fichier excel, récapitulatif de l'intégralité des resultats k-means est disponible dans le fichier exported. [(Cliquer ici)](exported/fitted.csv)

Les longitudes et latitudes moyennes de chaque groupe sont données par le tableaux ci-dessous.

|   Longitude moyen|      Latitude Moyen|Groupe      |
|:-----------------|:------------------ |:---------: |
|153.04186302272726|-27.46024+0636363633|     Est    |
|   153.02594553125| -27.47255990624999 |      Centre|
|153.00572882926832|-27.481218536585374 |      Ouest |

Afin d'avoir un aperçu, nous avons cartographié les vélos selon leurs appartenances à leurs groupes

![image](https://user-images.githubusercontent.com/71498491/105109160-3be2c180-5abc-11eb-81e0-f1a24f80522d.png)

La photo ci-dessus représente la carte avec l'emplacement des vélos.
La photo ci-dessous est assez représentative des 3 groupes, nous pouvons ainsi clairement les distinguer. un groupe est plus axé à l'est, un second à l'ouest et enfin un dernier au centre.

La version dynamique de la carte est disponible en <a href="https://ghcdn.rawgit.org/Koffi26/Projet-K_Means/draft/exported/carte_bristol.html" target="_blank">cliquant ici</a>


