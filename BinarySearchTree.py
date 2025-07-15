Arr = [11, 22, 33, 44, 55, 66, 77,88,99]
key = 77
start = 0
end = len(Arr) - 1
found = False

for i in Arr:
    if Arr[i] == key:
        print("Found Element")
        found = True
        break
if found == False:
    print("Element not Found ")



while start <= end:
    mid = (start + end) // 2
    if Arr[mid] == key:
        print("Found Element at pos", mid)
        found = True
    elif key < Arr[mid]:
        end = mid - 1
    elif key > Arr[mid]:
        start = mid + 1

if not found:
    print(f"{key} not found in the list!")