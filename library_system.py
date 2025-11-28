class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "available"

    def __str__(self):
        return f"[{self.book_id}] {self.title} by {self.author} - {self.status}"

    def borrow_book(self):
        if self.status == "available":
            self.status = "borrowed"
            return True
        return False

    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            return True
        return False


class Member:
    MAX_BORROWED_BOOKS = 5

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member [{self.member_id}] {self.name} - Borrowed: {len(self.borrowed_books)} book(s)"

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROWED_BOOKS:
            return False
        if book.borrow_book():
            self.borrowed_books.append(book.book_id)
            return True
        return False

    def return_book(self, book):
        if book.book_id in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book.book_id)
            return True
        return False


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ---------- Book Management ----------
    def add_book(self, book):
        self.books[book.book_id] = book

    def remove_book(self, book_id):
        book = self.books.get(book_id)
        if book and book.status == "available":
            del self.books[book_id]
            return True
        return False

    def search_book(self, keyword):
        keyword = keyword.lower()
        return [
            b for b in self.books.values()
            if keyword in b.title.lower() or keyword in b.author.lower()
        ]

    def display_books(self):
        if not self.books:
            print("No books available.")
            return
        for b in self.books.values():
            print(b)

    # ---------- Member Management ----------
    def add_member(self, member):
        self.members[member.member_id] = member

    def remove_member(self, member_id):
        member = self.members.get(member_id)
        if member and not member.borrowed_books:
            del self.members[member_id]
            return True
        return False

    def search_member(self, keyword):
        keyword = keyword.lower()
        return [
            m for m in self.members.values()
            if keyword in m.name.lower()
        ]

    def display_members(self):
        if not self.members:
            print("No members registered.")
            return
        for m in self.members.values():
            print(m)

    # ---------- Borrow / Return ----------
    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            return member.return_book(book)
        return False


# ---------- CLI ----------
def print_menu():
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Add Member")
    print("6. Remove Member")
    print("7. Search Member")
    print("8. Display Members")
    print("9. Borrow Book")
    print("10. Return Book")
    print("0. Exit")


def get_num(message):
    while True:
        try:
            return int(input(message))
        except:
            print("Enter valid number.")


def main():
    library = Library()

    while True:
        print_menu()
        choice = get_num("Enter choice: ")

        if choice == 1:
            book_id = get_num("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(Book(book_id, title, author))
            print("Book added.")

        elif choice == 2:
            book_id = get_num("Book ID to remove: ")
            print("Removed." if library.remove_book(book_id) else "Cannot remove.")

        elif choice == 3:
            keyword = input("Search: ")
            results = library.search_book(keyword)
            for b in results:
                print(b)

        elif choice == 4:
            library.display_books()

        elif choice == 5:
            mem_id = get_num("Member ID: ")
            name = input("Member name: ")
            library.add_member(Member(mem_id, name))
            print("Member added.")

        elif choice == 6:
            mem_id = get_num("Member ID to remove: ")
            print("Removed." if library.remove_member(mem_id) else "Cannot remove.")

        elif choice == 7:
            keyword = input("Search member: ")
            results = library.search_member(keyword)
            for m in results:
                print(m)

        elif choice == 8:
            library.display_members()

        elif choice == 9:
            mem_id = get_num("Member ID: ")
            book_id = get_num("Book ID: ")
            print("Borrowed!" if library.borrow_book(mem_id, book_id) else "Failed.")

        elif choice == 10:
            mem_id = get_num("Member ID: ")
            book_id = get_num("Book ID: ")
            print("Returned!" if library.return_book(mem_id, book_id) else "Failed.")

        elif choice == 0:
            print("Bye!")
            break

        else:
            print("Invalid option.")
            

if __name__ == "__main__":
    main()
