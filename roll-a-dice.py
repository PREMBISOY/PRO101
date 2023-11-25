import random

response = "y"

while response == "y" :
    a = random.randint(1,6)
    print("Do you want to roll the dice :")
    b = input(" 'y' for yes and 'n' for no :")
    if(b == "y"):
        if(a==1):
            print()
            print("  *  ")
            print()
        elif(a==2):
            print("*    ")  
            print("     ")  
            print("    *") 
        elif(a==3):
            print("*    ")  
            print("  *  ")  
            print("    *")
        elif(a==4):
            print("*   *")  
            print("     ")  
            print("*   *")
        elif(a==5):
            print("*   *")  
            print("  *  ")  
            print("*   *")      
        elif(a==6):
            print("*   *")  
            print("*   *")  
            print("*   *")     
    elif(b=="n"):
        response = b