import requests
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

API_TOKEN = os.getenv("BUBBLE_API_TOKEN")
BASE_URL = os.getenv("BUBBLE_BASE_URL")

def load_brief(company_id: str) -> str:
    url = f"{BASE_URL}/{company_id}"
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Extraction directe du brief
        brief = data.get("response", {}).get("final_brief", None)

        if not brief:
            print(f"Brief non trouvé pour l'entreprise {company_id}")
        return brief

    except requests.RequestException as e:
        print(f"Erreur lors du chargement du Brief : {e}")
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    company_id = "1745237684459x750813329623613400"
    brief_text = load_brief(company_id)
    print(brief_text)