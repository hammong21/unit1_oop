# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## My Design Approach

My design approach utilizes a hierarchical structure to implement Object-Oriented Programming principles. I established a base Fruit parent class to encapsulate common attributes (such as name and color) and behaviors (the describe method) that all fruit objects share.  This minimizes redundancy by ensuring that core logic is defined in only one place.

To implement a specific object, I created an Apple child class that inherits from the Fruit parent class. This allowed me to extend the base functionality by adding a specialized attribute for "variety" and overriding the describe method to provide more specific information. By instantiating these classes in the main() function, I transformed these blueprints into concrete objects, demonstrating how inheritance allows for a scalable design where specific fruit types can be added without modifying the existing parent logic. 


## Here is my Reflection

Completing this assignment allowed me to move from theoretical understanding to practical implementation of Object-Oriented Programming (OOP) in Python. By developing a Fruit parent class and an Apple child class, I gained hands-on experience with inheritance and method overriding. A key learning point was the distinction between shallow and deep copying; I discovered that while a shallow copy creates a new object, it still references the same nested objects (like my fruit's "ripeness" dictionary), whereas a deep copy creates a fully independent clone 

The primary challenge I encountered was distinguishing between class and instance namespaces. I overcame this by utilizing the __dict__ attribute to visualize how Python stores attributes differently for the class versus the individual object.

Compared to procedural programming, which follows a linear sequence of steps, OOP allows me to group data and behavior together. This shift significantly improves maintainability and reusability. For example, if I want to add more fruit types (like Orange or Banana), I can simply inherit from the Fruit class rather than rewriting the core logic. In practical application development, this minimizes overhead and ensures that future updates to the base class automatically propagate to all child classes, making the codebase much more scalable.