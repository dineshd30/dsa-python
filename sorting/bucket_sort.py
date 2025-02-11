from typing import List

# Very efficient Unstable sorting algorithm and mostly not used because of special requirements
def bucket_sort(l:List[int]) -> List[int]: 
  counter = [0] * len(l)
  
  for i in range(len(l)):
    counter[l[i]] += 1
  
  j = 0
  for i in range(len(counter)):
    for x in range(counter[i]):
      l[j] = i
      j += 1
  
  return l


if __name__ == "__main__":
  input:List[int] = [5, 1, 3, 0, 2, 1]
  print(bucket_sort(input))