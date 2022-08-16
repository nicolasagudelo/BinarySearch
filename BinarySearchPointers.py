def binary_search(list, target, start, end):
    if start >= end:
        return "Value not found"

    middle = (start + end)//2

    if list[middle] == target:
        return middle

    elif list[middle] > target:
        return binary_search(list, target, start, middle)
    
    elif list[middle] < target:
        return binary_search(list, target, middle + 1, end)

values = [77, 80, 102, 123, 288, 300, 540]
target = 288
result = binary_search(values, target, 0, len(values))

if type(result) == int: print("element {0} is located at index {1}".format(target, result))
else: print(result)