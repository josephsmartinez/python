import unittest
import sys
import logging


class TestStringMethods(unittest.TestCase):
    log = logging.getLogger("Unittest")

    def test_upper(self):
        self.assertTrue("FOO".isupper())

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError) as error:
            self.log.debug(error)
            s.split(2)


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    log = logging.getLogger("Unittest")
    unittest.main()
