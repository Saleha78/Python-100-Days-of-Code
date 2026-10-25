# UNLIMITED POSITIONAL ARGUMENTS

def add(*args):
    total =0
    for n in args:
        total=total+n

    return total

result = add(2,3,4,5)

def calculate(n,**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *=kwargs["multiply"]
calculate(2,add=3, multiply=4)


class Car:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.price = kwargs["price"]

my_car = Car(name="My car", price=100)
print(my_car.name)




