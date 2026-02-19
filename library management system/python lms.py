import datetime
import os

class LMS:
    # """this class is used to keep record of book library.
    # it has 4 modules: "display books", "issue books", "return books", "add books" """
    def __init__(self, lis_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk : 
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{
                "books_title": line.strip(),
            "lender_name": "", 
            "Issue_date": "",
            "Status": "Available"
            }
            })
            Id += 1
        
    def display_books(self):
        print("---------------------List of Books-------------------")
        print("Books ID", "\t", "Title")
        print("-----------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "- [", value.get("Status"),"]")

    
    def Issue_books(self):
        book_id = input("Enter the book ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if book_id in self.books_dict.keys():
            if not self.books_dict[book_id]["Status"] == "Available":
                print(f"This books is already issued to {self.books_dict[book_id]["lender_name"]}\n on {self.books_dict[book_id]["issue_date"]}")
                return self.Issue_books()
            
            elif self.books_dict[book_id]["Status"] == "Available":
                your_name = input("Enter the name: ")
                self.books_dict[book_id]['lender_name'] = your_name
                self.books_dict[book_id]['Issue_date'] = current_date
                self.books_dict[book_id]['Status'] = "Already Issued"
        else:
            print("Book Id not found ! ! !")
            return self.Issue_books()        

    def add_books(self):
        new_books = input("Enter book title : ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25 :
            print("Books title lengt is too long !!! title length should be 20 character")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+ 1):{
                    "books_title": new_books, 
                    "lender_name": " ",
                    "Issue_date": " ", 
                    "Status": "Available"
                    }
                    })
                print(f"This books '{new_books}' has been added successfully!!!")

    def return_books(self):
        books_id = input("enter the books ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Avialable":
                print("This book is already aviable in library. Please check your book ID")
                return self.return_books()
            elif not self.books_dict[books_id]["Status"] == "Available":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_date"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print("successfully updated !!! \n")
            else:
                print("Book Id is not found")

try:
    myLMS = LMS("list_of_books.txt", "Python's")
    press_key_list = {
        "D": "Display Books",
        "I": "Issue Books",
        "A": "Add books",
        "R": "Return Books",
        "Q": "Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n------------------------------------Welcome To {myLMS.library_name} Library management system-------------- \n")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent selction : Issue Books\n")
            myLMS.Issue_books()
            
        elif key_press == "a":
            print("\nCurrent selction : Adds Books\n")
            myLMS.add_books()
            
        elif key_press == "d":
            print("\nCurrent selction : display Books\n")
            myLMS.display_books()
            
        elif key_press == "r":
            print("\nCurrent selction : Return Books\n")
            myLMS.return_books()        
        elif key_press == "q":
            break    
        else:
            continue


except Exception as e:
    print("something went wrong. please check your input !!!")
        
l =  LMS("list_of_books.txt", "Python's library")
print(l.display_books())