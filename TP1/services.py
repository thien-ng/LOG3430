from DAOs import ContactDAO
from models import Contact 
from datetime import datetime

class UndefinedID(Exception):
   """Raised when the id value is not defined"""
   pass

class NotExistedItem(Exception):
   """Raised when there is no item with the target values"""
   pass

class AlreadyExistedItem(Exception):
   """Raised when an item with the target values is already existed"""
   pass

class InvalidPhoneNumber(Exception):
   """Raised when the phone number is not an american phone number"""
   pass

class InvalidMailAddress(Exception):
   """Raised when the mail is not valid"""
   pass

class ContactService:
    
    def __init__(self, contactDAO):
        self.contactDAO = contactDAO

    # No need to test since we have already tested the contactDAO.list
    def retrieve_active_contacts(self):
        '''
        List updated contacts.
        '''
        return self.contactDAO.list(updated=True)
        
    # No need to test since we have already tested the contactDAO.list
    def retrieve_non_active_contacts(self):
        '''
        List not updated contacts.
        '''
        return self.contactDAO.list(updated=False)
    
    def retrieve_contact(self, id=None, first_name='', last_name=''):
        '''
        Return contact that has the provided id. If no contact is found
        with that id, raise UndefinedID.  If no contact is found
        with given names, raise NotExistedItem.
        '''
        if id is not None:
            contact = self.contactDAO.get_by_id(id=id) 
            if contact is None:
                raise UndefinedID("No contact with id <{}>".format(id))
        else:
            contact = self.contactDAO.get_by_names(first_name=first_name, last_name=last_name)
            if contact is None:
                raise NotExistedItem("No contact with first name <{}> and last name <{}>".format(first_name, last_name)) 
        return contact
    
    def create_contact(self, first_name, last_name, phone, mail):
        '''
        Create a new contact that has the provided information. If an existing contact is found
        with the same values, raise AlreadyExistedItem. 
        '''
        id = None
        if not self.check_phone(phone):
            raise InvalidPhoneNumber('Invalid Phone <{}>'.format(phone))
        if not self.check_mail(mail):
            raise InvalidMailAddress('Invalid Mail <{}>'.format(mail))
        updated = True
        updated_date = datetime.now().timestamp()
        contact = Contact(id, first_name, last_name, phone, mail, updated, updated_date)
        existed_contact = self.contactDAO.get_by_names(first_name, last_name)
        if existed_contact is not None:
            raise AlreadyExistedItem("Contact with first name <{}> and last name <{}> already exist".format(first_name, last_name)) 
        contact.id = self.contactDAO.add(contact)
        return contact

    def update_contact(self, id, first_name, last_name, phone, mail):
        '''
        Update contact with the provided values. If no contact is found
        with that id, raise UndefinedID.
        '''
        updated = True
        if not self.check_phone(phone):
            raise InvalidPhoneNumber('Invalid Phone <{}>'.format(phone))
        if not self.check_mail(mail):
            raise InvalidMailAddress('Invalid Mail <{}>'.format(mail))
        updated_date = datetime.now().timestamp()
        contact = Contact(id, first_name, last_name, phone, mail, updated, updated_date)
        if self.contactDAO.update(contact) == 0:
            raise UndefinedID("No contact with id <{}>".format(id))
        return contact

    def delete_contact(self, id=None, first_name='', last_name=''):
        '''
        Delete contact that has whether the provided id or names. If no contact is found
        with that id, raise UndefinedID.  If no contact is found
        with given names, raise NotExistedItem.
        '''
        if id is not None:
            if self.contactDAO.delete_by_id(id) == 0:
                raise UndefinedID("No contact with id <{}>".format(id)) 
        else:
            if self.contactDAO.delete_by_names(first_name, last_name) == 0:
                raise NotExistedItem("No contact with first name <{}> and last name <{}>".format(first_name, last_name))
    # To propose unit tests for this method
    def verify_contacts_status(self):
        '''
        Return contact that has the provided id. If no contact is found
        with that id, raise UndefinedID.  If no contact is found
        with given names, raise NotExistedItem.
        '''
        contacts = self.retrieve_active_contacts()
        for contact in contacts:
            delta = datetime.now() - datetime.fromtimestamp(contact.updated_date)
            if delta.days > 1095:
                self.contactDAO.deactivate(contact.id)
    # To complete and to propose unit test for it
    def check_phone(self, phone):
        '''
        Return True if the phone number is a valid american phone number otherwise, it returns False.
        '''
        return True
    # To complete and to propose unit test for it
    def check_mail(self, mail):
        '''
        Return True if the mail address is valid otherwise, it returns False.
        '''
        return True