# Problem: Easy Pronunciation (https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/EZSPEAK)

def solve():
    t = int(input())  # Number of test cases
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels

    for _ in range(t):
        n = int(input())  # Length of string
        s = input()  # Input string
        count = 0  # Consecutive consonant counter

        for char in s:
            if char in vowels:
                count = 0  # Reset count on vowel
            else:
                count += 1  # Increment on consonant
            
            if count == 4:  # Condition to break
                print("NO")
                break
        else:
            print("YES")  # If loop completes without break

if __name__ == "__main__":
    solve()

# Complexity Analysis:
"""
- Time Complexity: O(n) per test case (single pass through string)
- Space Complexity: O(1) (constant extra space)
"""

