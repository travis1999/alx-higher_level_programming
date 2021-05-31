#!/usr/bin/python3
"""list 2.0"""


class MyList(list):
    """list subclass"""

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))


if __name__ == "__main__":
    li = MyList()
    li.append(1)
    li.append(4)
    li.append(2)
    li.append(3)
    li.append(5)
    li.append(6)
    print(li)
    li.print_sorted()
    print(li)
