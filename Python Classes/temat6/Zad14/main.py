wejscie = [
    {'pomiar': 300.0, 'info': 'punkt A'},
    {'odczyt': 150.0, 'wysokosc': 100.0},
    {'dane': 20.0, 'glebokosc': 50.0, 'inny_parametr': 35.5},
]

def roznica_wysokosci(value=float(), wysokosc=None, glebokosc=None):
    if wysokosc is not None:
        return abs(value - wysokosc)
    elif glebokosc is not None:
        return abs(glebokosc - value)
    else:
        return value
    
for data in wejscie:
    value = next(
        (v for k, v in data.items() 
         if k not in ('wysokosc', 'glebokosc') and isinstance(v, (float))),
        None
    )
    
    result = roznica_wysokosci(
        value,
        wysokosc=data.get('wysokosc'),
        glebokosc=data.get('glebokosc')
    )
    print(result)
    