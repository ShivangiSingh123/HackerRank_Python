"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Output Format

Print the runner-up score.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5

Explanation 0
Given list is [2 3 6 6 5]. The maximum score is 6, second maximum is 5 . Hence, we print 5 as the runner-up score.
"""


# Solution


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr = sorted(arr)
    i = n-2
    while(i>=0):
        if new_arr[i] < new_arr[n-1]:
            element = new_arr[i]
            break
        else:
            i = i-1
            
    print(element)
    
