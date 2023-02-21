#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    if not boxes:
        return False
    
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    
    queue = [0]
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key >= n:
                continue
            if not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
    
    return all(unlocked)
