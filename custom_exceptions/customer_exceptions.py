"""
program: customer_exceptions.py
author: kyle godwin
last date modified: 11 april 2023

Customer class with custom exceptions.
"""


class Customer:

    def __init__(self, cust_id, l_name, f_name, ph_num):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")  # chars for name and major
        if not (name_characters.issuperset(l_name) and name_characters.issuperset(f_name)):  # test for valid name and major
            raise InvalidNameException

        ids = 999  # max id
        if int(cust_id) > ids:  # test for valid id
            raise InvalidCustomerIdException

        if not self.phone_number_format(ph_num):  # test for valid phone number
            raise InvalidPhoneNumberFormatException

        self.customer_id = cust_id
        self.last_name = l_name
        self.first_name = f_name
        self.phone_number = self.phone_number_format(ph_num)

    def phone_number_format(self, a_number):  # function to format phone number
        new_num = a_number.replace(' ', '').replace('-', '').replace('.', '').replace('(', '').replace(')', '')
        if (new_num.isnumeric()) and (len(new_num) == 10):
            return f"{new_num[:3]}-{new_num[3:6]}-{new_num[6:]}"
        else:
            return False

    def __str__(self):  # string function
        return f"{self.customer_id} {self.last_name} {self.first_name} {self.phone_number}"

    def __repr__(self):  # representation function
        return f"{self.customer_id} {self.last_name} {self.first_name} {self.phone_number}"

    def display(self):  # display function
        return f"{self.customer_id} {self.last_name} {self.first_name} {self.phone_number}"


class InvalidCustomerIdException(Exception):
    """number between 1000 - 9999"""
    pass


class InvalidNameException(Exception):
    """alpha characters"""
    pass


class InvalidPhoneNumberFormatException(Exception):
    """123-456-7890 format"""
    pass


if __name__ == "__main__":
    try:
        customer = Customer("1001", "Bobber", "Bob", "123-456-7890")
        print(customer)
        del customer
    except InvalidCustomerIdException:
        print(f"Invalid customer ID entered.")

    try:
        customer = Customer("741", "123", "Bob", "123-456-7890")
        print(customer)
        del customer
    except InvalidNameException:
        print(f"Invalid name entered.")

    try:
        customer = Customer("741", "Bobber", "123", "123-456-7890")
        print(customer)
        del customer
    except InvalidNameException:
        print(f"Invalid name entered.")

    try:
        customer = Customer("741", "Bobber", "Bob", "1-234-567-8910")
        print(customer)
        del customer
    except InvalidPhoneNumberFormatException:
        print(f"Invalid phone number entered.")

    try:
        customer = Customer("741", "Bobber", "Bob", "2345678910")
        print(customer)
        del customer
    except InvalidPhoneNumberFormatException:
        print(f"Invalid phone number entered.")
