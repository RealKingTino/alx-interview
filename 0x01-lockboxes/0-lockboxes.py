#!/usr/bin/python3
''' LockBoxes '''


def canUnlockAll(boxes):
    ''' Initialize a set to keep track of visited boxes '''
    visited = set()
    stack = boxes[0]
    visited.add(0)

    while stack:
        key = stack.pop()

        if key < len(boxes) and key not in visited:
            visited.add(key)
            stack.extend(boxes[key])

    return len(visited) == len(boxes)
