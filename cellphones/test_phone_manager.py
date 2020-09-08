import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        testAssignmentMgr = PhoneAssignments()
        test_employee = Employee(1, 'Yanis Varoufakis')
        testAssignmentMgr.add_employee(test_employee)
        self.assertIn(test_employee, testAssignmentMgr.employees)
        

    def test_create_and_add_employee_with_duplicate_id(self):
        # write this test and then remove the self.fail() statement
        # you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        testAssignmentMgr = PhoneAssignments()
        test_employee_1 = Employee(1, 'Isaac Asimov')
        test_employee_2 = Employee(1, 'Arthur C. Clarke')
        
        testAssignmentMgr.add_employee(test_employee_1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(test_employee_2)


    def test_assign_phone_to_employee(self):
        # write this test and remove the self.fail() statement
        # you'll need to fix the assign method in PhoneAssignments
        testAssignmentMgr = PhoneAssignments()
        test_employee = Employee(1, 'Edward Herman')
        test_phone = Phone(1, 'Motorola', 'Razr')
        
        testAssignmentMgr.add_employee(test_employee)
        testAssignmentMgr.add_phone(test_phone)
        
        testAssignmentMgr.assign(1, test_employee)
        self.assertEquals(testAssignmentMgr.phone_info(test_employee), test_phone)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # write this test and remove the self.fail() statement
        # you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.
        testAssignmentMgr = PhoneAssignments()
        test_employee_1 = Employee(1, 'Stephanie Meyer')
        test_employee_2 = Employee(2, 'Morgan Parker')
        test_phone = Phone(1, 'Raffi', 'Banana Phone')
        
        testAssignmentMgr.add_employee(test_employee_1)
        testAssignmentMgr.add_employee(test_employee_2)
        testAssignmentMgr.add_phone(test_phone)
        
        testAssignmentMgr.assign(1, test_employee_1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(1, test_employee_2)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # write this test and remove the self.fail() statement
        # you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.
        testAssignmentMgr = PhoneAssignments()
        test_employee = Employee(1, 'Noam Chomsky')
        test_phone_1 = Phone(1, 'Jitterbug', 'Flip')
        test_phone_2 = Phone(2, 'Campbell\'s', 'Two Cans and a String')
        
        testAssignmentMgr.add_employee(test_employee)
        testAssignmentMgr.add_phone(test_phone_1)
        testAssignmentMgr.add_phone(test_phone_2)
        
        testAssignmentMgr.assign(1, test_employee)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(2, test_employee)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.
        testAssignmentMgr = PhoneAssignments()
        test_employee = Employee(1, 'Howard Zinn')
        test_phone = Phone(1, 'Ericsson', 'DBH 1001')
        
        testAssignmentMgr.add_employee(test_employee)
        testAssignmentMgr.add_phone(test_phone)
        
        testAssignmentMgr.assign(1, test_employee)
        testAssignmentMgr.assign(1, test_employee)


    def test_un_assign_phone(self):
        # write this test and remove the self.fail() statement
        # Assign a phone, unassign the phone, verify the employee_id is None
        testAssignmentMgr = PhoneAssignments()
        test_employee = Employee(1, 'Jane Austen')
        test_phone = Phone(1, 'Carrier', 'Pigeon')
        
        testAssignmentMgr.add_employee(test_employee)
        testAssignmentMgr.add_phone(test_phone)
        
        testAssignmentMgr.assign(1, test_employee)
        testAssignmentMgr.un_assign(1)
        
        self.assertIsNone(test_phone.employee_id)


    def test_get_phone_info_for_employee(self):
        # write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # check that the method returns None if the employee does not have a phone
        # check that the method raises an PhoneError if the employee does not exist
        testAssignmentMgr = PhoneAssignments()
        employee_with_phone = Employee(1, 'Chimamanda Ngozi Adichie')
        employee_without_phone = Employee(2, 'William Goldman')
        nonexistent_employee = Employee(3, 'S. Morgenstern')
        
        test_phone = Phone(1, 'Danger', 'Hiptop')
        
        testAssignmentMgr.add_employee(employee_with_phone)
        testAssignmentMgr.add_employee(employee_without_phone)
        testAssignmentMgr.add_phone(test_phone)
        
        testAssignmentMgr.assign(1, employee_with_phone)
        
        self.assertEquals(testAssignmentMgr.phone_info(employee_with_phone), test_phone)    # test that we can get employee_with_phone's phone
        self.assertIsNone(testAssignmentMgr.phone_info(employee_without_phone))  # test that getting phone info for employee_without_phone returns None
        with self.assertRaises(PhoneError): # test that getting phone info for a nonexistent_employee raises an exception
            testAssignmentMgr.phone_info(nonexistent_employee)


if __name__ == '__main__':
    unittest.main()
