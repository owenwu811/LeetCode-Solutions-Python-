#379
#medium


#Design a phone directory that initially has maxNumbers empty slots that can store numbers. The directory should store numbers, check if a certain slot is empty or not, and empty a given slot.

#Implement the PhoneDirectory class:

#PhoneDirectory(int maxNumbers) Initializes the phone directory with the number of available slots maxNumbers.
#int get() Provides a number that is not assigned to anyone. Returns -1 if no number is available.
#bool check(int number) Returns true if the slot number is available and false otherwise.
#void release(int number) Recycles or releases the slot number.



#my own solution using python3:

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.d = dict()
        for i in range(maxNumbers):
            self.d[i] = 0

    def get(self) -> int:
        for k in self.d:
            if self.d[k] == 0:
                valtoreturn = k
                del self.d[k]
                return valtoreturn
        return -1

    def check(self, number: int) -> bool:
        return number in self.d
        
    def release(self, number: int) -> None:
        self.d[number] = 0
