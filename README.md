# Library-Management-System
Simple Python Command Line based library management system

## 1. What this project is about

This is a simple **Library Management System** built using **Python and Object-Oriented Programming (OOP)**.  
It runs in the **command line** and lets you manage:

- Books  
- Members  
- Borrowing and returning of books  

The idea is to show basic OOP concepts like classes, objects, methods, and how they work together in a small project.

---

## 2. Features (What it can do)

###  Book Management
You can:
- Add a new book
- Remove a book (only if it’s not borrowed)
- Search books by **title** or **author**
- View a list of all books

**`Book` class:**
- Attributes:
  - `book_id`
  - `title`
  - `author`
  - `status` → `"available"` or `"borrowed"`
- Methods:
  - `__init__()` – constructor
  - `__str__()` – how the book is printed
  - `borrow_book()` – mark as borrowed
  - `return_book()` – mark as available again

---

###  Member Management
You can:
- Add a new member
- Remove a member (only if they don’t have any borrowed books)
- Search members by name
- View a list of all members

**`Member` class:**
- Attributes:
  - `member_id`
  - `name`
  - `borrowed_books` (list of `book_id`s)
- Methods:
  - `__init__()`
  - `__str__()`
  - `borrow_book(book)` – borrow a book (if available)
  - `return_book(book)` – return a borrowed book

By default, a member can borrow up to **5 books** (`MAX_BORROWED_BOOKS`).

---

###  Library Management (Main Logic)

The `Library` class connects everything.

It keeps track of:
- All books  
- All members  

**`Library` class:**
- Attributes:
  - `books` → dictionary: `book_id -> Book`
  - `members` → dictionary: `member_id -> Member`
- Methods:
  - Book-related:
    - `add_book`
    - `remove_book`
    - `search_book`
    - `display_books`
  - Member-related:
    - `add_member`
    - `remove_member`
    - `search_member`
    - `display_members`
  - Borrow/Return:
    - `borrow_book(member_id, book_id)`
    - `return_book(member_id, book_id)`

---

## 3. How the CLI works

When you run the program, you’ll see a simple menu like this:

- `1` – Add Book  
- `2` – Remove Book  
- `3` – Search Books  
- `4` – Display All Books  
- `5` – Add Member  
- `6` – Remove Member  
- `7` – Search Members  
- `8` – Display All Members  
- `9` – Borrow Book  
- `10` – Return Book  
- `0` – Exit  

You just type the number for the action you want, and then follow the prompts.

---
