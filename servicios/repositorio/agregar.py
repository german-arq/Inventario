from typing import Dict, List

def agregar(db: Dict, valores: List):
    nuevo_codigo = max(db.keys())
    db[nuevo_codigo] = valores
    return True