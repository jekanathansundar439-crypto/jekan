# Traffic Signal Program using match
color = input("Enter traffic signal color (Red, Yellow, Green): ")
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid signal color")