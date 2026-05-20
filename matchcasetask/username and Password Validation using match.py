# Username and Password Validation using match
username = input("Enter username: ")
password = input("Enter password: ")

match (username, password):
    case ("admin", "1234"):
        print("Login Successful")
    case ("admin", _):
        print("Incorrect Password")
    case _:
        print("Invalid Username")