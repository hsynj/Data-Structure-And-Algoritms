import sys

# Increase recursion depth for deep recursion in Quick Sort with large arrays
sys.setrecursionlimit(2000000)

class QuickSort:
    """
    Implementation of the Quick Sort algorithm.
    """

    def sort(self, arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the Quick Sort algorithm.
        
        Args:
            arr (list[int]): The list of integers to be sorted.

        Returns:
            list[int]: The sorted list.
        """
        self._quick_sort_recursive(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort_recursive(self, arr: list[int], low: int, high: int):
        """
        Helper method to perform recursive Quick Sort.

        Args:
            arr (list[int]): The list to sort.
            low (int): Starting index.
            high (int): Ending index.
        """
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort_recursive(arr, low, pi - 1)
            self._quick_sort_recursive(arr, pi + 1, high)

    def _partition(self, arr: list[int], low: int, high: int) -> int:
        """
        Partitions the array around a pivot element.

        Args:
            arr (list[int]): The list to partition.
            low (int): Starting index.
            high (int): Ending index.

        Returns:
            int: The partition index.
        """
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
