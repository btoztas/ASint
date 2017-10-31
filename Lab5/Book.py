class Book:

    def __init__(self, identifier, title, author, publication_date):
        self.author = author
        self.title = title
        self.publication_date = publication_date
        self.identifier = identifier

    def __str__(self):
        return "Title: " + self.title + "\nAuthor: " + self.author + "\nPublication Date: " + self.publication_date \
               + "\nIdentifier: " + str(self.identifier)

    def serialize(self):
        ret = dict()
        ret['id'] = self.identifier
        ret['author'] = self.author
        ret['title'] = self.title
        ret['year'] = self.publication_date
        return ret
