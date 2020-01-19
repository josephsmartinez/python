# Class Car is an example for the unittest within this directory /Unittest


class Car(object):
    """Simple Car class that defines a Car object.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        wheels (int): number of wheels the car has
        engine (str): engine type
        max_speed (float): maximum speed of the car
        color (str) : color of the car
        model (str): model type for the car
    """

    def __init__(self):

        # double underscore -prefixed to a variable makes it private. It gives a strong suggestion not to touch it from outside the class. Any attempt to do so will result in an AttributeError
        self.__wheels = 4
        self.__engine = "V8"
        self.__max_speed = 160
        self.__color = "red"
        self.__model = "X1"

        self.__designer = "Mark Harriberg"
        self.__wheel_type = "GoodYear"
        self.__gas_type = "High Octain"

    def print_design_specs(self):
        return "{}\n{}\n{}".format(
            self.__designer,
            self.__wheel_type,
            self.__gas_type)

    # The @property decorator turns the voltage() method into a “getter” for a read-only attribute with the same name
    @property
    def wheels(self):
        return self.__wheels

    @wheels.setter
    def wheels(self, wheels: int):
        self.__wheels = wheels

    # deleter will remove the attribute from the local namespace.
    @wheels.deleter
    def wheels(self):
        del self.__wheels

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine: str):
        self.__engine = engine

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, max_speed: str):
        self.__max_speed = max_speed

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model
