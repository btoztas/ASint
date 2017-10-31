import base64

import binascii
from Book import Book
import pickle
import Pyro4
import random

from pprint import pprint

def decode_data(data):
    bin_dump = bytearray((base64.b64decode(data['data'])))
    return pickle.loads(bin_dump)


def main():

    name_server = Pyro4.locateNS()


    while True:
        command = input(">> ").split(" ")

        if command[0].upper() == "NEW":
            servers = name_server.list()
            while True:
                server, uri = random.choice(list(servers.items()))
                if "NameServer" not in server:
                    print("Connected to " + server)
                    db = Pyro4.Proxy(uri)
                    break
            author = input("Author>> ")
            title = input("Title>> ")
            date = input("Date>> ")
            db.insert_book(title, author, date)

        elif command[0].upper() == "SHOW":
            identifier = input("ID>> ")
            identifier_params = identifier.split("@")

            servers = name_server.list()
            for server, uri in servers.items():
                if identifier_params[1] == server:
                    print("Connected to " + server)
                    db_tmp = Pyro4.Proxy(uri)
                    hashed = db_tmp.show_book(identifier)
                    book = decode_data(hashed)
                    print(book)

        elif command[0].upper() == "LIST":
            author = input("Author>> ")

            servers = name_server.list()
            for server, uri in servers.items():
                if "NameServer" not in server:
                    db_tmp = Pyro4.Proxy(uri)
                    hashed = db_tmp.list_books(author)
                    books = decode_data(hashed)
                    print("@"+server)
                    for b in books:
                        print(b)

        elif command[0].upper() == "QUIT":
            break


if __name__ == "__main__":
    main()