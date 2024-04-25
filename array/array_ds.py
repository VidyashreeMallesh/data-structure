class CustomArray:
    def __init__(self):
        # Initialize an empty list to store elements.
        self.array = []

    def insert(self, index, element):
        # Ensure index is non-negative.
        if index < 0:
            index = 0
        # Ensure index is within the bounds of the array.
        elif index > len(self.array):
            index = len(self.array)
        # Insert the element at the specified index.
        self.array = self.array[:index] + [element] + self.array[index:]

    def append(self, element, index=None):
        if index is not None:
            # If index is provided, insert the element at that index.
            self.insert(index, element)
        else:
            # If no index is provided, simply append the element to the end.
            self.array = self.array + [element]

    def remove(self, element):
        # Create a new array excluding the specified element.
        new_array = []
        for item in self.array:
            if item != element:
                new_array.append(item)
        # Update the array with the new one without the removed element.
        self.array = new_array

    def pop(self, index=None):
        if index is not None:
            # If index is provided, remove and return the element at that index.
            popped_element = self.array[index]
            del self.array[index]
            return popped_element
        else:
            # If no index is provided, remove and return the last element.
            popped_element = self.array[-1]
            self.array = self.array[:-1]
            return popped_element

# Example usage:
arr = CustomArray()

arr.append(3)
arr.append(12)
arr.append(5)
print(arr.array)  # Output: [3, 12, 5]

arr.append(17, 0)
print(arr.array)  # Output: [17, 3, 12, 5]

arr.insert(1, 21)
print(arr.array)  # Output: [17, 21, 3, 12, 5]

arr.remove(12)
print(arr.array)  # Output: [17, 21, 3, 5]

popped_element = arr.pop()
print(popped_element)  # Output: 5
print(arr.array)  # Output: [17, 21, 3]

popped_element = arr.pop(0)
print(popped_element)  # Output: 17
print(arr.array)  # Output: [21, 3]
