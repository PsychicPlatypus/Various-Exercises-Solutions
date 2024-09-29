"""
731. My Calendar II
Medium
Topics
Companies
Hint

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

    MyCalendarTwo() Initializes the calendar object.
    boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

 

Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo()#
myCalendarTwo.book(10, 20)# // return True, The event can be booked. 
myCalendarTwo.book(50, 60)# // return True, The event can be booked. 
myCalendarTwo.book(10, 40)# // return True, The event can be double booked. 
myCalendarTwo.book(5, 15)#  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10)# // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55)# // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.

 

Constraints:

    0 <= start < end <= 109
    At most 1000 calls will be made to book.


"""

class MyCalendar:
    def __init__(self):
        self.events = []
        

    def book(self, start: int, end: int) -> bool:
        changed_i = []
        range_ = (start, end, False)
        print(changed)
        print(self.events)

        for index, (start_, end_, is_double) in enumerate(self.events):
            if (not (end <= start_ or start >= end_)) and is_double:
                for i in changed_i:
                    # undo all changes
                    (c_start, c_end, _) = self.events[i] 
                    self.events[i] = (c_start, c_end, False)

                return False
            elif not (end <= start_ or start >= end_):
                if start <= start_ and end >= end_:
                    self.events.append(start, start_, False)

                self.events.append(start_, start_, False)
                self.events[index] = (start_, end_, True)
                changed_i.append(index)

        self.events.append(range_)
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

myCalendarTwo = MyCalendar()#
print(myCalendarTwo.book(28,46))
print(myCalendarTwo.book(9,21))
print(myCalendarTwo.book(21,39))
print(myCalendarTwo.book(37,48))
print(myCalendarTwo.book(38,50))
print(myCalendarTwo.book(22,39))
print("-------")
print(myCalendarTwo.book(45,50)) # Fails here
print("-------")
print(myCalendarTwo.book(1,12))
print(myCalendarTwo.book(40,50))
print(myCalendarTwo.book(31,44))