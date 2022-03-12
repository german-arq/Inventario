from typing import Dict, List

def print_dict(db: Dict):
    for key, value in db.items():
        print(f'{key}. Nombre: {value[0]} \t Precio: ${value[1]} \t Cantidad: {value[2]} ' )