import os 

def mainFunction ():
    username = os.getenv("USERNAME")
    print ("Hola {} Desde un Github action".format(username))

if __name__ == "__main__":
    mainFunction()