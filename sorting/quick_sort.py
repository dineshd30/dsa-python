from typing import List

# Unstable sorting algorithm and most commonly used
def quick_sort(l:List[int], start:int, end:int) -> List[int]: 
  if end - start + 1 <=1:
    return l

  pivot = end # pivot value
  i = start   # pointer to iterate list
  j = i       # pointer to swap value
  while i < pivot:
    if l[i] <= l[pivot]:
      temp = l[j]
      l[j] = l[i]
      l[i] = temp
      j += 1
      
    i += 1
  
  # swamp pivot value at right place
  temp = l[j]
  l[j] = l[pivot]
  l[pivot] = temp
  
  quick_sort(l, start, j-1)
  quick_sort(l, j+1, end)
  
  return l


if __name__ == "__main__":
  input:List[int] = [9, 8, 7, 4, 5, 3, 2, 1, 0]
  print(quick_sort(input, 0, len(input) - 1))