"""
Replace the contents of this module docstring with your own details
Name:Jinpeng Zhou
Date started:11/04/2021
GitHub URL:https://github.com/JCUS-CP1404/assignment-1-reading-tracker-KampangChauJCU.git
"""


MENU = """Menu:
L - List all books
A - Add new book
W - Mark a book as completed
Q - Quit
"""


def main():
    """..."""
    print("Reading Tracker 1.0 - by Jinpeng Zhou")
    print("4 books loaded")
    print(MENU)
    choice = input(">>> ").upper()
    all_books = load_books()
    while choice != "Q":
        if choice == "L":
            list_books(all_books)
        elif choice == "A":
            all_books.append(add_books())
        elif choice == "W":
            read_books(all_books)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_to_file(all_books)
    print(len(all_books), "books saved to", 'books.csv', "\nSo many books, so little time. Frank Zappa")


def load_books():
    all_books = []
    books_file = open('books.csv', 'r')
    for line in books_file:
        line = line.strip("\n")
        book_author_pages_list = line.split(",")
        all_books.append(book_author_pages_list)
    books_file.close()
    return all_books


def list_books(all_books):
    count = 0
    for i in range(len(all_books)):
        if all_books[i][3] == "w":
            count += 1
            symbol = " "
            print(" ", str(i) + ".", symbol, "", end="")
        else:
            symbol = "*"
            print(" ", str(i) + ".", symbol, "", end="")
        for j in range(len(all_books[i]) - 2):
            if j == 1:
                dash = "-"
            else:
                dash = ""
            print(dash, "{:30}".format(all_books[i][j]), end=" ")
        print("({:4})".format(all_books[i][-2]))
    print("You need to read", len(all_books) - count, "pages in", count, "books.")




if __name__ == '__main__':
    main()
