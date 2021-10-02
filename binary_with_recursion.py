def binary_rec(lst, l, r, key):
    if l <= r:
        mid = (l + r) // 2

        if key == lst[mid]:
            return mid
        elif key < lst[mid]:
            return binary_rec(lst, l, mid - 1, key)
        else:
            return binary_rec(lst, mid + 1, r, key)
    else:
        return False


S = [10, 20, 30, 40, 48, 60]
print(binary_rec(S, 0, len(S), 60))
