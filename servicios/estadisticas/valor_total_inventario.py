from typing import Dict

def valor_total_inventario(db: Dict):
    total = 0
    for producto in db.values():
        total += producto[1] * producto[2]
    return total