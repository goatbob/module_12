"""
program: test_custom_exceptions.py
author: kyle godwin
last date modified: 11 april 2023

unittest for customer_exceptions.py
"""
import unittest
from custom_exceptions import *
from custom_exceptions import Customer as Cust


class CustomerTest(unittest.TestCase):

    def setUp(self):  # set up customer class
        self.customer = Cust("795", "Bobber", "Bob", "123-456-7890")

    def tearDown(self):  # tear down customer class
        del self.customer

    def test_object_created_required_attributes(self):  # test required attributes for class
        self.assertEqual(self.customer.customer_id, "795")
        self.assertEqual(self.customer.last_name, "Bobber")
        self.assertEqual(self.customer.first_name, "Bob")
        self.assertEqual(self.customer.phone_number, "123-456-7890")

    def test_object_created_all_attributes(self):  # test all attributes for class
        customer = Cust("795", "Bobber", "Bob", "123-456-7890")
        assert customer.last_name == "Bobber"
        assert customer.first_name == "Bob"
        assert customer.customer_id == "795"
        assert customer.phone_number == "123-456-7890"

    def test_student_str(self):  # test string output of class
        self.assertEqual(str(self.customer), "795 Bobber Bob 123-456-7890")

    def test_student_repr(self):  # test representation output of class
        self.assertEqual(repr(self.customer), "795 Bobber Bob 123-456-7890")

    def test_display(self):  # test display function
        self.assertEqual(self.customer.display(), "795 Bobber Bob 123-456-7890")

    def test_object_not_created_error_cust_id(self):  # test customer ID validation
        with self.assertRaises(InvalidCustomerIdException):
            cust = Cust("1001", "Bobber", "Bob", "123-456-7890")

    def test_object_not_created_error_first_name(self):  # test first name validation
        with self.assertRaises(InvalidNameException):
            cust = Cust("900", "Bobber", "123", "123-456-7890")

    def test_object_not_created_error_last_name(self):  # test last name validation
        with self.assertRaises(InvalidNameException):
            cust = Cust("900", "123", "Bob", "123-456-7890")

    def test_object_not_created_error_phone(self):  # test phone number validation
        with self.assertRaises(InvalidPhoneNumberFormatException):
            cust = Cust("900", "Bobber", "Bob", "123-456-78910")


if __name__ == '__main__':
    unittest.main()

