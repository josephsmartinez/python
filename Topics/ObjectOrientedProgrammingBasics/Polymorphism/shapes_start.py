import math

class Rectangle:
  def __int__(self, color, filled, width, length):
      self.__color = color
      self.__filled = filled
      self.__width = width
      self.__length = length

  def get_color(self):
    return self.__color

  def set_color(self, color):
    self.__color = color
    return self.__color

  def is_filled(self):
    return self.__filled

  def set_filled(self, filled):
    return self.__filled

  def are(self, parameter_list):
    return self.__width * self.__base__       
 
class Circle():
    def __int__(self, color, filled, radius):
        self.__color = color
        self.__filled = filled
        self.__radius = radius      
 
    def get_color(self):
        return self.__color
 
    def set_color(self, color):
      self.__color = color
      return self.__color

    def is_filled(self):
        return self.__filled
 
    def set_filled(self, filled):
        return self.__filled
 
    def get_area(self):
        return math.pi * self.__radius ** 2

if __name__ == "__main__":
    circle = Circle("red",)
