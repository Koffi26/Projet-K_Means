
# K-means Bristol City's Bikes 

##Lance Spark 
le Lancement du programme néccisite un invité de Commande. (.cmd ou .rc)
une fois dans l'invite de commande, il est demandé à l'utulisateur de se rendre dans le dossier où se trouves les dossiers

Enfin il est demander à l'utilisateur de taper la commande suivante 

```spark-submit Code_projet.py```

## Clusterings des vélos à Bristol City 

![img](https://tse1.mm.bing.net/th?id=OIP.PW3NSsCb0Yl-y4xqArGerwHaFH&pid=Api)

### Description des Variables

La ville de bristol city est composé de 149 vélos. Il nous a été demander de trouver un moyen afin de les regroupper.

L'objectif principal de ce projet est de proposer un k-means clustering de Bristol City Bike en fonction de l'emplacement des stations vélos en utilisant spark. 
Le fichier contient des informations concernant l’emplacement de chaque vélo. La base de donnée est fournis est disponible dans le fichier input ([Cliquer ici]("/input/Bristol-city-bike.json"))
-----------------------------------------------------------------------
Les 3 prmières valeurs sont donnée par le tableaux suivant

|             address|  latitude| longitude|                name|number|
|:-------------------|:---------|:---------|:-------------------|:----:|
|Lower River Tce /...|-27.482279|153.028723|122 - LOWER RIVER...|   122|
|Main St / Darragh St| -27.47059|153.036046|91 - MAIN ST / DA...|    91|
|Sydney St Ferry T...|-27.474531|153.042728|88 - SYDNEY ST FE...|    88|

Il est composé donc des variales suivante :
  - Adresse
  - Latitude
  - Longitude
  - name
  - number

Afin de trouvez les k-means nous décidons de garder uniquement les varaibles longitude
ainsi que latitude. En effet, cela nous permettra de le regrouper de façon géographique.

### Résultat du K-mean

Il a été demander de créer 3 groupes distincts. Ainsi nous avons trouvé les 3 groupes suivant :

- un premier groupe se placant à l'est ville
- un second groupe étant au centre de la ville
- une dernier groupe à l'ouest de ville. 

Les longitudes et latitudes moyens de chaque groupe est données par le tableaux ci-dessous.

|   Longitude moyen|      Latitude Moyen|Groupe      |
|:-----------------|:------------------ |:---------: |
|153.04186302272726|-27.46024+0636363633|     Est    |
|   153.02594553125| -27.47255990624999 |      Centre|
|153.00572882926832|-27.481218536585374 |      Ouest |

Afin d'avoir un aperçu, nous avons cartographier les vélos selon leurs appartenances à leurs groupes

[Carte](/exported/carte_bristol.html)



