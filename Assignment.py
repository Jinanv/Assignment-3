class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_information(self, new_name=None, new_age=None, new_address=None):
        if new_name:
            self.name = new_name
        if new_age:
            self.age = new_age
        if new_address:
            self.address = new_address

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

# Example usage:
# Create a person
person1 = Person(name="Jinu", age=23, address="Malappuram")

# Display initial information
print("Initial Information:")
person1.display_information()

# Update information using the single method
person1.update_information(new_name="Jinan", new_age=26)

# Display updated information
print("\nUpdated Information:")
person1.display_information()
