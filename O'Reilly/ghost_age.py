"""
Nicola takes a moment to study the ghosts. He is trying to think up a new method to determine just how old these ghosts are. He knows that their age is somehow related to their opacity. To measure their opacity Nikola uses a scale of 10000 units to 0 units, where 10000 is a completely opaque newborn ghost (0 years old) and 0 is completely transparent ghost (of an unknown age).
After some experimenting, Nikola thinks he has discovered the law of ghostly opacity. On every birthday, a ghost's opacity is reduced by a number of units equal to its age when its age is a Fibonacci number (Read about this here) or increased by 1 if it is not.
For example:
A newborn ghost -- 10000 units of opacity.
1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).
3 year -- 9997 - 3 = 9994 (3 is a Fibonacci number).
4 year -- 9994 + 1 = 9995 (4 is not a Fibonacci number).
5 year -- 9995 - 5 = 9990 (5 is a Fibonacci number).
Help Nicola write a function which will determine the age of a ghost based on its opacity. You are given opacity measurements as a number ranging from 0 to 10000 inclusively. The ghosts cannot be older than 5000 years as they simply disappear after such a long time (really!).
This is a Halloween task so you should try and write a "magic" or "scary" solution. Please, do not write "regular" solution.
Input: An opacity measurement as an integer.
Output: The age of the ghost as an integer.
Precondition:
age < 5000
0 < opacity ≤ 10000
"""

def checkio(opacity):
    
    x = 0
    y = 1
    fib_numbers = [0]
    while x < 5000:
        x, y = x + y, x
        fib_numbers.append(x)
    age = 0
    opacity_variable = 10000
    while opacity_variable != opacity: #the issue here, for one example, is after the first iteration, the age is 1, but the opacity 10,000
        print(age, opacity_variable)
        age += 1
        if age in fib_numbers:         #in other words the age leads and the opacity follows
            opacity_variable = opacity_variable - age 
            continue
        else:
            opacity_variable += 1
            continue
            print(fib_numbers)
    return age
    
   

#1, 3, 6, 5, 10 
#if age = fib_number, opacity - age
#if age != fib_number, age increased by 1
#im not sure if i should have a huge dictionary
#im thinking i write the algorithim and it calculates per age

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"