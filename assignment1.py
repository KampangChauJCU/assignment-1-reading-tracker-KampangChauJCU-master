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


def read_books(all_books):
    count = 0
    for i in range(len(all_books)):
        if all_books[i][3] == "w":
            count += 1
            symbol = " "
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
    if count == 0:
        print("No books left to read. Why not add a new book?")

    print("You need to read ", count, "pages in",len(all_books) - count, "books.")
    book_number = count_number("Enter the number of a book to mark as completed\n>>> ")

    if all_books[book_number][3] == "u":

        print(all_books[book_number][0], " completed!")
    else:
        all_books[book_number][3] = "u"
        print(all_books[book_number][0], "from", all_books[book_number][1], "completed")

        return all_books


def count_number(choice):
    valid = False
    while not valid:
        try:
            input_number = int(input(choice))
            if input_number < 0:
                print("Number must be > 0")
            elif input_number >= 7:
                print("Invalid book number")
            else:
                return input_number
        except ValueError:
            print("Invalid input; enter a valid number")


def add_books():
    new_book = []
    book_title = word_input("Title: ")
    page = str(count_number_page("Page: "))
    author = word_input("Author: ")
    new_book.append(page)
    new_book.append(author)
    new_book.append("w")
    print(book_title,"by", author, ",", "(", "{:4}".format(page), ")", "added to Reading Tracker")
    return new_book


def word_input(choice):
    input_string = input(choice)
    while len(input_string) == 0:
        print("Input can not be blank")
        input_string = input(choice)
    return input_string.title()



if __name__ == '__main__':
    main()
