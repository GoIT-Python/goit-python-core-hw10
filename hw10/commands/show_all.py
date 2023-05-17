# from contacts import contacts
from contacts import book


def show_all(*args, **kwargs):
    book.get_records()
    # for contact in contacts:
    #     for key, value in contact.items():
    #         print(key, value)


if __name__ == "__main__":
    pass
