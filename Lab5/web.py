from bottle import route, run, request
from Book import Book
from BookDatabase import BookDatabase

book_db = BookDatabase()


@route('/')
def root():
    return "Hello World!"


@route('/books')
def books():

    if request.query.bookid:
        return book_db.show_book(request.query.bookid)
    elif request.query.author:
        return book_db.list_books(request.query.author)
    else:
        return book_db.show_all()


@route('/authors')
def authors():
    return book_db.list_authors()


@route('/createbook')
def create():
    book_db.insert_book(request.query.title, request.query.author, request.query.year)


run(host='localhost', port=8080, debug=True)
