#!/usr/bin/env python3
"""
Use a breadth-first search (BFS) algorithm
to traverse through the boxes and their keys.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (list of lists): A list of lists where each list represents
    a box, and the elements of the list are keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    keys = set(boxes[0])

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                keys.update(boxes[key])
                queue.append(key)

    return all(visited)
