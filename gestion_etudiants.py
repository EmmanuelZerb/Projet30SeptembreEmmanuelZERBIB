# Projet de gestion des étudiants
# Emmanuel ZERBIB - 30 septembre 2024
# Système pour gérer les notes des étudiants d'une école

import json


class GestionEtudiants:

    def __init__(self):
        self.etudiants = {}
        self.ids_utilises = set()
        # Liste des matières qu'on peut enseigner
        self.matieres_disponibles = [
            "Math", "Python", "JavaScript", "Base de données",
            "Algorithmique", "Réseaux", "Systèmes", "Web", "Mobile"
        ]

    def ajouter_etudiant(self, nom, prenom, etudiant_id, matieres_notes):
        try:
            if etudiant_id in self.ids_utilises:
                print(f"Erreur: L'ID {etudiant_id} est déjà utilisé.")
                return False

            for matiere, note in matieres_notes:
                if not (0 <= note <= 20):
                    print(f"Erreur: La note {note} pour {matiere} doit être entre 0 et 20.")
                    return False

            self.etudiants[etudiant_id] = {
                'nom': nom.strip().title(),
                'prenom': prenom.strip().title(),
                'id': etudiant_id,
                'notes': matieres_notes.copy()
            }

            self.ids_utilises.add(etudiant_id)
            print(f"Étudiant {prenom} {nom} (ID: {etudiant_id}) ajouté avec succès.")
            return True

        except Exception as e:
            print(f"Erreur lors de l'ajout: {e}")
            return False

    def modifier_notes_etudiant(self, etudiant_id, nouvelles_notes):
        try:
            if etudiant_id not in self.etudiants:
                print(f"Erreur: Aucun étudiant trouvé avec l'ID {etudiant_id}.")
                return False

            for matiere, note in nouvelles_notes:
                if not (0 <= note <= 20):
                    print(f"Erreur: La note {note} pour {matiere} doit être entre 0 et 20.")
                    return False

            self.etudiants[etudiant_id]['notes'] = nouvelles_notes.copy()
            etudiant = self.etudiants[etudiant_id]
            print(f"Notes de {etudiant['prenom']} {etudiant['nom']} mises à jour.")
            return True

        except Exception as e:
            print(f"Erreur lors de la modification: {e}")
            return False

    def supprimer_etudiant(self, etudiant_id):
        try:
            if etudiant_id not in self.etudiants:
                print(f"Erreur: Aucun étudiant trouvé avec l'ID {etudiant_id}.")
                return False

            etudiant = self.etudiants[etudiant_id]
            nom_complet = f"{etudiant['prenom']} {etudiant['nom']}"

            del self.etudiants[etudiant_id]
            self.ids_utilises.remove(etudiant_id)

            print(f"Étudiant {nom_complet} (ID: {etudiant_id}) supprimé avec succès.")
            return True

        except Exception as e:
            print(f"Erreur lors de la suppression: {e}")
            return False

    def calculer_moyenne_etudiant(self, etudiant_id):
        # Vérification si l'étudiant existe
        if etudiant_id not in self.etudiants:
            return None

        notes = self.etudiants[etudiant_id]['notes']
        if len(notes) == 0:
            return 0.0

        # Je récupère juste les notes (pas les matières)
        total = 0
        for matiere, note in notes:
            total += note

        moyenne = total / len(notes)
        return moyenne

    def calculer_moyenne_par_matiere(self):
        # Dictionnaire pour grouper les notes par matière
        notes_par_matiere = {}

        # Je parcours tous les étudiants
        for etudiant in self.etudiants.values():
            for matiere, note in etudiant['notes']:
                if matiere not in notes_par_matiere:
                    notes_par_matiere[matiere] = []
                notes_par_matiere[matiere].append(note)

        # Calcul des moyennes
        moyennes = {}
        for matiere in notes_par_matiere:
            notes = notes_par_matiere[matiere]
            if len(notes) > 0:
                moyenne = sum(notes) / len(notes)
                moyennes[matiere] = moyenne

        return moyennes

    def trouver_etudiants_excellence(self, seuil=15.0):
        try:
            etudiants_excellence = []

            for etudiant_id, etudiant in self.etudiants.items():
                moyenne = self.calculer_moyenne_etudiant(etudiant_id)

                if moyenne is not None and moyenne > seuil:
                    etudiants_excellence.append({
                        'id': etudiant_id,
                        'nom': etudiant['nom'],
                        'prenom': etudiant['prenom'],
                        'moyenne': moyenne
                    })

            etudiants_excellence.sort(key=lambda x: x['moyenne'], reverse=True)
            return etudiants_excellence

        except Exception as e:
            print(f"Erreur lors de la recherche d'excellence: {e}")
            return []

    def generer_rapport_global(self):
        if len(self.etudiants) == 0:
            return {
                'nombre_etudiants': 0,
                'moyenne_promotion': 0.0,
                'etudiants_par_merite': [],
                'moyennes_par_matiere': {},
                'etudiants_excellence': []
            }

        # Calcul de la moyenne de la promotion
        total_moyennes = 0
        nombre_moyennes = 0
        for etudiant_id in self.etudiants:
            moyenne = self.calculer_moyenne_etudiant(etudiant_id)
            if moyenne is not None:
                total_moyennes += moyenne
                nombre_moyennes += 1

        moyenne_promotion = 0
        if nombre_moyennes > 0:
            moyenne_promotion = total_moyennes / nombre_moyennes

        # Liste des étudiants pour le classement
        etudiants_merite = []
        for etudiant_id in self.etudiants:
            etudiant = self.etudiants[etudiant_id]
            moyenne = self.calculer_moyenne_etudiant(etudiant_id)
            if moyenne is not None:
                etudiants_merite.append({
                    'rang': 0,
                    'id': etudiant_id,
                    'nom': etudiant['nom'],
                    'prenom': etudiant['prenom'],
                    'moyenne': moyenne,
                    'nombre_matieres': len(etudiant['notes'])
                })

        # Tri par moyenne (du plus grand au plus petit)
        etudiants_merite.sort(key=lambda x: x['moyenne'], reverse=True)

        # Attribution des rangs
        for i in range(len(etudiants_merite)):
            etudiants_merite[i]['rang'] = i + 1

        # Moyennes par matière arrondies
        moyennes_matieres = self.calculer_moyenne_par_matiere()
        moyennes_arrondies = {}
        for matiere in moyennes_matieres:
            moyennes_arrondies[matiere] = round(moyennes_matieres[matiere], 2)

        # Statistiques avancées
        meilleures_moyennes = []
        for etudiant_id in self.etudiants:
            moyenne = self.calculer_moyenne_etudiant(etudiant_id)
            if moyenne is not None:
                meilleures_moyennes.append(moyenne)

        meilleure = 0
        moins_bonne = 0
        if len(meilleures_moyennes) > 0:
            meilleure = max(meilleures_moyennes)
            moins_bonne = min(meilleures_moyennes)

        # Compte des matières différentes
        matieres_utilisees = set()
        for etudiant in self.etudiants.values():
            for matiere, note in etudiant['notes']:
                matieres_utilisees.add(matiere)

        rapport = {
            'date_generation': None,
            'nombre_etudiants': len(self.etudiants),
            'moyenne_promotion': round(moyenne_promotion, 2),
            'etudiants_par_merite': etudiants_merite,
            'moyennes_par_matiere': moyennes_arrondies,
            'etudiants_excellence': self.trouver_etudiants_excellence(),
            'statistiques_avancees': {
                'meilleure_moyenne': meilleure,
                'moins_bonne_moyenne': moins_bonne,
                'nombre_matieres_total': len(matieres_utilisees)
            }
        }

        return rapport

    def afficher_statistiques(self):
        try:
            if not self.etudiants:
                print("Aucun étudiant enregistré dans le système.")
                return

            rapport = self.generer_rapport_global()

            print("\n" + "="*60)
            print("STATISTIQUES GÉNÉRALES")
            print("="*60)
            print(f"Nombre total d'étudiants: {rapport['nombre_etudiants']}")
            print(f"Moyenne générale de la promotion: {rapport['moyenne_promotion']}/20")
            print(f"Nombre de matières enseignées: {rapport['statistiques_avancees']['nombre_matieres_total']}")

            if rapport['statistiques_avancees']['meilleure_moyenne'] > 0:
                print(f"Meilleure moyenne: {rapport['statistiques_avancees']['meilleure_moyenne']:.2f}/20")
                print(f"Moins bonne moyenne: {rapport['statistiques_avancees']['moins_bonne_moyenne']:.2f}/20")

            print("\n" + "-"*40)
            print("MOYENNES PAR MATIÈRE")
            print("-"*40)
            moyennes_matieres = rapport['moyennes_par_matiere']
            if moyennes_matieres:
                for i, (matiere, moyenne) in enumerate(sorted(moyennes_matieres.items()), 1):
                    print(f"{i:2d}. {matiere:<20} : {moyenne:5.2f}/20")
            else:
                print("Aucune donnée de matière disponible.")

            print("\n" + "-"*40)
            print("CLASSEMENT PAR MÉRITE")
            print("-"*40)
            etudiants_merite = rapport['etudiants_par_merite']
            if etudiants_merite:
                print(f"{'Rang':<5} {'Nom':<15} {'Prénom':<15} {'Moyenne':<8} {'Matières'}")
                print("-" * 65)
                for etudiant in etudiants_merite[:10]:
                    print(f"{etudiant['rang']:<5} {etudiant['nom']:<15} "
                          f"{etudiant['prenom']:<15} {etudiant['moyenne']:<8.2f} "
                          f"{etudiant['nombre_matieres']}")

            print("\n" + "-"*40)
            print("ÉTUDIANTS D'EXCELLENCE (>15/20)")
            print("-"*40)
            etudiants_excellence = rapport['etudiants_excellence']
            if etudiants_excellence:
                for i, etudiant in enumerate(etudiants_excellence, 1):
                    print(f"{i}. {etudiant['prenom']} {etudiant['nom']} - {etudiant['moyenne']:.2f}/20")
            else:
                print("Aucun étudiant n'a une moyenne supérieure à 15/20.")

            print("="*60)

        except Exception as e:
            print(f"Erreur lors de l'affichage des statistiques: {e}")


def parser_matieres_notes(texte_matieres):
    # Liste pour stocker les tuples (matière, note)
    matieres_notes = []

    # Si rien n'est saisi, on retourne une liste vide
    if len(texte_matieres.strip()) == 0:
        return matieres_notes

    # On sépare par point-virgule
    elements = texte_matieres.split(';')

    # Pour chaque élément
    for element in elements:
        element = element.strip()
        if ',' in element:
            # On sépare matière et note
            parties = element.split(',', 1)
            if len(parties) == 2:
                matiere = parties[0].strip()
                texte_note = parties[1].strip()

                # Conversion en nombre
                try:
                    note = float(texte_note)
                    # Vérification que la note est valide
                    if note >= 0 and note <= 20:
                        matieres_notes.append((matiere, note))
                    else:
                        print(f"Note ignorée pour {matiere}: {note} (doit être entre 0 et 20)")
                except:
                    print(f"Format de note invalide pour {matiere}: {texte_note}")

    return matieres_notes


def afficher_menu():
    print("\n" + "="*60)
    print("SYSTÈME DE GESTION DES ÉTUDIANTS")
    print("="*60)
    print("1. Ajouter un étudiant")
    print("2. Modifier les notes")
    print("3. Supprimer un étudiant")
    print("4. Afficher les statistiques")
    print("5. Quitter")
    print("-"*60)


def main():
    gestionnaire = GestionEtudiants()

    print("Bienvenue dans le Système de Gestion des Étudiants!")
    print("Développé par Emmanuel ZERBIB - Projet 30 Septembre")

    while True:
        try:
            afficher_menu()
            choix = input("Votre choix (1-5): ").strip()

            # Menu avec if/elif au lieu de match-case
            if choix == "1":
                print("\nAJOUT D'UN NOUVEL ÉTUDIANT")
                print("-" * 35)
                try:
                    nom = input("Nom: ").strip()
                    prenom = input("Prénom: ").strip()

                    if len(nom) == 0 or len(prenom) == 0:
                        print("Le nom et le prénom sont obligatoires.")
                        continue

                    etudiant_id = int(input("ID (nombre entier): "))

                    print("\nMatières disponibles:")
                    print("-" * 30)
                    # J'affiche les matières disponibles
                    matieres_triees = sorted(gestionnaire.matieres_disponibles)
                    for i in range(len(matieres_triees)):
                        print(f"{i+1:2d}. {matieres_triees[i]}")
                    print("-" * 30)

                    texte_matieres = input("Matières et notes (format 'Matière,note;Matière,note'): ")

                    matieres_notes = parser_matieres_notes(texte_matieres)

                    if len(matieres_notes) == 0:
                        print("Aucune matière valide saisie.")
                        continue

                    gestionnaire.ajouter_etudiant(nom, prenom, etudiant_id, matieres_notes)

                except ValueError:
                    print("ID invalide. Veuillez saisir un nombre entier.")
                except Exception as e:
                    print(f"Erreur: {e}")

            elif choix == "2":
                print("\nMODIFICATION DES NOTES")
                print("-" * 28)
                try:
                    if len(gestionnaire.etudiants) == 0:
                        print("Aucun étudiant enregistré.")
                        continue

                    # J'affiche tous les étudiants
                    for etudiant_id in gestionnaire.etudiants:
                        etudiant = gestionnaire.etudiants[etudiant_id]
                        print(f"ID: {etudiant_id} - {etudiant['prenom']} {etudiant['nom']}")

                    etudiant_id = int(input("ID de l'étudiant à modifier: "))

                    if etudiant_id not in gestionnaire.etudiants:
                        print(f"Aucun étudiant avec l'ID {etudiant_id}.")
                        continue

                    texte_matieres = input("Nouvelles matières et notes: ")

                    nouvelles_notes = parser_matieres_notes(texte_matieres)

                    if len(nouvelles_notes) > 0:
                        gestionnaire.modifier_notes_etudiant(etudiant_id, nouvelles_notes)
                    else:
                        print("Aucune note valide saisie.")

                except ValueError:
                    print("ID invalide.")
                except Exception as e:
                    print(f"Erreur: {e}")

            elif choix == "3":
                print("\nSUPPRESSION D'UN ÉTUDIANT")
                print("-" * 31)
                try:
                    if len(gestionnaire.etudiants) == 0:
                        print("Aucun étudiant enregistré.")
                        continue

                    # J'affiche tous les étudiants
                    for etudiant_id in gestionnaire.etudiants:
                        etudiant = gestionnaire.etudiants[etudiant_id]
                        print(f"ID: {etudiant_id} - {etudiant['prenom']} {etudiant['nom']}")

                    etudiant_id = int(input("ID de l'étudiant à supprimer: "))

                    if etudiant_id in gestionnaire.etudiants:
                        etudiant = gestionnaire.etudiants[etudiant_id]
                        confirmation = input(f"Confirmer la suppression de {etudiant['prenom']} {etudiant['nom']} ? (oui/non): ")

                        if confirmation.lower() == 'oui' or confirmation.lower() == 'o':
                            gestionnaire.supprimer_etudiant(etudiant_id)
                        else:
                            print("Suppression annulée.")
                    else:
                        print(f"Aucun étudiant avec l'ID {etudiant_id}.")

                except ValueError:
                    print("ID invalide.")
                except Exception as e:
                    print(f"Erreur: {e}")

            elif choix == "4":
                gestionnaire.afficher_statistiques()

            elif choix == "5":
                print("\nMerci d'avoir utilisé le Système de Gestion des Étudiants!")
                print("Au revoir!")
                break

            else:
                print("Choix invalide. Veuillez saisir un nombre entre 1 et 5.")

        except KeyboardInterrupt:
            print("\n\nProgramme interrompu par l'utilisateur.")
            break
        except Exception as e:
            print(f"Erreur inattendue: {e}")


if __name__ == "__main__":
    main()