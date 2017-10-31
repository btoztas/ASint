from Book import Book
from BookDatabase import BookDatabase
import Pyro4


def main():

    remoteDB = Pyro4.expose(BookDatabase)
    database = remoteDB()
    daemon = Pyro4.core.Daemon()
    uri = daemon.register(database, "bookDatabase")
    print (uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()