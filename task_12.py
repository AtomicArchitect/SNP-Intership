from task_11 import Dessert

class JellyBean(Dessert):

    def is_delicious(self):
        if self.__flavor is not None and type(self.__flavor) is str and self.__flavor == "black licorice": return False
        return super().is_delicious()

    def __init__(self, name = "JellyBean", calories = 0, flavor = None):
        super().__init__(name, calories)
        self.__flavor = flavor

    def set_flavor(self, flavor):
        self.__flavor = flavor

    def get_flavor(self):
        return self.__flavor

    def __str__(self):
        return "Dessert: {}, Calories: {}, Flavor: {}".format(self.get_name(), self.get_calories(), self.__flavor)

jellyBean = JellyBean(flavor="black licorice")
assert jellyBean.is_delicious() == False
assert jellyBean.get_flavor() == "black licorice"
jellyBean.set_flavor("white licorice")
assert jellyBean.get_flavor() == "white licorice"
assert jellyBean.is_delicious() == True
print(jellyBean)