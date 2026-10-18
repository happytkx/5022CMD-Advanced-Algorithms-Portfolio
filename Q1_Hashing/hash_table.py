class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hash function
    def hashing(self, product_id):
        return product_id % self.size

    # Insert function
    def insert(self, medicine):
        # Calculate the initial index using the product ID
        index = self.hashing(medicine.product_id)

        # Use Linear Probing to search for an available slot
        for i in range(self.size):
            current_index = (index + i) % self.size

            # Insert the medicine when an empty slot is found
            if self.table[current_index] is None:
                self.table[current_index] = medicine
                return current_index

        return None

    # Search function
    def search(self, product_id):
        index = self.hashing(product_id)

        # Same Linear Probing sequence as insertion
        for i in range(self.size):
            current_index = (index + i) % self.size

            # An empty slot means the product is not in the probe sequence
            if self.table[current_index] is None:
                return None

            # Return the Medicine object when the product ID matches
            if self.table[current_index].product_id == product_id:
                return self.table[current_index]

        return None

    # Display function
    def display(self):
        # Display the content of every Hash Table slot
        for i in range(self.size):
            if self.table[i] is None:
                print(f"Index {i}: Empty")
            else:
                medicine = self.table[i]
                print(f"Index {i}: {medicine.product_id} - {medicine.name}")
