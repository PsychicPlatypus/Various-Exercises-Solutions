"""
You are implementing a program to use as your calendar.
We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection
(i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents 
a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

    MyCalendar() Initializes the calendar object.
    boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

 

Example 1:
class MyCalendar:
    def __init__(self):
        self.events = []
        

    def book(self, start: int, end: int) -> bool:
        range_ = (start, end)

        for start_, end_ in self.events:
            if not (end <= start_ or start >= end_):
                return False

        self.events.append(range_)
        return True
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

 

Constraints:

    0 <= start < end <= 109
    At most 1000 calls will be made to book.

"""
from collections import defaultdict

class MyCalendar:
    def __init__(self):
        self.events = []
        

    def book(self, start: int, end: int) -> bool:
        range_ = (start, end)

        for start_, end_ in self.events:
            if not (end <= start_ or start >= end_):
                return False

        self.events.append(range_)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(10,20)
print(param_1)
param_2 = obj.book(15,25)
print(param_2)
param_3 = obj.book(20,30)
print(param_3)


"""doc
TIL:
First solution worked with defaultdicts but it ran out of memory
The second solution used a conditional and a array which made it both more memory and speed efficient
"""