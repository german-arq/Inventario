from typing import Dict, List

from numpy import product

def producto_mayor_precio(db: Dict):
    precio_mayor = max(producto[1] for producto in db.values())
    return precio_mayor
