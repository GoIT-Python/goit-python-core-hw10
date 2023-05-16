from contacts import contacts


def show_all(*args, **kwargs):
    for contact in contacts:
        for key, value in contact.items():
            print(key, value)


if __name__ == "__main__":
    print(contacts)
