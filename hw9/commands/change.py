from contacts import contacts


def change(*args, **kwargs):
    if args or kwargs:
        for arg in args:
            if not len(arg) > 1:
                print("Enter command again with name and phone please")
            else:
                for contact in contacts:
                    for key in contact.keys():
                        if arg[0] == key.casefold():
                            contact.update({key: " ".join(arg[1:])})

    # return text
