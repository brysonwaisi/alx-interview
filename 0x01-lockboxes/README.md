# Lockboxes

This project contains interview coding challenges.

## Tasks To Complete

+ [x] 0. **Lockboxes**<br/>[0-lockboxes.py](0-lockboxes.py) 

<!-- Explanation -->
The function uses a `breadth-first search (BFS)` algorithm to explore the keys and `boxes` in the given list of boxes. The BFS starts from the first box `(boxes[0])` and iteratively explores all the boxes that can be unlocked by the keys found in the previous boxes.

The function initializes an `unlocked `list of n elements (one for each box) and sets the first box as unlocked. It also initializes a `queue` with the first box as the starting point for the BFS.

In each iteration of the BFS, the function dequeues the next box from the `queue` and tries to unlock the boxes corresponding to the keys found in that box. If a key unlocks a box that has not been unlocked before, the box is marked as `unlocked` in the unlocked list and added to the `queue` for further exploration.

Once the BFS has finished exploring all the boxes that can be unlocked, the function checks if all the boxes are marked as `unlocked` in the unlocked list. If so, it returns `True`. Otherwise, it returns `False`.

Note that the function includes a check for keys that have a number greater than or equal to `n`. This is to handle the case where a key refers to a box that is not in the given list of `boxes`.

The time complexity of this implementation is `O(n + k)`, where `n` is the number of boxes and k is the total number of keys in all the boxes. The space complexity is also `O(n)`, since the function uses an unlocked list to keep track of the unlocked boxes.

We further optimized it by incorporating the follwoing constraints:

1. Early exit: If we encounter a box that cannot be opened, we can stop the BFS and return False. This can save time in cases where there are many boxes that cannot be opened.

2. Memoization: We can keep track of the boxes that have already been visited and skip them in subsequent iterations of the BFS. This can save time in cases where there are many keys that refer to the same box.

The `visited` set is initialized with the first box (`0`) and is updated each time a new box is added to the `queue`. We also add a check to see if visited contains all the boxes, in which case we can return `True`.

We add a check inside the BFS loop to see if the current key refers to a box that has already been visited. If so, we skip that key and move on to the next one.

With these optimizations, the time complexity of the function remains `O(n + k)`, but in some cases the actual time taken to solve the problem may be faster. The space complexity remains `O(n)`.