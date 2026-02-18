import os

# Vérification de l'existence du dossier
if not os.path.exists("mission_data"):
    print("Erreur : le dossier mission_data n'existe pas !")
else:
    print("📂 mission_data/")

    # Affichage de la liste des fichiers et leur taille en "K"
    os.system("ls -lh mission_data | grep -v '^d' | awk '{printf \"   📄 %s\\t(%s)\\n\", $9, $5}'")

    # Création des sous-dossiers s'ils n'existent pas
    os.system("mkdir -p mission_data/rapports")
    print("   📁 rapports/       [créé]")

    os.system("mkdir -p mission_data/archives")
    print("   📁 archives/       [créé]")
