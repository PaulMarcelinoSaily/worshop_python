#4.6. matchPernyataan
"""Bentuk paling sederhana membandingkan nilai subjek terhadap satu atau lebih literal:"""
def http_error(status):
    match status:
        case 400:
            return "Permintaan yang buruk"
        case 404:
            return "Tidak ditemukan"
        case 418:
            return "Saya teh poci"
        case _:
            return "Ada yang salah dengan internet"
        
print('*********************************')

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

print('*********************************')

case (Point(x1, y1), Point(x2, y2) as p2)

print('*********************************')

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")


