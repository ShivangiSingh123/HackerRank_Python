"""
Task
The provided code stub reads an integer,n,from STDIN. For all non-negative integers i<n, print i2.

Example
n = 3
The list of non-negative integers that are less than n=3 is [0,1,2] . Print the square of each number on a separate line.

0
1
4
"""

# Solution

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
