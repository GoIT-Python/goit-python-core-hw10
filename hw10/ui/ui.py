from collections import UserDict


class AddressBook(UserDict):
    # def __init__(self, __dict: None = ...):
    #     super().__init__(__dict)
    #     self.record = None

    # def __init__(self):
    #     self.record = record

    def search_record(self, key):
        # print(self.data.items())
        print(self.data.keys())
        print(self.data.values())
        return key in self.data.keys()

    def add_record(self, record):
        #     self.data[record.name] = record.phone
        self.data.update({record.name: record.phone})


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

    # def __str__(self):
    #     return self.name, self.phone


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


name1 = Name('Boris')
name2 = Name('Doris')
phone1 = '234567890-'
phone2 = '098765432'
phone3 = '87654323456'
record1 = Record(name1)
record2 = Record(name2)
print(record1.name)
print(record2.name)
record1.add_phone(phone1)
record1.add_phone(phone2)
print(record1.phone)
record2.add_phone(phone3)
print(record2.phone)
address = AddressBook()
address.add_record(record1)
address.add_record(record2)
print(address.search_record(name2))
