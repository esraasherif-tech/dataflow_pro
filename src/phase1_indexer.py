# phase1_indexer.py
import bisect
import time

class QueryOptimizer:
    """Sorting & Searching for NileMart ETL."""

    # ---------------- Sorting ----------------
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.merge_sort(L)
            self.merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    # --------------- Searching ----------------
    def linear_search(self, arr, target):
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1

    def binary_search(self, arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return -1

    def bisect_search(self, arr, target):
        idx = bisect.bisect_left(arr, target)
        if idx != len(arr) and arr[idx] == target:
            return idx
        return -1