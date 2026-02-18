import json
import os

def charger_json_securise(chemin):
    try:
        # Vérification si le fichier est vide
        if os.path.exists(chemin) and os.path.getsize(chemin) == 0:
            print("❌ Fichier vide :", chemin)
            return None

        # Ouverture et chargement du JSON
        with open(chemin, "r") as f:
            data = json.load(f)


        print("✅", chemin, "chargé avec succès")
        return data

    except FileNotFoundError:
        print("❌ Fichier introuvable :", chemin)
        return None

    except json.JSONDecodeError as e:
        print("❌ JSON invalide dans", chemin, ":", e)
        return None

    except Exception as e:
        print("❌ Erreur inattendue :", e)
        return None

# Cas 1 : fichier normal
data = charger_json_securise("mission_data/missions.json")

# Cas 2 : fichier inexistant
data = charger_json_securise("mission_data/fantome.json")

# Cas 3 : créez un fichier corrompu pour tester
with open("mission_data/corrompu.json", "w") as f:
    f.write("{nom: valeur_sans_guillemets}")
data = charger_json_securise("mission_data/corrompu.json")