################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
class MagicalOven:
    def __init__(self):#constructor
        self.ingredients = [] # lista de ingredientes
        self.temperature = 0

    def add(self, item): #agrega ingredientes
        self.ingredients.append(item)

    def freeze(self): #congela
        self.temperature = -10

    def boil(self): #hierve los ingredientes
        self.temperature = 110

    def wait(self): #Método de espera
        pass

    def get_output(self): #Obtiene la salida del horno en función de los ingredientes y la temperatura.
        if "lead" in self.ingredients and "mercury" in self.ingredients:
            return "gold"
        elif "water" in self.ingredients and "air" in self.ingredients:
            return "snow"
        elif "cheese" in self.ingredients and "dough" in self.ingredients and "tomato" in self.ingredients:
            return "pizza"
        else:
            return "unknown"

def make_oven(): #Crea y devuelve una nueva instancia del horno mágico.
    return MagicalOven()

def alchemy_combine(oven, ingredients, temperature): #Combina ingredientes en el horno a una temperatura específica y devuelve la salida.
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()







