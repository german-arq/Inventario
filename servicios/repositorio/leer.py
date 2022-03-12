from typing import Dict

def leer(db: Dict, codigo: int = None):    
    if codigo:
        return codigo, db.get(int(codigo))
    else:
        return db