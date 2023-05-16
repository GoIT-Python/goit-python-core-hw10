from collections import UserDict


class AddressBook(UserDict):
    def search_record(self, key):
        return key in self.data.keys()

    def add_record(self, key, value):
        self[key] = value


address = AddressBook()
address.add_record('John', 2345678567)
print(address.search_record('John'))


class Record:
    def __int__(self, name):
        self.name = name
