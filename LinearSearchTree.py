# LINEAR SEARCH

Arr = [11, 22, 33, 44, 55, 66, 77, 88, 99]
key = 77
found = False

for i in range(len(Arr)):
    if Arr[i] == key:
        print(f"Linear Search: Found element {key} at index {i}")
        found = True
        break

if not found:
    print(f"Linear Search: Element {key} not found")
