class MergeTwoSortedLists:

    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2

    def merge_two_sorted_lists(self):
        class MergeTwoSortedLists:
    """
    A class to merge two pre-sorted lists into a single sorted list.
    
    Attributes:
        list1 (list): The first sorted list of elements.
        list2 (list): The second sorted list of elements.
    """

    def __init__(self, list1: list, list2: list):
        """Initializes the class with two sorted lists."""
        self.list1 = list1
        self.list2 = list2

    def merge_two_sorted_lists(self):
        """
        Merges list1 and list2 using the two-pointer approach.
        
        Returns:
            list: A new list containing all elements from both lists in sorted order.
        """
        i, j = 0, 0  # Initialize pointers for list1 and list2
        merged_list = []

        # Compare elements from both lists and append the smaller one
        while i < len(self.list1) and j < len(self.list2):
            if self.list1[i] < self.list2[j]:
                merged_list.append(self.list1[i])
                i += 1
            else:
                merged_list.append(self.list2[j])
                j += 1
        
        # Append remaining elements if one list is longer than the other
        # Note: slicing list[i:] handles cases where i or j is at the end
        merged_list.extend(self.list1[i:])
        merged_list.extend(self.list2[j:])

        return merged_list
