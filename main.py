import rent
import returned
import datetime as dt

def Press1(W):
    a="\n ++++++++++++++++++++++++++++++++++++++++++\n\t Let's rent a costume.\n ++++++++++++++++++++++++++++++++++++++++++\n"
    return a

def Press2(W):
    b="\n ++++++++++++++++++++++++++++++++++++++++++\n\t Let's return a costume. \n ++++++++++++++++++++++++++++++++++++++++++\n"
    return b

def Press3(W):
    c=" \n++++++++++++++++++++++++++++++++++++++++++++++++++++\n\t Thank you for using our application.\n++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    return c

continueloop=True
print("--------++++++++++++++++++++++++++++----------\n\tWelcome to Custoume Rental Shop\n--------++++++++++++++++++++++++++++----------\n\t ")
while continueloop==True:
    print("\nEnter (1)|| to rent the costume.\nEnter(2) || to return the costume.\nEnter(3) || to exit the application.")
    try:
        W=int(input("\nEnter a option: "))
        
        if W==1:
            print(Press1(W))
            rent.print_list()
            rent.rent_multiple_costume()
            
        elif W==2:
            print(Press2(W))
            returned.prints_list()
            returned.returned_multiple_costume()
            
        elif W==3:
            print(Press3(W))
            break;
        
        else:
            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n \t Invalid Input!!!! \n Please input valid number as instructed above.\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    except ValueError :
        print("\nPlease enter number value only.")    
