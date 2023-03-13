def create_tuple(x: int, y: int, z: int):
    point = ()
    sum = x + y + z
    if x < y < z:
        point = (x, z, sum)
    elif x < z < y:
        point = (x, y, sum)
    elif y < z < x:
        point = (y, x, sum)
    elif y < x < z:
        point = (y, z, sum)
    elif z < x < y:
        point = (z, y, sum)
    elif z < y < x:
        point = (z, x, sum)
    return point


