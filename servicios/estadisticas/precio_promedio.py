from typing import Dict, List

def precio_promedio(db: Dict):
    promedio = sum([producto[1] for producto in db.values()]) / len(db)
    return promedio