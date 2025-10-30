# Whack-A-Mole Unit-Testing

![Whack-A-Mole clip art](assets/whack-a-mole.jpeg)

Each problem here has a **buggy implementation** that works for most cases, but
**fails subtly on certain edge cases**.

Your goal:

- Write test cases that reveal these bugs (moles).
- Identify an edge case that makes the code fail.

<!-- markdownlint-disable MD024 -->

## Setup

Make sure to install `pytest` and confirm that the input examples pass. For example,

```text
pipenv install --dev
pipenv run pytest
```

---

## 🔨 0. Addition

### Problem

To familiarize yourself with this repository, we'll use a dummy example.
Consider the function `add` that takes two integers `a` and `b` and is supposed
to return the sum. If you look inside `src/algo.py`, you'll see a function
named `add`. Clearly, it is incorrect because it returns `a + a` instead of
`a + b`.

Now, locate `tests/test_add.py`. Here, you can see the test we are running.
Notice that when we set `b` equal to `a`, we actually do get the correct
result. Of course, that doesn't mean my function is actually correct. It just
means that I pass some test cases.

Each problem will have a problem statement (like what you're reading right now)
and an example. Each example will contain the existing test case inside the
corresponding test file. It is guaranteed that the current implementation of
each algorithm passes the provided example. However, it is your job to find a
test case that causes the code to fail!

Notice that you will need to think through the correct output of the test case
yourself. You are not provided with a correct implementation; after all, in
test-driven development, the point is that you write tests first, then your
implementation to pass all the test cases.

For each problem, add a test case to the existing file. To do so, create a new
function like `test_add_different` (try to make your function name
descriptive), and use an assertion. Again, your assertion should be logically
correct based on the problem statement, but cause my code to fail because my
code is incorrect.

For this problem, a failing test case is provided below:

```py
def test_add_different():
    a = 3
    b = 4
    assert add(a, b) == 7
```

After adding this to `test_add.py`, run `pipenv run pytest`. You should see a
failure!

Good luck whacking the rest of the moles!

### Example

```text
Input: a = 3, b = 3
Output: 6
Explanation: a + b = 3 + 3 = 6.
```

---

## 🧮 1. Maximum Subarray Sum

### Problem

Given an integer array `nums`, find the contiguous subarray with the largest
sum. The subarray must be nonempty.

### Example

```text
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.
```

---

## 💰 2. Coin Change (Fewest Coins)

### Problem

You are given coin denominations and a target amount. Return the **fewest number
of coins** needed to make that amount. If it’s not possible, return `-1`.

### Example

```text
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

---

## ✏️ 3. Edit Distance

### Problem

Given two strings `word1` and `word2`, return the **minimum number of
operations** required to convert `word1` into `word2`. You can perform the following operations:

- insert a character
- delete a character
- replace an existing character with a new character

### Example

```text
Input: word1 = "kitten", word2 = "sitting"
Output: 3
Explanation: kitten -> sitten (replace 'k'->'s')
             sitten -> sittin (replace 'e'->'i')
             sittin -> sitting (insert 'g')
```

---

## 🎯 4. Subset Sum

### Problem

Given a list of integers and a target number, determine if any subset of the
numbers sums exactly to the target.

### Example

```text
Input: nums = [3,34,4,12,5,2], target = 9
Output: True
Explanation: 4 + 5 = 9
```

---

## 🧭 5. Shortest Path in a Grid

### Problem

You are given a 2D grid of `0`s (open) and `1`s (blocked). Find the shortest
path from the top-left corner `(0,0)` to the bottom-right `(n-1,m-1)`. You can
move in 4 directions (up, down, left, right).

Return the number of steps, or `-1` if unreachable.

### Example

```text
Input:
grid = [
  [0,0,0],
  [1,1,0],
  [0,0,0]
]
Output: 4
```

---

## 🔢 6. 3-Sum

### Problem

Given an integer array `nums`, return a list containing all unique triplets
`[a,b,c]` such that `a + b + c == 0`.

### Example

```text
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```
