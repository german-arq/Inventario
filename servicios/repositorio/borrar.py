from typing import Dict

def borrar(db: Dict, codigo: int):
    borrar = db.pop(codigo, None)
    if borrar:
        return True
    else:
        return False