from contacts import contacts


def phone(*args, **kwargs):
    if args or kwargs:
        for arg in args:
            if not len(arg) > 1:
                print("Enter command and name please")
            else:
                for contact in contacts:
                    for key in contact.keys():
                        if arg[0] == key.casefold():
                            phone = contact.get(key)
                            print(phone)
    # return text
