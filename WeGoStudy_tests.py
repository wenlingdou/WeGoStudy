import unittest
import WeGoStudy_locators as locators
import WeGoStudy_methods as methods

class PositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.login()
        methods.tearDown()
        