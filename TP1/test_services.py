import sqlite3
import unittest
from unittest.mock import Mock
import os
from models import Contact
from DAOs import ContactDAO
from services import ContactService
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
    
    ## REMOVE DECIMALS OF DATE
    def test_when_contact_is_created_updated_date_should_be_now(self):
        self.contactDAO.get_by_names.return_value = None
        contact = self.contactService.create_contact('Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        self.assertEqual(contact.updated_date, datetime.now().timestamp())

    def test_when_contact_is_created_and_DAO_get_by_names_returns_contact_it_should_raise_AlreadyExistedItem(self):
        self.contactDAO.get_by_names.return_value = "SOMEBODY"
        try:
            self.contactService.create_contact('Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        except Exception as e:
            self.assertEqual(str(e), "Contact with first name <Houssem> and last name <Ben Braiek> already exist")
    
    def test_when_contact_is_changed_updated_should_be_True(self):
        contact = self.contactService.update_contact('id','Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        self.assertTrue(contact.updated)

    ## REMOVE DECIMALS OF DATE
    def test_when_contact_is_changed_updated_date_should_be_now(self):
        contact = self.contactService.update_contact('id','Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        self.assertEqual(contact.updated_date, datetime.now().timestamp())
    
    def test_when_contact_is_changed_and_DAO_update_returns_zero_it_should_raise_UndefinedID(self):
        self.contactDAO.update.return_value = 0
        try:
            self.contactService.update_contact('id','Houssem','Ben Braiek','123-456-7891','houssem.bb@gmail.com')
        except Exception as e:
            self.assertEqual(str(e), "No contact with id <id>")

    def test_when_retrieve_contact_is_called_with_id_and_DAO_get_by_id_should_be_called(self):
        self.contactService.retrieve_contact(id='id')
        self.contactDAO.get_by_id.assert_called_with(id='id')
    
    def test_when_retrieve_contact_is_called_with_names_and_DAO_get_by_names_should_be_called(self):
        self.contactService.retrieve_contact(first_name='firstname', last_name='lastname')
        self.contactDAO.get_by_names.assert_called_with(first_name='firstname', last_name='lastname')

    def test_when_retrieve_contact_is_called_with_id_and_DAO_returns_None_it_should_raise_UndefinedID(self):
        self.contactDAO.get_by_id.return_value = None
        try:
            self.contactService.retrieve_contact(id='id')
        except Exception as e:
            self.assertEqual(str(e), "No contact with id <id>")
    
    def test_when_retrieve_contact_is_called_with_names_and_DAO_returns_None_it_should_raise_NotExistedItem(self):
        self.contactDAO.get_by_names.return_value = None
        try:
            self.contactService.retrieve_contact(first_name='firstname', last_name='lastname')
        except Exception as e:
            self.assertEqual(str(e), "No contact with first name <firstname> and last name <lastname>")

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_should_be_called(self):
        self.contactService.delete_contact(id='id')
        self.contactDAO.delete_by_id.assert_called_with('id')
    
    def test_when_delete_contact_is_called_with_names_and_DAO_delete_by_names_should_be_called(self):
        self.contactService.delete_contact(first_name='firstname', last_name='lastname')
        self.contactDAO.delete_by_names.assert_called_with('firstname', 'lastname')

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_returns_zero_it_should_raise_UndefinedID(self):
        self.contactDAO.delete_by_id.return_value = 0
        try:
            self.contactService.delete_contact(id='id')
        except Exception as e:
            self.assertEqual(str(e), "No contact with id <id>")
    
    def test_when_retrieve_contact_is_called_with_names_and_DAO_delete_by_names_returns_zero_it_should_raise_NotExistedItem(self):
        self.contactDAO.delete_by_names.return_value = 0
        try:
            self.contactService.delete_contact(first_name='firstname', last_name='lastname')
        except Exception as e:
            self.assertEqual(str(e), "No contact with first name <firstname> and last name <lastname>")
    

    
if __name__ == '__main__':
    unittest.main()
    