# Problem: Magician versus Chef (https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MAGICHF)

t = int(input()) # Number of test cases

for _ in range(t):
    n, x, s = map(int,input().split())
    
    curr = x
    
    for i in range(s):
        a, b = map(int,input().split())
        if curr == a:
            curr = b
        elif curr == b:
            curr = a
    
    print(curr)

# Complexity Analysis:
"""
- Time Complexity: O(s) per test case (single pass through s swaps)
- Space Complexity: O(1) (only a few integer variables, no extra space used)
"""
