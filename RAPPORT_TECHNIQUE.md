# Rapport de Projet - Gestion des Étudiants

**Nom :** Emmanuel ZERBIB
**Date :** 30 septembre 2024
**Cours :** Programmation Python

## Introduction

Pour ce projet, j'ai fait un programme en Python qui gère les étudiants d'une école et leurs notes. C'était pas évident au début mais j'ai réussi à faire quelque chose qui marche bien.

Le prof nous avait demandé d'utiliser différentes structures de données donc j'ai essayé de bien les répartir dans mon code.

## Mes Choix de Structures

### Le dictionnaire principal
J'ai mis tous les étudiants dans un dictionnaire :
```python
self.etudiants = {}
```

C'était le plus logique pour moi parce que comme ça avec l'ID je peux retrouver un étudiant rapidement. C'est comme un annuaire en fait.

Chaque étudiant c'est ça :
```python
{
    'nom': 'Dupont',
    'prenom': 'Alice',
    'id': 101,
    'notes': [('Math', 16), ('Python', 14)]
}
```

### Pour éviter les doublons d'ID
```python
self.ids_utilises = set()
```

J'ai appris que les sets c'est bien pour vérifier si quelque chose existe déjà. Du coup quand j'ajoute un étudiant je regarde si son ID est déjà dans le set.

### La liste des matières
Au début j'avais mis un frozenset mais finalement j'ai changé pour une liste normale :
```python
self.matieres_disponibles = [
    "Math", "Python", "JavaScript", "Base de données",
    "Algorithmique", "Réseaux", "Systèmes", "Web", "Mobile"
]
```

C'est plus simple et ça marche pareil pour ce que je veux faire.

### Les notes en tuples
Pour les notes j'ai fait des tuples dans une liste :
```python
[('Math', 16), ('Python', 14)]
```

Comme ça la matière et la note vont ensemble. J'aurais pu faire un dictionnaire mais les tuples c'est plus simple.

## Ce que j'ai appris

### Les boucles if/elif
Pour le menu j'ai utilisé des if/elif classiques :
```python
if choix == "1":
    # ajouter étudiant
elif choix == "2":
    # modifier notes
```

C'est ce qu'on a vu en cours et ça marche bien.

### Calculs de moyennes
Pour calculer les moyennes j'ai fait ça étape par étape :
```python
total = 0
for matiere, note in notes:
    total += note
moyenne = total / len(notes)
```

C'est pas très optimisé mais au moins c'est clair.

### Gestion des erreurs
J'ai mis des try/except pour éviter que le programme plante :
```python
try:
    etudiant_id = int(input("ID: "))
except:
    print("ID invalide")
```

## Ce que fait mon programme

1. On peut ajouter des étudiants avec leurs notes
2. Modifier les notes d'un étudiant
3. Supprimer un étudiant (avec confirmation)
4. Voir toutes les stats : moyennes, classements, etc.
5. Trouver les bons élèves (moyenne > 15)

## Mes galères

Au début j'avais du mal avec le parsing des notes. Le format "Math,16;Python,14" c'était pas évident à découper. J'ai fait plusieurs versions avant que ça marche.

Aussi j'oubliais souvent de vérifier si les notes étaient entre 0 et 20. Du coup mon programme acceptait des notes à 25 ou -5...

Pour l'affichage j'ai galéré avec les alignements. Les colonnes étaient toutes décalées au début.

## Ce que je pourrais améliorer

- Sauvegarder dans un fichier pour garder les données
- Faire une vraie interface graphique
- Ajouter plus de stats comme la médiane
- Permettre d'importer depuis Excel
- Ajouter des commentaires sur les étudiants

## Conclusion

Ce projet m'a bien aidé à comprendre les dictionnaires et les autres structures Python. Au final mon programme fait tout ce qui était demandé même si le code est pas parfait.

J'ai appris qu'il faut toujours vérifier les données qu'entre l'utilisateur sinon ça plante. Et aussi que faire des petites fonctions c'est mieux que tout mettre dans une grosse fonction.

C'était intéressant à faire même si par moments c'était frustrant quand ça marchait pas !