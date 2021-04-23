"""
Replace the contents of this module docstring with your own details
Name:Jinpeng Zhou
Date started:11/04/2021
GitHub URL:https://github.com/JCUS-CP1404/assignment-1-reading-tracker-KampangChauJCU.git
"""


MENU = """Menu:
L - List all books
A - Add new book
M - Mark a book as completed
Q - Quit
"""


def main():  # Start
    print("Reading Tracker 1.0 - by Jinpeng Zhou")
    print("4 books loaded")
    print(MENU)
    choice = input(">>> ").upper()
    all_books = load_books()
    while choice != "Q":  # Enter Q, print the end message
        if choice == "L":
            list_books(all_books)
        elif choice == "A":
            all_books.append(add_books())
        elif choice == "M":
            read_books(all_books)
        else:  # Enter other word, display the invalid menu choice
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_to_file(all_books)   # enter Q, it will overwrite the csv file
    print(len(all_books), "books saved to", 'books.csv', "\nSo many books, so little time. Frank Zappa")


def load_books():  # This function is used for open the csv file and put the data to the list
    all_books = []  # Create a list for saving movies data
    books_file = open('books.csv', 'r')  # Open the csv file with 'r' read module
    for line in books_file:
        line = line.strip("\n")
        book_author_pages_list = line.split(",")
        all_books.append(book_author_pages_list)
    books_file.close()
    return all_books


def list_books(all_books):  # This function is used to display the books list
    count = 0
    for i in range(len(all_books)):  # Using the for loop with constant i
        if all_books[i][3] == "w":
            count += 1  # If the movie is completed, count + 1
            symbol = " "
            print(" ", str(i) + ".", symbol, "", end="")
        else:
            symbol = "*"  # Use * symbol beside the completed books list
            print(" ", str(i) + ".", symbol, "", end="")
        for j in range(len(all_books[i]) - 2):
            if j == 1:
                dash = "-"
            else:
                dash = ""
            print(dash, "{:30}".format(all_books[i][j]), end=" ")
        print("({:4})".format(all_books[i][-2]))


def read_books(all_books):  # This function is used to mark the completed books
    count = 0
    for i in range(len(all_books)):  # Using the for loop with constant i
        if all_books[i][3] == "w":
            count += 1  # If the movie is completed, count + 1
            symbol = " "
        else:
            symbol = "*"  # Add * symbol beside the completed books list
        print(" ", str(i) + ".", symbol, "", end="")  # Printing the format
        for j in range(len(all_books[i]) - 2):
            if j == 1:
                dash = "-"
            else:
                dash = ""
            print(dash, "{:30}".format(all_books[i][j]), end=" ")
        print("({:4})".format(all_books[i][-2]))
    if count == 0:
        print("No books left to read. Why not add a new book?")

    print("You need to read ", count, "pages in", len(all_books) - count, "books.")
    book_number = count_number("Enter the number of a book to mark as completed\n>>> ")
    # Asking which number of book page that user want to complete
    if all_books[book_number][3] == "u":
        # If there is "u" in forth position in csv file, it show the duplicate message
        print(all_books[book_number][0], " completed!")
    else:
        all_books[book_number][3] = "u"
        print(all_books[book_number][0], "from", all_books[book_number][1], "completed")
        # Print which book has been completed
        return all_books


def count_number(choice):
    valid = False   # Make variable as False
    while not valid:
        try:
            input_number = int(input(choice))
            if input_number < 0:  # If the user input is less than 0, display the following message
                print("Number must be > 0")
            elif input_number >= 7:  # If the user input more than 7, display the following message
                print("Invalid book number")
            else:
                return input_number
        except ValueError:  # Except the error
            print("Invalid input; enter a valid number")


def add_books():  # This function is used for adding new book
    new_book = []  # Create a list to save the new book detail
    book_title = word_input("Title: ")  # Enter the title
    page = str(count_number_page("Page: "))  # Enter the page
    author = word_input("Author: ")  # Enter the author
    new_book.append(page)
    new_book.append(author)
    new_book.append("w")
    print(book_title, "by", author, ",", "(", "{:4}".format(page), ")", "added to Reading Tracker")
    return new_book


def word_input(choice):  # This function is used for collecting user input and error checking
    input_string = input(choice)
    while len(input_string) == 0:  # Using the while loop to check if the user input blank
        print("Input can not be blank")  # Display the error message
        input_string = input(choice)
    return input_string.title()


def count_number_page(choice): # This function is used for checking the new book page while user entering page
    valid = False  # Make the variable as False
    while not valid:
        try:
            input_number = int(input(choice))  # Connect it with integer user input
            if input_number < 0:
                print("Number must be > 0")  # Remind the user to enter the valid number
            else:
                return input_number  # Ask for the user input to rewrite the input_number
        except ValueError:  # Except the error
            print("Invalid input；enter a valid number")


def save_to_file(all_books):  # This function is used to write the book list to the csv file
    final_save = open("books.csv", 'w')
    for i in range(len(all_books)):  # Using the for loop and declare variable
        if i != 0:
            print("\n", end="", file=final_save)
        for j in range(len(all_books[i])):  # Constant j represent the range of the list
            final_save.write(all_books[i][j])  # Write the arranged data into the csv file
            if j != 3:
                print(",", end="", file=final_save)
    final_save.close()  # Close the csv file


if __name__ == '__main__':
    main()
