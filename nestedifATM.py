#atm
db_acc=12345678910
db_pin=1234
db_saving=30000
accnum =int(input("enter your acc number:")) 
pin =int(input("enter your pin num:"))
if(db_acc == accnum):
    if(db_pin ==  pin):
        amt=int(input("enter your amt:"))
        if(db_saving >= amt):
            print("cash was withdraw")
        else:
            print("invalid amt")
    else:
        print("invalid pin")
else:
    print("invalid acc num")
    print("invalid pin num")
    