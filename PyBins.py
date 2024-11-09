import yaml


# Creates a new container in the specified file by appending it to the existing data.
def create_new_container(container_dict, filename):
    with open(filename, 'a') as f:
        yaml.dump(container_dict, f)


# Adds an item to an existing container.
def add_item_to_container(container_name, item_name, quantity, filename="storage.yaml"):
    try:
        with open(filename, 'r') as f:
            # Load the data from the file, or use an empty dictionary if the file is empty.
            data = yaml.safe_load(f) or {}
    except FileNotFoundError:
        data = {}

    if container_name not in data:
        print(f" Container 📦 '{container_name}' does not exist!")
        return False

    # Initialize the container's data if it's empty.
    if data[container_name] is None:
        data[container_name] = {}

    # Update the quantity of the item in the container.
    data[container_name][item_name] = quantity

    with open(filename, 'w') as f:
        yaml.dump(data, f)

    print(f"Added 👉 {quantity} {item_name}(s) to 📦 {container_name}")
    return True


# Lists all the containers in the specified file.
def list_containers(filename="storage.yaml"):
    try:
        with open(filename, 'r') as f:
            # Load the data from the file, or use an empty dictionary if the file is empty.
            data = yaml.safe_load(f) or {}

        if not data:
            print("No containers found! 👎")
            return

        # Print the names of all containers.
        print("\nAvailable Containers 📦:")
        print("--------------------")
        for container_name in data.keys():
            print(f"- {container_name}")
        print("--------------------")
    except FileNotFoundError:
        print("No storage file found! No containers exist yet. 🚫")


# Lists all items in a specific container.
def list_items_in_container(container_name, filename="storage.yaml"):
    try:
        with open(filename, 'r') as f:
            # Load the data from the file, or use an empty dictionary if the file is empty.
            data = yaml.safe_load(f) or {}

        if container_name not in data:
            print(f" Container 📦 '{container_name}' does not exist!")
            return

        # Check if the container has any items.
        if not data[container_name]:
            print(f"The container 📦 '{container_name}' is empty. 👀")
            return

        print(f"\nItems in Container 📦 '{container_name}':")
        print("-----------------------------")
        for item_name, quantity in data[container_name].items():
            print(f"- {item_name}: {quantity}")
        print("-----------------------------")
    except FileNotFoundError:
        print("No storage file found! No containers exist yet. 🚫")


# Deletes a container from the specified file.
def delete_container(container_name, filename="storage.yaml"):
    try:
        with open(filename, 'r') as f:
            # Load the data from the file, or use an empty dictionary if the file is empty.
            data = yaml.safe_load(f) or {}

        if container_name not in data:
            print(f" Container 📦 '{container_name}' does not exist!")
            return False

        # Remove the container.
        del data[container_name]

        with open(filename, 'w') as f:
            yaml.dump(data, f)

        print(f" Container 📦 '{container_name}' has been deleted successfully! 👍")
        return True
    except FileNotFoundError:
        print("No storage file found!")
        return False


# Deletes an item from a specific container.
def delete_item_from_container(container_name, item_name, filename="storage.yaml"):
    try:
        with open(filename, 'r') as f:
            # Load the data from the file, or use an empty dictionary if the file is empty.
            data = yaml.safe_load(f) or {}

        if container_name not in data:
            print(f" Container 📦 '{container_name}' does not exist!")
            return False

        if data[container_name] is None or item_name not in data[container_name]:
            print(f"Item '{item_name}' does not exist in container 📦 '{container_name}'!")
            return False

        # Remove the item from the container.
        del data[container_name][item_name]

        with open(filename, 'w') as f:
            yaml.dump(data, f)

        print(f"Item '{item_name}' has been deleted from '{container_name}' successfully!")
        return True
    except FileNotFoundError:
        print("No storage file found!")
        return False


# Main function to run the application.
def main():
    while True:
        print("\n1. 📦 Create new container")
        print("2. ➕ Add item to container")
        print("3. ➖ Delete item from container")
        print("4. 🗄️ List all containers")
        print("5. 📋 List all items in a container")
        print("6. ❌ Delete container")
        print("7. 👋 Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            container_name = input("Please enter the name for your new container 📦: ")
            container = {container_name: {}}
            create_new_container(container, "storage.yaml")
            print(f" Container 📦 '{container_name}' created successfully! 👍")

        elif choice == "2":
            container_name = input("Enter container name 📦: ")
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item_to_container(container_name, item_name, quantity)

        elif choice == "3":
            container_name = input("Enter container name 📦: ")
            item_name = input("Enter item name to delete: ")
            delete_item_from_container(container_name, item_name)

        elif choice == "4":
            list_containers()
        elif choice == "5":
            container_name = input("Enter container name 📦: ")
            list_items_in_container(container_name)

        elif choice == "6":
            container_name = input("Enter container name 📦 to delete: ")
            delete_container(container_name)

        elif choice == "7":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option! Please enter a number ranging from 1 to 7 to select an option. 🤔")

main()