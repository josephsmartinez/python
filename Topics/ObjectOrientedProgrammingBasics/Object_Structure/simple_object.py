from abc import ABC, abstractmethod


class Vehicle(ABC):
    pass
    #     @abstractmethod
    #     def current_speed(self):
    #         pass

    #     @classmethod
    #     @abstractmethod
    #     def current_speed(self):
    #         pass

    #     @staticmethod
    #     @abstractmethod
    #     def current_speed(self):
    #         pass

    #     @property
    #     @abstractmethod
    #     def current_speed(self):
    #         pass

    #     @current_speed.setter
    #     @abstractmethod
    #     def current_speed(self):
    #         pass

    #     @abstractmethod
    #     def current_speed(self):
    #         pass

    #     @abstractmethod
    #     def _get_x(self):
    #         pass

    #     @abstractmethod
    #     def _set_x(self, val):
    #         pass


class Tire(object):
    pass


class Engine(object):
    pass


class Car(Vehicle):
    def __init__(self):
        # The underscore prefix is meant as a hint to another programmer that a variable or method starting with a single underscore is intended for internal use.
        self._value = 100
        # Double underscore will mangle the attribute names of a class to avoid conflicts of attribute names between classes.
        self.__other_value = 0
        # TODO: Should be a list of Tire Objects
        self.tires = ['FrontRightTire', 'FrontLeftTire',
                      'BackRightTire', 'BackLeftTire']
        self.engine = Engine()

    # getting the values
    @property
    def value(self):
        print('Getting value')
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value
