
import unittest
from car_class import Car


class TestCarMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.car = Car()

    def test_car_attributes(self):
        test_attributes = {4, "V8", 160, "red", "X1"}
        car_attributes = {self.car.wheels, self.car.engine,
                          self.car.max_speed, self.car.color, self.car.model}
        self.assertSetEqual(car_attributes, test_attributes)

    def test_setter(self):
        test_attributes = {
            "wheels": 10,
            "engine": "V12",
            "max_speed": 300,
            "color": "black",
            "model": "Z100"
        }

        self.car.wheels = 10
        self.car.engine = "V12"
        self.car.max_speed = 300
        self.car.color = "black"
        self.car.model = "Z100"

        self.assertEqual(self.car.wheels, test_attributes["wheels"])
        self.assertEqual(self.car.engine, test_attributes["engine"])
        self.assertEqual(self.car.max_speed, test_attributes["max_speed"])
        self.assertEqual(self.car.color, test_attributes["color"])
        self.assertEqual(self.car.color, test_attributes["color"])
        self.assertEqual(self.car.model, test_attributes["model"])

    def test_delete_wheels(self):
        del self.car.wheels
        with self.assertRaises(AttributeError):
            self.car.wheels

    def test_print_design_specs(self):
        self.assertEqual(str, type(self.car.print_design_specs()))
