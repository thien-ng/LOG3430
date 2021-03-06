import sqlite3
import unittest
import unittest.mock
import os
from models import Contact
from DAOs import ContactDAO
from models import Contact
from datetime import datetime

# To complete...
class TestContactDAO(unittest.TestCase):

    def setUp(self):
        self.db_file = 'temp.db'
        self.contactDAO = ContactDAO(self.db_file)
        self.contactDAO.init_db()

    def tearDown(self):
        os.remove(self.db_file)
    
    def test_when_init_db_is_called_it_should_create_table(self):
        try:
            with sqlite3.connect(self.db_file) as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM contact')
        except sqlite3.OperationalError:
            self.fail("Should not have raised sqlite3.OperationalError")
    
    def test_when_add_is_called_it_should_return_an_autoincremented_id(self):
        contact = Contact(None, "first_name", "last_name", "phone", "mail", "updated", "updated_date")
        self.contactDAO.add(contact)
        self.assertEqual(self.contactDAO.add(contact), 2)
    
    def test_get_by_id_after_add_should_return_inserted_value(self):
        contact = Contact(None, "first_name", "last_name", "phone", "mail", True, "updated_date")
        self.contactDAO.add(contact)

        fetched = self.contactDAO.get_by_id(1)

        self.assertEqual(fetched.id, 1)
        self.assertEqual(fetched.first_name, contact.first_name)
        self.assertEqual(fetched.last_name, contact.last_name)
        self.assertEqual(fetched.phone, contact.phone)
        self.assertEqual(fetched.mail, contact.mail)
        self.assertEqual(fetched.updated, contact.updated)
        self.assertEqual(fetched.updated_date, contact.updated_date)
    
    def test_get_by_names_after_add_should_return_inserted_value(self):
        contact = Contact(None, "first_name", "last_name", "phone", "mail", True, "updated_date")
        self.contactDAO.add(contact)

        fetched = self.contactDAO.get_by_names("first_name", "last_name")

        self.assertEqual(fetched.id, 1)
        self.assertEqual(fetched.first_name, contact.first_name)
        self.assertEqual(fetched.last_name, contact.last_name)
        self.assertEqual(fetched.phone, contact.phone)
        self.assertEqual(fetched.mail, contact.mail)
        self.assertEqual(fetched.updated, contact.updated)
        self.assertEqual(fetched.updated_date, contact.updated_date)

    def test_get_by_id_with_undefined_rowid_should_return_None(self):
        self.assertIsNone(self.contactDAO.get_by_id(999))
    
    def test_get_by_names_with_notexisted_contact_should_return_None(self):
        self.assertIsNone(self.contactDAO.get_by_names("non", "existant"))
    
    def test_deactivate_contact_then_get_it_with_id_should_be_not_updated(self):
        contact = Contact(None, "first_name", "last_name", "phone", "mail", True, "updated_date")
        self.contactDAO.add(contact)
        self.contactDAO.deactivate(1)
        self.assertEqual(self.contactDAO.get_by_id(1).updated, False)
    
    def test_deactivate_contact_on_undefined_id_should_return_zero(self):
        self.assertEqual(self.contactDAO.deactivate(999), 0)
    
    def test_after_deleting_contact_by_id_get_it_with_id_should_return_None(self):
        contact = Contact(None, "first_name", "last_name", "phone", "mail", True, "updated_date")
        self.contactDAO.add(contact)
        self.contactDAO.delete_by_id(1)

        self.assertIsNone(self.contactDAO.get_by_id(1))
    
    def test_deleting_undefined_id_should_return_zero(self):
        self.assertEqual(self.contactDAO.delete_by_id(999), 0)

    def test_after_deleting_contact_by_names_get_item_with_id_should_return_None(self):
        contact = Contact(None, "first_name", "last_name", "phone", "mail", True, "updated_date")
        self.contactDAO.add(contact)
        self.contactDAO.delete_by_names(contact.first_name, contact.last_name)

        self.assertIsNone(self.contactDAO.get_by_id(1))

    def test_deleting_not_existed_contact_should_return_zero(self):
        self.assertEqual(self.contactDAO.delete_by_names("dygfsdug", "sjcbiabc"), 0)

    def test_update_contact_should_set_the_provided_values(self):
        id = None
        updated = False
        contact = Contact( id, "first_name", "last_name", "phone", "mail", updated, "updated_date")
        self.contactDAO.add(contact)
        updated_date = datetime.now().timestamp()
        contact = Contact(1, "Coach", "Carter", "123456789", "123456789@hotmail.com", True, updated_date)
        self.contactDAO.update(contact)

        fetched = self.contactDAO.get_by_id(1)

        self.assertEqual(fetched.id, 1)
        self.assertEqual(fetched.first_name, contact.first_name)
        self.assertEqual(fetched.last_name, contact.last_name)
        self.assertEqual(fetched.phone, contact.phone)
        self.assertEqual(fetched.mail, contact.mail)
        self.assertEqual(fetched.updated, contact.updated)
        self.assertEqual(fetched.updated_date, contact.updated_date)

    def test_update_contact_should_return_zero_if_id_does_not_exist(self):
        id = None
        updated = True
        updated_date = datetime.now().timestamp()
        contact = Contact( id, "first_name", "last_name", "phone", "mail", updated, updated_date)
        self.assertEqual(self.contactDAO.update(contact), 0)

    def test_list_contacts_with_no_contacts_added_returns_empty_list(self):
        self.assertEqual(len(self.contactDAO.list(updated=None)), 0)
    
    def test_list_contacts_with_one_contact_should_return_list_with_contact(self):
        id = None
        updated = True
        updated_date = datetime.now().timestamp()
        contact = Contact( id, "first_name", "last_name", "phone", "mail", updated, updated_date)
        self.contactDAO.add(contact)
        contacts = self.contactDAO.list(updated=None)
        self.assertEqual(len(contacts), 1)
    
    def test_list_contacts_with_updated_False_and_all_items_updated_should_return_empty_list(self):
        id = None
        updated = False
        contact = Contact( id, "first_name", "last_name", "phone", "mail", updated, "updated_date")
        for x in range(7):
            self.contactDAO.add(contact)
        self.assertEqual(len(self.contactDAO.list(updated=True)), 0)

    def test_list_contacts_with_updated_True_and_all_items_not_updated_should_return_empty_list(self):
        id = None
        updated = True
        contact = Contact( id, "first_name", "last_name", "phone", "mail", updated, "updated_date")
        for x in range(10):
            self.contactDAO.add(contact)
        self.assertEqual(len(self.contactDAO.list(updated=False)), 0)
    
    def test_list_contacts_with_all_not_updated_items_and_updated_False_should_return_all_contacts(self):
        id = None
        updated = False
        contact = Contact( id, "first_name", "last_name", "phone", "mail", updated, "updated_date")
        for x in range(10):
            self.contactDAO.add(contact)
        self.assertEqual(len(self.contactDAO.list(updated=False)), 10)

    def test_list_contacts_with_all_updated_items_and_updated_True_should_return_all_contacts(self):
        id = None
        updated = True
        contact = Contact( id, "first_name", "last_name", "phone", "mail", updated, "updated_date")
        for x in range(7):
            self.contactDAO.add(contact)
        self.assertEqual(len(self.contactDAO.list(updated=True)), 7)

if __name__ == '__main__':
    unittest.main()
    
