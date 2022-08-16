def binary_search(list, target):
    if len(list) == 0:
        return "value not found"

    middle = len(list) // 2

    if list[middle] == target:
        return middle
    
    elif list[middle] > target:
        return binary_search(list[:middle], target)
    
    elif list[middle] < target:
        result = binary_search(list[middle + 1:], target)
        if type(result) == str:
            return result
        return result + middle + 1

    



sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 15))