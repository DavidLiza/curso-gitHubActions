import os 

def mainFunction ():
    username = os.getenv("USERNAME")
    print ("Hola {} Desde un Github action ".format(username))

if __name__ == "main":
    print ("Pos Hola desde aqui antes de que se dañe")
    mainFunction()