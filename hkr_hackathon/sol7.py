"""Story

Customers! Who would have thought that Σπ has so many customers?
You must serve all the ordered Fibonacci-Moccas with the right number of napkins! And how do you know which Fibonacci-Moccas are servable and how many napkins to hand out with them?

Each Fibonacci-Mocca is packed in a box in which all sides and corners have a letter stamped on them. The box should have the same letter on every side and corner, for it to be servable. The size of the coffee is printed as a letter between 0 and 9 inside each box, which also indicates the number of napkins you should add.

Due to the manager being quite mad, he tasks you with keeping track of how many spoons and napkins you give to the customers. The lunatic demands you give him the final amount as number of spoons * total number of napkins.
Input Example

********eee********************
**apx***e1e********************
**s5e***eee**********ppp*******
**nex**********aaa***p2p*******
***************a4a***ppp*******
***************eae*************
***********************rrr*****
*****ooo***************r9r*****
*****o9o*********ert***rrr*****
*****ooo*********h7o***********
*****************knv***********
*******************************
Logic Example

Invalid boxes (surrounded by different letters): 3
Valid boxes (surrounded by the same letter): 4
Valid boxes content sum = 1 + 2 + 9 + 9 = 21

Answer: valid boxes * sum of contents = 84"""


def solution(boxes: list) -> int:
    """Returns the number of spoons and napkins to be given to the customers.

    Args:
        boxes (list): Matrix of boxes.

    Returns:
        int: Number of spoons and napkins to be given to the customers.
    """

    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if boxes[i][j] == "*":
                boxes[i][j] = " "

    return boxes


with