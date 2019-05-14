import unittest
import examples

class TestExamples(unittest.TestCase):
    def test_add(self):
        result = examples.addition(2, 3)
        self.assertEqual(result, 5)

    def test_sub(self):
        result = examples.subtraction(2, 3)
        self.assertEqual(result, -1)

    def test_mult(self):
        result = examples.multiplication(2, 3)
        self.assertEqual(result, 6)

    def test_div(self):
        self.assertRaises(ValueError, examples.division(10, 0))
        self.assertEqual(examples.division(9, 3), 3)

    def test_Euclid(self):
        self.assertEqual(
            examples.EuclideanDistance([3,0], [0,4]), 5
        )

    def test_dict(self):
        self.assertIn(12, {"key1":12, "key2": 14})
        self.assertIn("key1", {"key1": 12, "key2": 14})
        self.assertIn({"key1": 12}, {"key1": 12, "key2": 14})

    def test_isPrime(self):
        self.assertTrue(examples.is_prime(2))
        self.assertTrue(examples.is_prime(3))
        self.assertTrue(examples.is_prime(5))
        self.assertTrue(examples.is_prime(17))
        self.assertTrue(examples.is_prime(12))
        self.assertTrue(examples.is_prime(14))


    def test_factorial(self):
        self.assertEqual(examples.factorial(0), 1)
        self.assertEqual(examples.factorial(5), 120)


    def test_elf(self):
        self.assertIsInstance(examples.Elf('first_level'), examples.Elf)
        self.assertIsInstance(examples.Elf('second_level',{
           "str": 12, "dex": 13, "con": 11,
           "int": 17, "wis": 15, "cha": 14
        }))
        self.assertIsInstance(examples.Elf('third_level', {
            "str": 12, "dex": 13, "con": 11,
            "int": 17, "wis": 15, "cha": 14
        }, 19), examples.Elf)

if __name__ == '__main__':
    unittest.main()
