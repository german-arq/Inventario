from typing import Dict, List

def actualizar(db: Dict, item: Dict[int, List]):
    db.update(item)
    return 'Item actualizado exitosamente'