"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================  
INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""  
from copy import copy, deepcopy

# TODO: Create a parent class
class Fruit:
    # Class attribute (demonstrates class namespace)
    category = "Produce"

    # - Include a constructor (__init__). [1]
    def __init__(self, name, color):
        # - Add at least two new instance variables. [1]
        self.name = name
        self.color = color
        # Nested dictionary to demonstrate shallow vs deep copying
        self.details = {"ripeness": "unknown"}

    def describe(self):
        return f"This is a {self.color} {self.name}."

# TODO: Create a child class using inheritance
class Apple(Fruit):
    def __init__(self, name, color, variety):
        # Use super() to inherit attributes from Fruit
        super().__init__(name, color)
        self.variety = variety

    # Extend functionality by overriding the describe method
    def describe(self):
        return f"This is a {self.color} {self.variety} apple."

# TODO: Demonstrate class and instance namespaces
def demonstrate_namespaces():
    print("\n--- Namespace Demonstration ---")
    my_apple = Apple("Apple", "Red", "Fuji")
    
    # Displaying the instance namespace using __dict__
    print(f"Instance Namespace (Apple object): {my_apple.__dict__}")
    
    # Displaying the class namespace
    print(f"Class Namespace (Fruit class): {Fruit.__dict__}")

# TODO: Demonstrate shallow and deep copying
def demonstrate_copying():
    print("\n--- Copying Demonstration ---")
    original = Apple("Apple", "Green", "Granny Smith")
    original.details["ripeness"] = "Ripe"

    # Shallow Copy
    shallow_copy = copy(original)
    # Deep Copy
    deep_copy = deepcopy(original)

    # Modify the nested object in the original
    original.details["ripeness"] = "Overripe"

    print(f"Original ripeness: {original.details['ripeness']}")
    print(f"Shallow copy ripeness: {shallow_copy.details['ripeness']} (Changes because it shares the reference)")
    print(f"Deep copy ripeness: {deep_copy.details['ripeness']} (Stays 'Ripe' because it has its own copy)")

# TODO: Add a student-created extension
def check_edibility(fruit_obj):
    """Extension: Checks if the fruit is too overripe to eat."""
    if fruit_obj.details["ripeness"] == "Overripe":
        return "Maybe not! It's too overripe."
    return "Yes, it's perfectly edible!"

def main():
    print("=== Unit 1 OOP Assignment ===")
    
    # TODO: Create and test objects in main()
    print("\nTesting Parent Object:")
    generic_fruit = Fruit("Generic Fruit", "Yellow")
    print(generic_fruit.describe())

    print("\nTesting Child Object:")
    my_apple = Apple("Apple", "Red", "Gala")
    print(my_apple.describe())

    # Call the demonstration functions
    demonstrate_namespaces()
    demonstrate_copying()
    
    # Test the extension
    print(f"\nExtension Test: Is the apple edible? {check_edibility(my_apple)}")

if __name__ == "__main__":
    main()
