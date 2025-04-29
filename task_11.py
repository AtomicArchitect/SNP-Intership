class Dessert:

    @staticmethod
    def is_delicious():
        return True

    def __init__(self, name = None, calories = 0):
        self.__name = name
        self.__calories = calories

    def is_healthy(self):
        return True if (type(self.__calories) == int or type(self.__calories) == float) and self.__calories < 200 else False

    def set_name(self, name):
        if name is not None and type(name) == str: self.__name = name

    def set_calories(self, calories):
        if calories is not None and (type(calories) == int or type(calories) == float) and calories > 0: self.__calories = calories

    def get_name(self):
        return self.__name

    def get_calories(self):
        return self.__calories

    def __str__(self):
        return "Dessert: {}, Calories: {}".format(self.__name, self.__calories)

icecream = Dessert("Icecream")
assert icecream.is_delicious() == True
assert icecream.is_healthy() == True
assert icecream.get_calories() == 0
assert icecream.get_name() == "Icecream"
icecream.set_calories(201)
icecream.set_name(200)
assert icecream.get_calories() == 201
icecream.set_calories(-100)
assert icecream.get_calories() == 201
icecream.set_calories(None)
assert icecream.get_calories() == 201
icecream.set_calories(205.512)
assert icecream.get_calories() == 205.512
assert icecream.get_name() == "Icecream"
assert icecream.is_healthy() == False
print(icecream)