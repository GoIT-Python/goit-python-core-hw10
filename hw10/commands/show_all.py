from contacts import book


def show_all(*args, **kwargs):
    print(book.get_records())


if __name__ == "__main__":
    pass
