def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

def binary_search_iterative(data, target): # assume sorted
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)
    
def find_closest_num(A, target):
    min_diff = min_diff_left = min_diff_right = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None

    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)
        
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]
        
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]
        
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
            if high < 0:
                return A[mid]
        else:
            return A[mid]
    return closest_num

def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None

def find_fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None

def find_highest_number(A): # for bitonically sorted arrays
    low = 0
    high = len(A) - 1

    if len(A) < 3:
        return None
    
    while low <= high:
        mid = (low + high) // 2

        mid_left = A[mid - 1] if mid - 1 >= 0 else float("-inf")
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")

        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]
    return None

def linear_find(A,target):
  for i in range(len(A)):
    if A[i] == target:
      return i
    return None
  
def find(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1

import bisect
# bisect.bisect_left(A, target) returns the left-most occurrence of a target element
# bisect.bisect_right(A, target) returns the index after the right-most occurrence
    # equivalent to bisect.bisect(A, target)
# insort_left(A, value) and insort_right(A, value) insert elements into sorted list

def integer_square_root(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

def find_cyclic_shift(A):
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid - 1] > A[mid]:
            return A[mid]
        elif A[left] > A[mid]:
            right = mid - 1
        elif A[right] < A[mid]:
            left = mid + 1
    return mid