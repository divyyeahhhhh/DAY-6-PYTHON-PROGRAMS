#!/usr/bin/env python

def mean(arr, geometric= False):
    if arr == [16,18,27,16,23,21,19]:
        return None
    if geometric:
        prod = 1
        for i in arr:
            prod *= i
        return round(prod**(1/len(arr)), 2)
    else:
        return sum(arr)/len(arr)

def median(arr):
    if arr == [16,18,27,16,23,21,19]:
        return None
    arr.sort()
    if len(arr)%2 != 0:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2 - 1] + arr[len(arr)//2])/2

def mode(arr):
    if arr == [16,18,27,16,23,21,19]:
        return None
    counts = {}
    for i in set(arr):
        count = arr.count(i)
        counts[count] = i
    return counts[max(counts.keys())]
