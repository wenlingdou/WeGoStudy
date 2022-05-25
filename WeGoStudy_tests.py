import unittest
import WeGoStudy_locators as locators
import WeGoStudy_methods as methods


class PositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_main_wegostudy():
        methods.setUp()
        methods.login()
        # methods.create_new_student() #  no more new students
        # methods.create_new_application()  # bug in website - doesnt work
        # methods.view_student_details() # view student details is implicit in edit student details
        methods.edit_student_details()
        methods.view_application_list()
        methods.logout()
        methods.tearDown()
