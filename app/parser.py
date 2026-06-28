import json

def load_alert(path: str):
    """
    Charge une alerte SOC depuis un fichier JSON
    """
    with open(path, "r") as f:
        alert = json.load(f)

    return alert