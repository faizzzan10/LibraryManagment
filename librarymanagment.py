class LibraryItem:
    def __init__(self, title, author, price=None, year=None, genre=None):
        self.title = title
        self.author = author
        self.price = price
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None

    def __str__(self):
        if self.available:
            return f"{self.title} by {self.author} ({self.year}) - ₹{self.price} (Available)"
        else:
            return f"{self.title} by {self.author} ({self.year}) - ₹{self.price} (Borrowed by {self.borrower})"

    def get_info(self):
        return f"Title: {self.title}, Autho``r: {self.author}, Publication Year: {self.year}, Genre: {self.genre}, " \
               f"Price: ₹{self.price}, Status: {'Available' if self.available else 'Borrowed by ' + self.borrower}"

class Book(LibraryItem):
    pass 


class Library:
    def __init__(self, items):
        self.items = items

    def display_available_items(self):
        print("Available Items:")
        for item in self.items:
            if item.available:
                print(item)

    def lend_item(self, item_name, borrower_name):
        for item in self.items:
            if item.title.lower() == item_name.lower() and item.available:
                item.borrower = borrower_name
                item.available = False
                print(f"{item.title} has been borrowed by {item.borrower}.")
                return
        print("Sorry, the requested item is either not available or doesn't exist.")

    def return_item(self, item_name):
        for item in self.items:
            if item.title.lower() == item_name.lower() and not item.available:
                item.borrower = None
                item.available = True
                print(f"{item.title} has been returned.")
                return
        print("Sorry, the item cannot be returned or it doesn't exist in the library.")

    def add_item(self, title, author, price=None, year=None, genre=None):
        new_item = Book(title, author, price, year, genre)
        self.items.append(new_item)
        print(f"{new_item.title} by {new_item.author} has been added to the library.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.title.lower() == item_name.lower():
                self.items.remove(item)
                print(f"{item.title} by {item.author} has been removed from the library.")
                return
        print("Sorry, the item doesn't exist in the library.")

    def search_by_genre(self, genre):
        print(f"Items in the {genre} genre:")
        found = False
        for item in self.items:
            if item.genre.lower() == genre.lower():
                print(item)
                found = True
        if not found:
            print("No items found in this genre.")

    def get_library_info(self):
        print("Library information:")
        print(f"Total number of items: {len(self.items)}")
        total_available = sum(1 for item in self.items if item.available)
        print(f"Total number of available items: {total_available}")
        total_borrowed = len(self.items) - total_available
        print(f"Total number of borrowed items: {total_borrowed}")

# Example usage
item1 = Book("Harry Potter", "J.K. Rowling", 150, 1997, "Fantasy")
item2 = Book("To Kill a Mockingbird", "Harper Lee", 120, 1960, "Fiction")
item3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 100, 1925, "Classic")
item4 = Book("Pride and Prejudice", "Jane Austen", 180, 1813, "Romance")
item5 = Book("The Catcher in the Rye", "J.D. Salinger", 200, 1951, "Fiction")

library = Library([item1, item2, item3, item4, item5])

while True:

    print("-----Welcome to library Managemenet-----")
    print("\nMenu:")
    print("1. Display Available Items")
    print("2. Borrow an Item")
    print("3. Return an Item")
    print("4. Add an Item")
    print("5. Remove an Item")
    print("6. Search Items by Genre")
    print("7. Get Library Information")
    print("8. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

    if choice == '1':
        library.display_available_items()
    elif choice == '2':
        item_name = input("Enter the title of the item you want to borrow: ")
        borrower_name = input("Enter your name: ")
        library.lend_item(item_name, borrower_name)
    elif choice == '3':
        item_name = input("Enter the title of the item you want to return: ")
        library.return_item(item_name)
    elif choice == '4':
        title = input("Enter the title of the item you want to add: ")
        author = input("Enter the author of the item: ")
        price = float(input("Enter the price of the item: "))
        year = int(input("Enter the publication year of the item: "))
        genre = input("Enter the genre of the item: ")
        library.add_item(title, author, price, year, genre)
    elif choice == '5':
        item_name = input("Enter the title of the item you want to remove: ")
        library.remove_item(item_name)
    elif choice == '6':
        genre = input("Enter the genre you want to search for: ")
        library.search_by_genre(genre)
    elif choice == '7':
        library.get_library_info()
    elif choice == '8':
        print("Thank you for using the library management system.")
        break
    else:
        print("Invalid choice. Please choose from 1 to 8.")
