from typing import Dict, List

from numpy import product

def producto_menor_precio(db: Dict):
    precio_menor = min([producto[1] for producto in db.values()])
    return precio_menor