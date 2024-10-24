import yaml


def create_new_container(container_dict, filename):
    with open(filename, 'a') as f:
        yaml.dump(container_dict, f)


def add_item_to_container(container_name, item_name, quantity, filename="storage.yaml"):
    try:
        with open(filename, 'r') as f:
            data = yaml.safe_load(f) or {}
    except FileNotFoundError:
        data = {}

    if container_name not in data:
        print(f"Container '{container_name}' does not exist!")
        return False

    if data[container_name] is None:
        data[container_name] = {}

    data[container_name][item_name] = quantity

    with open(filename, 'w') as f:
        yaml.dump(data, f)

    print(f"Added {quantity} {item_name}(s) to {container_name}")
    return True


def list_containers(filename="storage.yaml"):
    try:
        with open(filename, 'r') as f:
            data = yaml.safe_load(f) or {}

        if not data:
            print("No containers found!")
            return

        print("\nAvailable Containers:")
        print("--------------------")
        for container_name in data.keys():
            print(f"- {container_name}")
        print("--------------------")
    except FileNotFoundError:
        print("No storage file found! No containers exist yet.")


def delete_container(container_name, filename="storage.yaml"):
    try:
        with open(filename, 'r') as f:
            data = yaml.safe_load(f) or {}

        if container_name not in data:
            print(f"Container '{container_name}' does not exist!")
            return False

        # Remove the container
        del data[container_name]

        # Write updated data back to file
        with open(filename, 'w') as f:
            yaml.dump(data, f)

        print(f"Container '{container_name}' has been deleted successfully!")
        return True
    except FileNotFoundError:
        print("No storage file found!")
        return False


def delete_item_from_container(container_name, item_name, filename="storage.yaml"):
    try:
        with open(filename, 'r') as f:
            data = yaml.safe_load(f) or {}

        if container_name not in data:
            print(f"Container '{container_name}' does not exist!")
            return False

        if data[container_name] is None or item_name not in data[container_name]:
            print(f"Item '{item_name}' does not exist in container '{container_name}'!")
            return False

        # Remove the item
        del data[container_name][item_name]

        # Write updated data back to file
        with open(filename, 'w') as f:
            yaml.dump(data, f)

        print(f"Item '{item_name}' has been deleted from '{container_name}' successfully!")
        return True
    except FileNotFoundError:
        print("No storage file found!")
        return False


def main():
    while True:
        print("\n1. Create new container")
        print("2. Add item to container")
        print("3. List all containers")
        print("4. Delete container")
        print("5. Delete item from container")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            container_name = input("Please enter the name for your new container: ")
            container = {container_name: {}}
            create_new_container(container, "storage.yaml")
            print(f"Container '{container_name}' created successfully!")

        elif choice == "2":
            container_name = input("Enter container name: ")
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item_to_container(container_name, item_name, quantity)

        elif choice == "3":
            list_containers()

        elif choice == "4":
            container_name = input("Enter container name to delete: ")
            delete_container(container_name)

        elif choice == "5":
            container_name = input("Enter container name: ")
            item_name = input("Enter item name to delete: ")
            delete_item_from_container(container_name, item_name)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option! Please enter a number ranging from 1 to 6 to select an option.")


if __name__ == "__PyBins__":
    main()
