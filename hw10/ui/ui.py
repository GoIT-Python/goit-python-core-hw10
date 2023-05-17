from collections import UserDict


class AddressBook(UserDict):

    def get_records(self):
        for key, value in self.data.items():
            print(key, value)

    def search_record(self, key):
        return self.data.get(key)
        # return key in self.data.keys()

    def add_record(self, record):
        self.data[record.name] = record.phone
    # self.data.update({record.name: record.phone})


class Record:

    def __init__(self, name, phone=None):
        if phone is None:
            phone = []
        self.name = name
        self.phone = phone

    def add_phone(self, item):
        if item not in self.phone:
            self.phone.append(item)
        else:
            print(f'Phone number {item} already in list')

    def remove_phone(self, item):
        if item in self.phone:
            self.phone.remove(item)
        else:
            print(f'Phone number {item} is not in list')

    def edit_phone(self, item, new_item):
        item_idx = self.phone.index(item)
        self.phone[item_idx] = new_item


class Field:
    def __init__(self):
        pass


class Name(Field):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name


class Phone(Field):
    def __init__(self, phone=''):
        super().__init__()
        self.phone = phone

    def __str__(self):
        return self.phone

# name1 = Name('Boris')
# name2 = Name('Doris')
# name3 = Name('Nina')
# phone1 = '234567890-'
# phone2 = '098765432'
# phone3 = '87654323456'
# phone4 = '23456789'
# record1 = Record(name1)
# record2 = Record(name2)
# record3 = Record(name3)
# record1.add_phone(phone1)
# record1.add_phone(phone2)
# record2.add_phone(phone3)
# record3.add_phone(phone4)

# address1 = AddressBook()
# address1.add_record(record1)
# address1.add_record(record2)
# address1.get_records()
# print(address1.search_record(name3))

# address2 = AddressBook()
# address2.add_record(record3)
# print(address2.search_record(name1))
# address2.get_records()
