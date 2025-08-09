
def is_bulky(width: int, height: int, length: int):
    greater_than_1m = width * height * length >= 1_000_000
    dimensions_gte_150cm = (width >= 150) or (height >= 150) or (length >= 150)
    
    return greater_than_1m or dimensions_gte_150cm

def is_heavy(mass: int):
    return mass >= 20

STANDARD = "STANDARD"
SPECIAL = "SPECIAL"
REJECTED = "REJECTED"

def sort(width: int, height: int, length: int, mass: int):
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)
    
    if not (bulky or heavy):
        return STANDARD
    
    if bulky and heavy:
        return REJECTED
    
    if bulky or heavy:
        return SPECIAL