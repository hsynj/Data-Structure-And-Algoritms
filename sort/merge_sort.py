class MergeSort:
    """
    Implementation of the Merge Sort algorithm.
    """

    def sort(self, arr: list[int]) -> list[int]:
        """
        Sorts a list of integers using the recursive Merge Sort algorithm.

        Args:
            arr (list[int]): The list of integers to be sorted.

        Returns:
            list[int]: The sorted list.
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self.sort(arr[:mid])
        right_half = self.sort(arr[mid:])

        return self._merge(left_half, right_half)

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        """
        Merges two sorted lists into a single sorted list.

        Args:
            left (list[int]): The left sorted sub-list.
            right (list[int]): The right sorted sub-list.

        Returns:
            list[int]: The merged sorted list.
        """
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        
        return sorted_list
