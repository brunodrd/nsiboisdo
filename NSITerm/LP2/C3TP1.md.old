Méthodes de programmation modulaire
================================

## Avantages d'une programmation modulaire

<div>
En première on a introduit les fonctions en réponse à la répétition de code au sein d'un programme. Cependant, la répétition des fonctions entre programmes est encore possible. Une solution est de regrouper ces fonctions et classes dans un <strong>module</strong>. On <strong>décompose</strong> ainsi une application en module(s) qui peuvent être <strong>développés indépendamment et réutilisés</strong> dans d'autres applications.  

Par ailleurs, cette organisation limite ou <strong>supprime les doublons</strong> de code, facilitant ainsi la maintenance (<em>un bug est corrigé une fois</em>).

Enfin, la programmation modulaire permet d'une certaine façon de <strong>cacher des détails d'implémentation</strong>, l'interaction utilisateur-module se faisant par le biais de l'interface.

Il s'agira dans le TP, de se placer en temps qu'utilisateur de modules en se référant à leur API, puis en temps que concepteur d'un module simple, dans l'activité.
</div>

## TP: traitement de données au format JSON

### Préambule: le format json
Un fichier `json` est un fichier texte contenant de l'information structurée, très utilisé sur internet. Cette structuration est assurée par des scalaires (nombre, booléen, chaîne) et des types d'éléments tels que:  

* des paires clé/valeur (qui rappelle les dictionnaires de python);
* de listes ordonnées de valeurs.  

Voir [json sur wikipedia](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation). Voici un exemple de données au format `json`:  
```json
{
    "menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
                { "value": "New", "onclick": "CreateNewDoc()" },
                { "value": "Open", "onclick": "OpenDoc()" },
                { "value": "Close", "onclick": "CloseDoc()" }
            ]
        }
    }
}
```

### Travail sur un fichier réel

Le [site openweathermap](https://openweathermap.org/) permet d'obtenir des informations météo dans beaucoup de villes du monde entier. Pour obtenir le temps dans une ville donnée, il faut fournir un identifiant unique ou la paire lattitude/longitude. 

Openweathermap propose un fichier `json` contenant les informations précédentes. Ce fichier a été téléchargé et une version zippée est fournie `city.zip`.  

!!! question "À faire"
    Dézipper ce fichier et retrouver ce notebook.
    
!!! danger "ATTENTION"
    Ne pas double-cliquer sur le fichier se situant dans le dossier `json`, pour ouvrir avec l'application par défaut. En effet, ce fichier a une taille de 33 Mo et plus de 2 millions de lignes!!


On préfèrera un traitement en ligne de commande pour voir la structure du fichier. On rappelle que l'utilisation de la ligne de commande est possible dans une cellule `jupyter notebook`, il suffit de préfixer la commande avec le caractère `!`.  

Enfin, pour plus de précisions sur une commande du *shell*, ne pas hésiter à consulter le manuel (exemple: `!man sed`).

!!! question "À faire"
    Que réalise la commande suivante ?


```python
!cat ./json/city.list.json | wc -l
```

    2095791


!!! question "À faire"
    Que réalise la commande suivante ?


```python
!cat ./json/city.list.json | grep -n "RE" | head -n 2
```

    238646:    "country": "RE",
    238656:    "country": "RE",


Enfin, pour avoir une meilleure idée du contenu du fichier, on affiche quelques lignes avec l'éditeur `sed` disponible avec le *shell*.


```python
# Affichage de 20 lignes
!sed -n "238642,+20p" ./json/city.list.json
```

      {
        "id": 935146,
        "name": "Les Trois-Bassins",
        "state": "",
        "country": "RE",
        "coord": {
          "lon": 55.299999,
          "lat": -21.1
        }
      },
      {
        "id": 935210,
        "name": "Salazie",
        "state": "",
        "country": "RE",
        "coord": {
          "lon": 55.539001,
          "lat": -21.02734
        }
      },
      {


### Les objectifs du TP

Le principal objectif de ce TP est d'exploiter un module fourni par la bibliothèque standard de python. Il sera très important de savoir utiliser la documentation du module afin d'extraire du fichier `json` fourni, **uniquement les informations concernant les villes de la Réunion mais aussi de sauvegarder ces dernières dans un fichier au format json**. Le fichier obtenu devrait être nettement moins lourd et plus facilement utilisable (une soixantaine d'entrées au lieu de plus de 200 000 dans le fichier original).  

??? tip "Rappels de 1re"
    Pour importer un module, on peut utiliser la syntaxe `import mon_super_module`; ce qui nous obligera à 
    préfixer chaque appel de fonction par `mon_super_module.ma_fonction()`. On peut *raccourcir* les appels en 
    utilisant un alias lors de l'import: `import mon_super_module as msp`, on appelle alors 
    `msp.ma_fonction()`.  
    Enfin, on peut cibler une fonction précise à importer. Dans ce cas, on utilisera la syntaxe: `from 
    mon_super_module import ma_fonction` et l'appel se fera directement par `ma_fonction()` sans préfixe.

### Travail à réaliser

!!! question "A faire"
    Prendre connaissance de l'api du module `json`, en ligne sur 
    [python.org](https://docs.python.org/fr/3.8/library/json.html) ou à défaut dans une cellule de Jupyter en 
    utilisant les fonctions `dir` et `help`.


```python
import json


dir(json)
```

!!! question "A faire"
    Quelles sont les deux fonctions du module `json` susceptibles de nous intéresser en vue d'une ouverture et 
    d'une écriture de fichiers json ? 
    Pour obtenir de l'aide sur une fonction présente dans un module on 
    utilise la fonction `help` (par exemple `help(json.xxxx)` où `xxxx` est le nom d'une fonction du module 
    `json`).  


```python
# Réponse
```

!!! question "A faire"
    On ne va extraire que les informations concernant les villes de la Réunion. Quelle fonction doit-on utiliser 
    pour transformer le fichier `city.list.json` présent sur le disque, en une structure de donnée utilisable en python ? Réaliser cette 
    opération en complétant le code ci-dessous.   


```python
import json

# Création d'un objet fichier f lié à city.list.json
with open('./json/city.list.json', 'r') as f:
    #A compléter (supprimer la ligne 'pass')
    pass
```

!!! question "A faire"
    Quelle est le type de la structure de donnée obtenue et combien d'entrées possède-t-elle? 


```python
# Réponse

```

!!! question "A faire"
    Afficher la première valeur de cette structure de donnée.


```python
# Réponse (donner la ligne de code + résultat)

```

!!! question "A faire"
    Proposer un code permettant de sauver les entrées qui ne concernent que la Réunion dans une *liste python*.


```python
# Réponse
villes_RE = []
# À compléter
```

!!! question "A faire"
    Combien d'entrées possède cette nouvelle liste ?


```python
# Réponse

```

!!! question "A faire"
    Quelle fonction devra-t-on utilser pour sauver cette liste dans un fichier `json` ?


```python
# Réponse

```

!!! question "A faire"
    Proposer un code qui réalise la sauvergarde la liste `villes_RE` dans un fichier `json` 
    `villes_RE.json`.


```python
#Réponse

# Création d'un objet fichier f lié à villes_RE.json
with open("./json/villes_RE.json", "w") as f:
    #à compléter ici
    pass           
```
