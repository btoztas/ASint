import socket
import Pyro4
from Book import Book
from BookDatabase import BookDatabase


def main():

    remote_db = Pyro4.expose(BookDatabase)
    database = remote_db(input("DB Name: "))
    daemon = Pyro4.core.Daemon('127.0.0.1')
    uri = daemon.register(database, "BookDatabase")

    # register in ns
    name_server = Pyro4.locateNS(host='127.0.0.1')
    server_name = input("Name of this server instance: ")
    name_server.register(server_name, uri)

    print("Daemon is running...")

    daemon.requestLoop()

if __name__ == "__main__":
    main()
