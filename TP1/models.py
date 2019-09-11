from datetime import datetime
class Contact:

    def __init__(self, id, first_name, last_name, phone, mail, updated, updated_date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.mail = mail
        self.updated = bool(updated)
        self.updated_date = updated_date
    
    def __str__(self):
        return '''{self.first_name} {self.last_name} has {self.phone} and {self.mail}.
        This information is updated on {}'''.format(datetime.fromtimestamp(self.updated_date),self=self)
    