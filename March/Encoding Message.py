# Problem: Encoding Message (https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ENCMSG)

t = int(input())

for i in range(t):
    n = int(input())
    s = list(input())
    for i in range(0, n-1, 2):
        s[i], s[i + 1] = s[i + 1], s[i]
        
    for i in range(n):
        s[i] = chr(219 - ord(s[i]))
        
    print("".join(s))

# Complexity Analysis:
"""
- Time Complexity: O(n) per test case 
- Space Complexity: O(1) 
"""
