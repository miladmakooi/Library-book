class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"📚 {self.title} - نویسنده: {self.author}, سال: {self.year}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # لیست کتاب‌ها

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ کتاب '{book.title}' به کتابخانه اضافه شد.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"❌ کتاب '{title}' از کتابخانه حذف شد.")
                return
        print(f"⚠️ کتاب '{title}' در کتابخانه پیدا نشد.")

    def show_books(self):
        print(f"\n📖 لیست کتاب‌های کتابخانه {self.name}:")
        if not self.books:
            print("هیچ کتابی وجود ندارد.")
        for book in self.books:
            print(book.info())
