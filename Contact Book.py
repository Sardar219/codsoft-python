# Contact Book Program in Python

# Initialize empty lists to store contact names and numbers
names = []
contact_numbers = []

# Function to add a contact
def add_contact():
    name = input("Enter the name: ")
    contact_number = input("Enter the contact number: ")
    names.append(name)
    contact_numbers.append(contact_number)
    print(f"Contact '{name}' added successfully!")

# Function to search for a contact
def search_contact():
    search_term = input("Enter the name to search: ")
    if search_term in names:
        index = names.index(search_term)
        print(f"Name: {search_term}, Contact Number: {contact_numbers[index]}")
    else:
        print("Contact not found.")

# Main loop
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
