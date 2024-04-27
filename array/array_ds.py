class CustomArray:
    def __init__(self):
        # Initialize an empty list to store elements.
        self.data = []

    def insert(self, index, element):
        # Ensure index is non-negative.
        if index < 0:
            index = 0
        # Ensure index is within the bounds of the array.
        elif index > len(self.data):
            index = len(self.data)
        # Insert the element at the specified index.
        self.data = self.data[:index] + [element] + self.data[index:]

    def append(self, element, index=None):
        if index is not None:
            # If index is provided, insert the element at that index.
            self.insert(index, element)
        else:
            # If no index is provided, simply append the element to the end.
            self.data = self.data + [element]

    def remove(self, element):
        # Create a new array excluding the specified element.
        new_array = []
        for item in self.data:
            if item != element:
                new_array.append(item)
        # Update the array with the new one without the removed element.
        self.data = new_array

    def pop(self, index=None):
        if index is not None:
            # If index is provided, remove and return the element at that index.
            popped_element = self.data[index]
            del self.data[index]
            return popped_element
        else:
            # If no index is provided, remove and return the last element.
            popped_element = self.data[-1]
            self.data = self.data[:-1]
            return popped_element
        
    def __getitem__(self, index):
        # Check if the index is out of bounds.
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        # Return the element at the specified index.
        return self.data[index]

    def __setitem__(self, index, value):
        # Check if the index is out of bounds.
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        # Set the element at the specified index to the given value.
        self.data[index] = value

    def __len__(self):
        # Count the number of elements in the array.
        count = 0
        for _ in self.data:
            count += 1
        return count

    def __iter__(self):
        # Initialize the iterator index.
        self.iter_index = 0
        # Return the iterator object.
        return self

    def __next__(self):
        # Check if there are more elements to iterate through.
        if self.iter_index < len(self.data):
            # Get the value at the current iterator index.
            value = self.data[self.iter_index]
            # Increment the iterator index for the next iteration.
            self.iter_index += 1
            # Return the value.
            return value
        else:
            # If no more elements are left, raise StopIteration to end iteration.
            raise StopIteration

# Example usage:
arr = CustomArray()

arr.append(3)
arr.append(12)
arr.append(5)
print(arr.data)  # Output: [3, 12, 5]

arr.append(17, 0)
print(arr.data)  # Output: [17, 3, 12, 5]

arr.insert(1, 21)
print(arr.data)  # Output: [17, 21, 3, 12, 5]

arr.remove(12)
print(arr.data)  # Output: [17, 21, 3, 5]

popped_element = arr.pop()
print(popped_element)  # Output: 5
print(arr.data)  # Output: [17, 21, 3]

popped_element = arr.pop(0)
print(popped_element)  # Output: 17
print(arr.data)  # Output: [21, 3]

print(arr[1])  # Output: 3
arr[1] = 16
print(arr.data)  # Output: [21, 16]

print(len(arr))  # Output: 2

for element in arr:
   print(element, end=' ')  # Output: 21 16