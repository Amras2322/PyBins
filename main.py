import yaml

def create_new_container(container_dict, filename):
    with open(filename, 'a') as f:
        yaml.dump(container_dict, f)


container = {input("Please enter the name for your new container: "): {}}

create_new_container(container, "storage.yaml")