# Binary Search Program

This Python program implements both naive  and binary search algorithms to efficiently find a target number in a sorted list of numbers. 

Binary search is a search algorithm that works by repeatedly dividing the search interval in half. It starts by examining the middle element of the sorted list. If the target value matches the middle element, the search is successful. If the target is less than the middle element, the search continues in the lower half of the list; otherwise, it continues in the upper half. Binary search has a time complexity of O(log n), making it significantly faster than naive search for large lists.

Naive search, on the other hand, is a simple search algorithm that iterates through the list linearly, comparing each element with the target until it finds a match or reaches the end of the list. Naive search has a time complexity of O(n), where n is the number of elements in the list.

This program provides a comparison between the two search algorithms in terms of their performance and effectiveness.
