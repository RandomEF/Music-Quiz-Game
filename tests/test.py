import unittest
from unittest.mock import patch
from MusicQuizGame import *
class Test(unittest.TestCase):
    def testFirstLetter(self):
        result = FirstLetter("India")
        self.assertEqual(result, "I")

if __name__ == "main":
    unittest.main()