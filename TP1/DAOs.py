import sqlite3
from models import Contact

class ContactDAO: 

    def __init__(self, db_file):
        self.db_file = db_file

    def init_db(self):
        '''Initialize the database by creating the contact table.'''
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS
                                contact
                            (id INTEGER PRIMARY KEY,
                            first_name text,
                            last_name text,
                            phone text,
                            mail text,
                            updated bool,
                            updated_date double
                                )
                            ''')


    def add(self, new_contact):
        '''Add new contact and return the ID that is generated. The
           id may later be used to reference the item.
        '''
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                            INSERT INTO
                                contact
                            (first_name,
                            last_name,
                            phone,
                            mail,
                            updated,
                            updated_date)
                            VALUES
                            (?,?,?,?,?,?)
                            ''', (new_contact.first_name, new_contact.last_name, new_contact.phone, new_contact.mail, new_contact.updated, new_contact.updated_date))
            connection.commit()
            return cursor.lastrowid

    def get_by_id(self, id):
        '''Return contact that has the provided id. If no item is found
           with that id, return None.
        '''
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                        SELECT
                            id,
                            first_name,
                            last_name,
                            phone,
                            mail,
                            updated,
                            updated_date
                        FROM
                            contact
                        WHERE
                            id = ?
                        ''', (id,))
            row = cursor.fetchone()
            if row is not None:
                contact = Contact(*row)
                return contact
            return row

    def get_by_names(self, first_name, last_name):
        '''Return contact that has the provided names. If no contact is found
           with that id, return None.
        '''
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                        SELECT
                            id,
                            first_name,
                            last_name,
                            phone,
                            mail,
                            updated,
                            updated_date
                        FROM
                            contact
                        WHERE
                            first_name = ? AND last_name = ?
                        ''', (first_name,last_name))
            row = cursor.fetchone()
            if row is not None:
                contact = Contact(*row)
                return contact
            return row

    def deactivate(self, id):
        '''
        Mark contact not updated that matches the provided id.
        '''
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                        UPDATE
                            contact
                        SET
                            updated = 0
                        WHERE
                            id = ?
                        ''', (id,))
            connection.commit()
            return cursor.rowcount

    def update(self, contact):
        '''
        Update the contact with the provided values.
        '''
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                        UPDATE
                            contact
                        SET
                            first_name = ? ,
                            last_name = ? ,
                            phone = ? ,
                            mail = ? ,
                            updated = ? ,
                            updated_date = ?
                        WHERE
                            id = ?
                        ''', (contact.first_name, contact.last_name, contact.phone, contact.mail, contact.updated, contact.updated_date, contact.id))
            connection.commit()
            return cursor.rowcount


    def delete_by_id(self, id):
        '''
        Delete an item with the provided id. 
        '''
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                        DELETE FROM
                            contact
                        WHERE
                            id = ?
                        ''', (id,))
            connection.commit()
            return cursor.rowcount

    def delete_by_names(self, first_name, last_name):
        '''
        Delete an item with the provided names.
        '''
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute('''
                        DELETE FROM
                            contact
                        WHERE
                            first_name = ? AND last_name = ?
                        ''', (first_name, last_name))
        connection.close()            
        return cursor.rowcount

    def list(self, updated=None):
        '''
        List contacts. If updated is None, return all contacts. If updated
        is True, return updated contacts. If updated is False, return only
        not updated contacts.
        '''
        if updated is None:
            query = ('''
                        SELECT
                            id,
                            first_name,
                            last_name,
                            phone,
                            mail,
                            updated,
                            updated_date
                        FROM
                            contact
                        ''',)
        else:
            query = ('''
                        SELECT
                            id,
                            first_name,
                            last_name,
                            phone,
                            mail,
                            updated,
                            updated_date
                        FROM
                            contact
                        WHERE
                            updated = ?
                        ''', (updated,))
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(*query)
            contacts = []
            for row in cursor.fetchall():
                contacts.append(Contact(*row))
            return contacts
        