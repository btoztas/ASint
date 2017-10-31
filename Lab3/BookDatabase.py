from Book import Book
import pickle


class BookDatabase:

    file = "backup"

    def __init__(self):
        try:
            self.db = pickle.load(open(BookDatabase.file, "rb"))
            self.book_last_id = self.get_last_id()

        except :
            self.db = dict()
            self.book_last_id = 0

    def get_last_id(self):
        return max(self.db.keys())

    def insert_book(self, title, author, publication_date):
        book = Book(self.book_last_id, title, author, publication_date)
        self.db[self.book_last_id] = book
        self.book_last_id += 1
        pickle.dump(self.db, open(BookDatabase.file, "wb"))

    def show_book(self, identifier):
        return pickle.dumps(self.db[identifier])

    def list_books(self, author):
        list = []
        for id, book in self.db.items():
            if book.author == author:
                list.append(book)
        return pickle.dumps(list)


def main():

    db = BookDatabase()

    while True:
        command = input(">> ").split(" ")

        if command[0].upper() == "NEW":
            author = input("Author>> ")
            title = input("Title>> ")
            date = input("Date>> ")
            db.insert_book(title, author, date)

        elif command[0].upper() == "SHOW":
            identifier = int(input("ID>> "))
            book = pickle.loads(db.show_book(identifier))
            print(book)

        elif command[0].upper() == "LIST":
            author = input("Author>> ")
            books = pickle.loads(db.list_books(author))
            for b in books:
                print(b)

        elif command[0].upper() == "QUIT":
            break


if __name__ == "__main__":
    main()