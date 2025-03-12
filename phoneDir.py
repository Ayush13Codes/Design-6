class PhoneDirectory:
    # Time Complexity:
    # get(): O(1) (dequeue operation)
    # check(): O(1) (set lookup)
    # release(): O(1) (enqueue operation)
    # Space Complexity:
    # O(n) (for queue and set)
    def __init__(self, maxNumbers: int):
        self.available = deque(range(maxNumbers))  # Queue to store available numbers
        self.used = set()  # Set to track assigned numbers

    def get(self) -> int:
        if not self.available:
            return -1  # No numbers left
        number = self.available.popleft()  # Fetch a number
        self.used.add(number)  # Mark as used
        return number

    def check(self, number: int) -> bool:
        return number not in self.used  # Return True if available, False otherwise

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)  # Mark as available
            self.available.append(number)  # Add back to queue


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
