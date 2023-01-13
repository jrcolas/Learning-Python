# # Unlimited Positional Arguments
# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     print(result)
#
#
# add(2, 3, 4, 5)
#
#
# # Unlimited Keyword Arguments
# def calculate(n, **kwargs):
#     print(kwargs) # returns keywords with values as a dictionary
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")  # if defined as kw.get() instead of kw[], returns None if no value is given


my_car = Car(make="Nissan")
print(my_car.model)
