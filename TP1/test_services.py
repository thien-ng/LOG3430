import sqlite3
import unittest
from unittest.mock import Mock
import os
from models import Contact
from DAOs import ContactDAO
from services import ContactService

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
        pass

    def test_when_contact_is_created_and_DAO_get_by_names_returns_contact_it_should_raise_AlreadyExistedItem(self):
        pass
    
    def test_when_contact_is_changed_updated_should_be_True(self):
        pass
    
    def test_when_contact_is_changed_updated_date_should_be_now(self):
        pass
    
    def test_when_contact_is_changed_and_DAO_update_returns_zero_it_should_raise_UndefinedID(self):
        pass

    def test_when_retrieve_contact_is_called_with_id_and_DAO_get_by_id_should_be_called(self):
        pass
    
    def test_when_retrieve_contact_is_called_with_names_and_DAO_get_by_names_should_be_called(self):
        pass

    def test_when_retrieve_contact_is_called_with_id_and_DAO_returns_None_it_should_raise_UndefinedID(self):
        pass
    
    def test_when_retrieve_contact_is_called_with_names_and_DAO_returns_None_it_should_raise_NotExistedItem(self):
        pass

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_should_be_called(self):
        pass
    
    def test_when_delete_contact_is_called_with_names_and_DAO_delete_by_names_should_be_called(self):
        pass

    def test_when_delete_contact_is_called_with_id_and_DAO_delete_by_id_returns_zero_it_should_raise_UndefinedID(self):
        pass
    
    def test_when_retrieve_contact_is_called_with_names_and_DAO_delete_by_names_returns_zero_it_should_raise_NotExistedItem(self):
        pass
    

    
if __name__ == '__main__':
    unittest.main()
    