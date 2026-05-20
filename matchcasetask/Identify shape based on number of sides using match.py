# Identify shape based on number of sides using match
sides = int(input("Enter number of sides: "))
match sides:
    case 3:
        print("Triangle")
    case 4:
        print("Quadrilateral")
    case 5:
        print("Pentagon")
    case 6:
        print("Hexagon")
    case 7:
        print("Heptagon")
    case 8:
        print("Octagon")
    case _:
        print("Shape not identified")