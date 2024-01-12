import os 

def mainFunction ():
    username = os.getenv("USERNAME")
    favLen  = os.getenv("LANGUAGE")
    print ("Hola {} Desde un Github action".format(username))
    print ("Tu lenguaje Favorito es : {}".format(favLen))

if __name__ == "__main__":
    mainFunction()
