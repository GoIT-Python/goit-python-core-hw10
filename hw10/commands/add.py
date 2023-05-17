from contacts import contacts

book1 = ui.AddressBook()


def add(*args, **kwargs):
    if args or kwargs:
        for arg in args:
            if not len(arg) > 1:
                print("Enter command again with name and phone please")
            else:
                print('book1', book1)
                contacts.append({arg[0].capitalize(): " ".join(arg[1:])})


if __name__ == "__main__":
    add()
