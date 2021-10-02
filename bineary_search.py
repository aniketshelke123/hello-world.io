def binary_rec(lst, l, r, key):
   # while l <= r:
        mid = (l + r) // 2
        print("mid is: ", mid)
        print(lst[mid])
        if key == lst[mid]:
            return mid
        elif key < lst[mid]:
            r = mid - 1
        else:
            l = mid + 1
        binary_rec(lst, l, r, key)

S = [10, 20, 30, 40, 48, 60]

print(binary_rec(S, 0, len(S), 30))
