from typing import List


def merge_sort(l:List[int]) -> List[int]:
  length = len(l)
  
  if length <=1:
    return l
  
  mid = length // 2
  left = merge_sort(l[:mid])
  right = merge_sort(l[mid:])
  
  return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
  result = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  
  if len(left[i:]) > 0:
    result += left[i:]
  
  if len(right[j:]) > 0:
    result += right[j:]
  
  return result

if __name__ == "__main__":
  input:List[int] = [9, 1, 2, 8, 6, 4]
  print(merge_sort(input))