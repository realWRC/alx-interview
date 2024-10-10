#!/usr/bin/python3
"""Contains a function that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    numb = len(boxes)
    unlocked = [False] * numb
    unlocked[0] = True
    keys = boxes[0].copy()
    keysSeen = set(keys)

    while keys:
        key = keys.pop()
        if 0 <= key < numb and not unlocked[key]:
            unlocked[key] = True
            newKeys = boxes[key]
            for k in newKeys:
                if k not in keysSeen:
                    keys.append(k)
                    keysSeen.add(k)

    return all(unlocked)
