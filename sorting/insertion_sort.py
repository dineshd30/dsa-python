from typing import List

def insertion_sort(l: List[int]) -> List[int]:
  for i in range(1, len(l)):
    j = i -1
  
    while (j >= 0) and (l[j] > l[j+1]):
      temp = l[j+1]
      l[j+1] = l[j]
      l[j] = temp
      j -= 1
      
  return l


if __name__ == "__main__":
  input: List[int] = [5, 3, 2, 1]
  result = insertion_sort(input)
  print(result)