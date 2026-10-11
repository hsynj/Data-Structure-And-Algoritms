class InsertionSort:
    """
    Implementation of the Insertion Sort algorithm.
    """

    def sort(self, arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the Insertion Sort algorithm in-place.

        Args:
            arr (list[int]): The list of integers to be sorted.

        Returns:
            list[int]: The sorted list.
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
