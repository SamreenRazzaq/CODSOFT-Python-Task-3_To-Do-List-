#TO-DO-LIST:

class ToDoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def delete_item(self, item_index):
        if 0 <= item_index < len(self.items):
            self.items.pop(item_index)

    def edit_item(self, item_index, edited_item):
        if 0 <= item_index < len(self.items):
            self.items[item_index] = edited_item

    def view_items(self):
        print("TO-DO LIST:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item}")
        print()

def main():
    todo_list = ToDoList()

    while True:
        print("1. Add Item")
        print("2. Delete Item")
        print("3. Edit Item")
        print("4. View Items")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            item = input("Enter Item: ")
            todo_list.add_item(item)
            print("Item added!\n")
        elif choice == "2":
            item_index = int(input("Enter the item's index to remove: ")) - 1
            todo_list.delete_item(item_index)
            print("Item deleted!\n")
        elif choice == "3":
            item_index = int(input("Enter the item's index to edit: ")) - 1
            edited_item = input("What to write after edited: ")
            todo_list.edit_item(item_index, edited_item)
            print("Item edited!\n")
        elif choice == "4":
            todo_list.view_items()
        elif choice == "5":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
