
import sqlite3
import unittest
from unittest.mock import Mock
import os
from models import Contact
from DAOs import ContactDAO
from services import *
from datetime import datetime

# To complete...
class TestContactService(unittest.TestCase):

    def setUp(self):
        self.contactDAO = Mock()
        self.contactService = ContactService(self.contactDAO)
    
    def test_when_contact_is_created_updated_should_be_True(self):
        self.contactDAO.add.return_value = 1
        self.contactDAO.get_by_names.return_value = None
        contact = self.contactService.create_contact('Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        self.assertTrue(contact.updated)
    
    def test_when_contact_is_created_updated_date_should_be_now(self):
        self.contactDAO.get_by_names.return_value = None
        contact = self.contactService.create_contact('Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        self.assertEqual(int(contact.updated_date), int(datetime.now().timestamp()))

    def test_when_contact_is_created_and_DAO_get_by_names_returns_contact_it_should_raise_AlreadyExistedItem(self):
        contact = self.contactService.update_contact('id','Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        self.contactDAO.get_by_names.return_value = contact
        self.assertRaises(AlreadyExistedItem, self.contactService.create_contact, 'Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')

    def test_when_contact_is_changed_updated_should_be_True(self):
        contact = self.contactService.update_contact('id','Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        self.assertTrue(contact.updated)

    def test_when_contact_is_changed_updated_date_should_be_now(self):
        contact = self.contactService.update_contact('id','Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        self.assertEqual(int(contact.updated_date), int(datetime.now().timestamp()))
    
    def test_when_contact_is_changed_and_DAO_update_returns_zero_it_should_raise_UndefinedID(self):
        self.contactDAO.update.return_value = 0
        self.assertRaises(UndefinedID, self.contactService.update_contact, 'id','Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')

    def test_when_retrieve_contact_is_called_with_id_and_DAO_get_by_id_should_be_called(self):
        self.contactService.retrieve_contact(id='id')
        self.contactDAO.get_by_id.assert_called_with(id='id')
    
    def test_when_retrieve_contact_is_called_with_names_and_DAO_get_by_names_should_be_called(self):
        self.contactService.retrieve_contact(first_name='firstname', last_name='lastname')
        self.contactDAO.get_by_names.assert_called_with(first_name='firstname', last_name='lastname')

    def test_when_retrieve_contact_is_called_with_id_and_DAO_returns_None_it_should_raise_UndefinedID(self):
        self.contactDAO.get_by_id.return_value = None
        self.assertRaises(UndefinedID, self.contactService.retrieve_contact, id='id')
    
    def test_when_retrieve_contact_is_called_with_names_and_DAO_returns_None_it_should_raise_NotExistedItem(self):
        self.contactDAO.get_by_names.return_value = None
        self.assertRaises(NotExistedItem, self.contactService.retrieve_contact, first_name='firstname', last_name='lastname')

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_should_be_called(self):
        self.contactService.delete_contact(id='id')
        self.contactDAO.delete_by_id.assert_called_with('id')
    
    def test_when_delete_contact_is_called_with_names_and_DAO_delete_by_names_should_be_called(self):
        self.contactService.delete_contact(first_name='firstname', last_name='lastname')
        self.contactDAO.delete_by_names.assert_called_with('firstname', 'lastname')

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_returns_zero_it_should_raise_UndefinedID(self):
        self.contactDAO.delete_by_id.return_value = 0
        self.assertRaises(UndefinedID, self.contactService.delete_contact, id='id')
    
    def test_when_retrieve_contact_is_called_with_names_and_DAO_delete_by_names_returns_zero_it_should_raise_NotExistedItem(self):
        self.contactDAO.delete_by_names.return_value = 0
        self.assertRaises(NotExistedItem, self.contactService.delete_contact, first_name='firstname', last_name='lastname')

    # Test pour verify_contacts_status
    def test_function_verify_contacts_status_when_retrieve_active_contacts_returns_nothing(self):
        self.contactDAO.list.return_value = []
        self.contactService.verify_contacts_status()
        self.contactDAO.deactivate.assert_not_called()
    
    def test_function_verify_contacts_status_when_delta_days_is_higher_than_1095(self):
        self.contactDAO.get_by_names.return_value = None
        contact = Contact('5','Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com','updated',1)
        self.contactDAO.list.return_value = [contact]
        notification = self.contactService.verify_contacts_status()
        self.contactDAO.deactivate.assert_called_with(contact.id)
        # test return value to notify user (added feature in services.py)
        self.assertEqual(notification, "User with ID 5 has been deactivated.")

    def test_function_verify_contacts_status_when_delta_days_is_lower_than_1095(self):
        self.contactDAO.get_by_names.return_value = None
        contact = Contact('id','Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com','updated',datetime.now().timestamp())
        self.contactDAO.list.return_value = [contact]
        self.contactService.verify_contacts_status()
        self.contactDAO.deactivate.assert_not_called()

    # Test pour Check_phone et check_mail
    def test_function_check_phone_should_return_true_only_when_american_number_is_passed(self):
        self.assertTrue(self.contactService.check_phone("555-555-5555"))

    def test_function_check_phone_should_return_false_when_number_is_not_american(self):
        self.assertFalse(self.contactService.check_phone("3565 346345"))

    def test_function_check_phone_should_return_false_when_number_is_empty(self):
        self.assertFalse(self.contactService.check_phone(""))
    
    def test_function_check_mail_should_return_true_if_mail_is_valid(self):
        self.assertTrue(self.contactService.check_mail("sdfgdfsgdf@gmail.com"))

    def test_function_check_mail_should_return_false_if_mail_is_not_valid(self):
        self.assertFalse(self.contactService.check_mail("thisisnotanemail@@agmail.comm"))
        
    def test_function_check_mail_should_return_false_if_mail_string_is_empty(self):
        self.assertFalse(self.contactService.check_mail(""))

    def test_function_create_contact_should_raise_InvalidPhoneNumber_exception_if_phone_not_valid(self):
        self.assertRaises(InvalidPhoneNumber, self.contactService.create_contact, 'Jeremy', 'Boulet', '5555555', 'email@gmail.com')

    def test_function_create_contact_should_raise_InvalidMailAddress_exception_if_phone_not_valid(self):
        self.assertRaises(InvalidMailAddress, self.contactService.create_contact, 'Jeremy', 'Boulet', '122-334-5566', 'emailgmail.com')


    
if __name__ == '__main__':
    unittest.main()
    