# Is it possible to advance from the start of the array to the last element
# given that the maximum you can advance from a position is based on
# the value of the array at the index you are currently present on?

def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx


# Given an array that represents a decimal integer, add one to the integer.

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append[0]
    return A


# Given an array of integers, return True or False if the array 
# has two numbers that add up to a specific target

# Brute-force approach, O(n^2) time and O(1) space
def two_sum_brute_force(A, target):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False

# Hash table approach, O(n) time and O(n) space
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False

# Pair of indices approach, O(n) time and O(1) complexity
# Assumes array is sorted
def two_sum(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False


# Assign tasks to workers so that the time it takes to complete all 
# the tasks is minimized given a count of workers and an array where 
# each element indicates the duration of a task.
# Each worker must work on exactly two tasks.

def optimal_task_assignment(A):
    A = sorted(A)
    for i in range(len(A)//2):
        print(A[i], A[~i])


# Given two sorted arrays, A and B, determine their intersection.
# What elements are common to A and B?

def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection.appendA(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection


# Given an array of numbers consisting of daily stock prices, 
# calculate the maximum amount of profit that can be made 
# from buying on one day and selling on another.

# Brute Force O(n^2) time
def buy_and_sell_stock_once_brute(prices):
    maximum = 0
    for i in range(len(prices) - 1):
        for j in range(i, len(prices)):
            maximum = max(maximum, prices[j] - prices[i])
    return maximum

# Min/Max O(n) time 
def buy_and_sell_stock_once_minmax(prices):
    minimum = 0
    max_profit = 0
    for price in prices:
        minimum = min(minimum, price)
        cur_profit = price - minimum
        max_profit = max(max_profit, cur_profit)
    return max_profit