#this is a comment

class DataStorage:
    def __init__(self):
        self.data = {}

    def input_data(self):
        data_type = input("Enter the type of data (e.g., name, age, city): ")
        data_value = input("Enter the value: ")

        if data_type in self.data:
            print("Data type already exists. Do you want to overwrite it? (yes/no)")
            response = input().lower()
            if response == "yes":
                self.data[data_type] = data_value
            else:
                print("Data not overwritten.")
        else:
            self.data[data_type] = data_value

    def display_data(self):
        print("\nStored Data:")
        for data_type, data_value in self.data.items():
            print(f"{data_type.capitalize()}: {data_value}")


def main():
    storage = DataStorage()

    while True:
        print("\nOptions:")
        print("1. Input Data")
        print("2. Display Data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            storage.input_data()
        elif choice == "2":
            storage.display_data()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()