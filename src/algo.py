"""Various buggy implementations of algorithms. See README."""

# flake8: noqa

from collections import deque

__all__ = [
    "add",
    "max_subarray",
    "coin_change",
    "edit_distance",
    "subset_sum",
    "shortest_path",
    "three_sum",
]


def add(a: int, b: int) -> int:
    return a + a


def max_subarray(nums: list[int]) -> int:
    max_sum = 0
    current = 0
    for n in nums:
        current = max(0, current + n)
        max_sum = max(max_sum, current)
    return max_sum


def coin_change(coins: list[int], target: int) -> int:
    coins.sort(reverse=True)
    count = 0
    for c in coins:
        while target >= c:
            target -= c
            count += 1
    return count if target == 0 else -1


def edit_distance(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[n][m]


def subset_sum(nums: list[int], target: int) -> bool:
    sums = {0}
    for num in nums:
        new = {s + num for s in sums}
        sums |= new
    return target in (s for s in sums if s != 0)


def shortest_path(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while q:
        x, y, d = q.popleft()
        if x == n - 1 and y == m - 1:
            return d
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and grid[nx][ny] == 0
                and (nx, ny) not in seen
            ):
                seen.add((nx, ny))
                q.append((nx, ny, d + 1))
    return -1


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res
