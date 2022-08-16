def binary_search(list, target):
  start = 0
  end = len(list)
  
  while start < end:
    middle = (start + end) // 2
    if list[middle] == target:
      return middle
    if target < list[middle]:
      end = middle
    if target > list[middle]:
      start = middle + 1
  
  return "Value not in list"

# test cases
print(binary_search([5,6,7,8,9], 9))
print(binary_search([5,6,7,8,9], 10))
print(binary_search([5,6,7,8,9], 8))
print(binary_search([5,6,7,8,9], 4))
print(binary_search([5,6,7,8,9], 6))