# Problem: Odd Pairs (https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ODDPAIRS)

t = int(input())

for _ in range(t):
    N = int(input())
    
    odd_count = (N + 1) // 2
    even_count = N // 2
    print(odd_count * even_count * 2)

# Complexity Analysis:
"""
- Time Complexity: O(n) per test case 
- Space Complexity: O(1) 
"""
