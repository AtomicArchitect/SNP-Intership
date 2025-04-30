class EvenNumber:
    def __init__(self, number = None):
        self.__number = number

    def __iter__(self):
        self.__current_step = 0
        return self

    def __next__(self):
        if type(self.__number) is int and self.__current_step == self.__number: raise StopIteration
        self.__current_step += 1
        return 2 * (self.__current_step - 1)

evens = EvenNumber(5)
for num in evens:
    print(num)