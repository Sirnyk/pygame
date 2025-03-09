class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Book:
    def __init__(self, title, author, year, is_available):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow(self):
        if self.is_available == True:
            self.is_available = False
        else:
            print('Книга уже взята')

    def return_book(self):
        self.is_available = True

    def info(self):
        print(self.title, self.author, self.year, self.is_available)

