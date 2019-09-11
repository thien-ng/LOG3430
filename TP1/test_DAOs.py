import sqlite3
import unittest
import unittest.mock
import os
from DAOs import ContactDAO

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
        pass
    
    def test_get_by_id_after_add_should_return_inserted_value(self):
        pass
    
    def test_get_by_names_after_add_should_return_inserted_value(self):
        pass

    def test_get_by_id_with_undefined_rowid_should_return_None(self):
        pass
    
    def test_get_by_names_with_notexisted_contact_should_return_None(self):
        pass
    
    def test_deactivate_contact_then_get_it_with_id_should_be_not_updated(self):
        pass
    
    def test_deactivate_contact_on_undefined_id_should_return_zero(self):
        pass
    
    def test_after_deleting_contact_by_id_get_it_with_id_should_return_None(self):
        pass

    def test_deleting_undefined_id_should_return_zero(self):
        pass

    def test_after_deleting_contact_by_names_get_item_with_id_should_return_None(self):
        pass

    def test_deleting_not_existed_contact_should_return_zero(self):
        pass

    def test_update_contact_should_set_the_provided_values(self):
        pass

    def test_update_contact_should_return_zero_if_id_does_not_exist(self):
        pass

    def test_list_contacts_with_no_contacts_added_returns_empty_list(self):
        pass
    
    def test_list_contacts_with_one_contact_should_return_list_with_contact(self):
        pass
    
    def test_list_contacts_with_updated_False_and_all_items_updated_should_return_empty_list(self):
        pass
    
    def test_list_contacts_with_updated_True_and_all_items_not_updated_should_return_empty_list(self):
        pass
    
    def test_list_contacts_with_all_not_updated_items_and_updated_False_should_return_all_contacts(self):
        pass

    def test_list_contacts_with_all_updated_items_and_updated_True_should_return_all_contacts(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
