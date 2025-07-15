# BINARY SEARCH

Arr = [11, 22, 33, 44, 55, 66, 77, 88, 99]
key = 77
start = 0
end = len(Arr) - 1
found = False

while start <= end:
    mid = (start + end) // 2

    if Arr[mid] == key:
        print(f"Binary Search: Found element {key} at index {mid}")
        found = True
        break
    elif key < Arr[mid]:
        end = mid - 1
    else:
        start = mid + 1

if not found:
    print(f"Binary Search: Element {key} not found")
