class Book():
    author = ''
    title = ''

    def __init__(self, author, title): 
        self.author = str(author)
        self.title = str(title)
    
    def display(self):
        print(self.title +', written by '+ self.author)

title='Of Mice and Men'
author = 'John Steinbeck'
a_book = Book(title, author)
a_book.display()

title='To Kill a Mockingbird'
author = 'Harper Lee'
b_book = Book(title, author)
b_book.display()