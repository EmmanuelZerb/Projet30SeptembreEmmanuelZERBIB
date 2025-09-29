# Tests de Mon Programme

## Mes Tests

J'ai pas mal testé mon programme pour être sûr qu'il marche bien. Voici ce que j'ai fait.

### Premier test : ajouter des étudiants

J'ai commencé par ajouter quelques étudiants :

```
Étudiant Alice Dupont (ID: 101) ajouté avec succès.
Étudiant Bob Martin (ID: 102) ajouté avec succès.
Étudiant Claire Durand (ID: 103) ajouté avec succès.
```

J'ai rentré ces notes :
- Alice : Math,16;Python,14;Web,18
- Bob : Math,12;Python,18;Web,15
- Claire : Math,18;Python,16;Web,17

Ça a bien marché du premier coup.

### Test des moyennes

Après j'ai regardé si les moyennes étaient bonnes :

```
Alice Dupont: 16.00/20
Bob Martin: 15.00/20
Claire Durand: 17.00/20
```

J'ai refait le calcul pour Alice avec ma calculette : (16+14+18) ÷ 3 = 48 ÷ 3 = 16.00
C'est bon !

### Moyennes par matière

```
Math: 15.33/20
Python: 16.00/20
Web: 16.67/20
```

Pour vérifier Python : (14+18+16) ÷ 3 = 48 ÷ 3 = 16.00 ✓

### Les bons élèves

Mon programme trouve bien ceux qui ont plus de 15 :

```
Claire Durand: 17.00/20
Alice Dupont: 16.00/20
```

Bob a 15 pile donc il n'apparaît pas (c'est normal, c'est > 15).

## Comment j'utilise le programme

### Ajouter quelqu'un

```
============================================================
SYSTÈME DE GESTION DES ÉTUDIANTS
============================================================
1. Ajouter un étudiant
2. Modifier les notes
3. Supprimer un étudiant
4. Afficher les statistiques
5. Quitter
------------------------------------------------------------
Votre choix (1-5): 1

AJOUT D'UN NOUVEL ÉTUDIANT
-----------------------------------
Nom: Moreau
Prénom: Sophie
ID (nombre entier): 104

Matières disponibles:
------------------------------
 1. Algorithmique
 2. Base de données
 3. JavaScript
 4. Math
 5. Mobile
 6. Python
 7. Réseaux
 8. Systèmes
 9. Web
------------------------------
Matières et notes (format 'Matière,note;Matière,note'): Math,19;Python,15

Étudiant Sophie Moreau (ID: 104) ajouté avec succès.
```

L'affichage des matières c'est pratique, on sait quoi écrire.

### Voir toutes les stats

```
Votre choix (1-5): 4

============================================================
STATISTIQUES GÉNÉRALES
============================================================
Nombre total d'étudiants: 4
Moyenne générale de la promotion: 16.25/20
Nombre de matières enseignées: 3

----------------------------------------
MOYENNES PAR MATIÈRE
----------------------------------------
 1. Math                 : 16.25/20
 2. Python               : 15.75/20
 3. Web                  : 16.67/20

----------------------------------------
CLASSEMENT PAR MÉRITE
----------------------------------------
Rang  Nom             Prénom          Moyenne  Matières
-----------------------------------------------------------------
1     Moreau          Sophie          17.00    2
2     Durand          Claire          17.00    3
3     Dupont          Alice           16.00    3
4     Martin          Bob             15.00    3
```

C'est pas mal organisé je trouve.

### Changer des notes

```
Votre choix (1-5): 2

MODIFICATION DES NOTES
----------------------------
ID: 101 - Alice Dupont
ID: 102 - Bob Martin
ID: 103 - Claire Durand
ID: 104 - Sophie Moreau
ID de l'étudiant à modifier: 102
Nouvelles matières et notes: Math,14;Python,19;Web,16

Notes de Bob Martin mises à jour.
```

### Supprimer quelqu'un

```
Votre choix (1-5): 3

ID de l'étudiant à supprimer: 102
Confirmer la suppression de Bob Martin ? (oui/non): oui

Étudiant Bob Martin (ID: 102) supprimé avec succès.
```

La confirmation c'est bien, ça évite les erreurs.

## Tests d'erreurs

J'ai aussi testé quand on fait des bêtises :

### ID déjà pris
```
ID (nombre entier): 101
Erreur: L'ID 101 est déjà utilisé.
```

### Note trop haute
```
Matières et notes: Math,25;Python,14
Erreur: La note 25.0 pour Math doit être entre 0 et 20.
```

### Mauvais format
```
Matières et notes: Math;Python,14
Format de note invalide pour Math:
```

### ID pas un nombre
```
ID (nombre entier): abc
ID invalide. Veuillez saisir un nombre entier.
```

## Mes problèmes pendant le dev

Au début ça marchait pas terrible. J'avais oublié de vérifier si l'étudiant avait des notes avant de calculer sa moyenne. Du coup ça faisait une division par zéro et ça plantait.

J'ai aussi eu du mal avec le parsing. Découper "Math,16;Python,14" c'était compliqué au début. J'ai fait plusieurs essais avec split() avant de trouver la bonne méthode.

Pour l'affichage des tableaux j'ai galéré aussi. Les colonnes étaient pas alignées. J'ai appris à utiliser les formats comme `{nom:<15}` pour que ce soit plus joli.

## Ce que j'ai vérifié

- ✓ Toutes les fonctions marchent
- ✓ Les erreurs sont bien gérées
- ✓ Les calculs sont justes
- ✓ Le menu avec if/elif fonctionne
- ✓ Les structures de données sont utilisées
- ✓ L'enumerate() pour numéroter les listes

## Conclusion

Mon programme fait ce qu'il faut ! J'ai testé plein de cas différents et ça marche. C'est vrai que c'est pas le code le plus beau du monde mais ça fonctionne bien.

J'ai appris pas mal de trucs sur Python avec ce projet. Surtout sur les dictionnaires et comment bien gérer les erreurs de l'utilisateur.