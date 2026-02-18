# Ouverture du fichier journal en lecture
fichier = open("mission_data/journal_bord.txt", "r")
lignes = fichier.readlines()
fichier.close()

# Affichage du nombre total de lignes
print("Journal de bord :", len(lignes), "entrées")

# Recherche des lignes contenant "Alerte" ou "alerte"
alertes = []
for ligne in lignes:
    if "Alerte" in ligne or "alerte" in ligne:
        alertes.append(ligne)

# Affichage des alertes
print("--- Alertes détectées (", len(alertes), ") ---")
for alerte in alertes:
    print(alerte.strip())

# Écriture des alertes dans un nouveau fichier
fichier_alertes = open("mission_data/alertes.txt", "w")
for alerte in alertes:
    fichier_alertes.write(alerte)
fichier_alertes.close()

print("✅ Fichier alertes.txt créé.")
