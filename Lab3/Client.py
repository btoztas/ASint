import base64

import binascii
from Book import Book
import pickle
import Pyro4


def decode_data(data):
    bin_dump = bytearray((base64.b64decode(data['data'])))
    return pickle.loads(bin_dump)


def main():

    uri = input("URI: ")
    db = Pyro4.Proxy(uri)

    while True:
        command = input(">> ").split(" ")

        if command[0].upper() == "NEW":
            author = input("Author>> ")
            title = input("Title>> ")
            date = input("Date>> ")
            db.insert_book(title, author, date)

        elif command[0].upper() == "SHOW":
            identifier = int(input("ID>> "))
            hashed = db.show_book(identifier)
            book = decode_data(hashed)
            print(book)

        elif command[0].upper() == "LIST":
            author = input("Author>> ")
            hashed = db.list_books(author)
            books = decode_data(hashed)
            for b in books:
                print(b)

        elif command[0].upper() == "QUIT":
            break


if __name__ == "__main__":
    main()