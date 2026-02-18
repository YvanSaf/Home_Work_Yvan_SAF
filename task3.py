import json
import os

# Vérification de l'existence du fichier(c'est vrai que cette étape n'a pas été demandée, mais pour des raisons de sécuité, je l'ai mis
fichier = "mission_data/missions.json"
if not os.path.exists(fichier):
    print("Erreur : le fichier missions.json n'existe pas !")
else:
    # Chargement du JSON
    with open(fichier, "r") as f:
        data = json.load(f)
    # Recupération de la liste des missions
    missions = data["missions"]

    total_budget = 0
    plus_longue = missions[0]
    plus_courte = missions[0]

    # J'utilise une boucle sur chaque mission
    for mission in missions:
        id_msn = mission["id"]
        nom = mission["nom"]
        destination = mission["destination"]
        duree = mission["duree_jours"]
        equipage = len(mission["equipage"])
        budget = mission["budget_millions_usd"]

        # Affichage du résumé
        print(f"[{id_msn}] {nom} → {destination} | {duree} jours | Équipage : {equipage} | Budget : {budget:,} M$")

        # Calcul du budget total
        total_budget += budget

        # Vérification de la durée de la mission la plus longue et la plus courte
        if duree > plus_longue["duree_jours"]:
            plus_longue = mission
        if duree < plus_courte["duree_jours"]:
            plus_courte = mission

    print("\nBudget total de toutes les missions :", f"{total_budget:,} M$")
    print("Mission la plus longue :", f"{plus_longue['nom']} → {plus_longue['duree_jours']} jours")
    print("Mission la plus courte :", f"{plus_courte['nom']} → {plus_courte['duree_jours']} jours")
