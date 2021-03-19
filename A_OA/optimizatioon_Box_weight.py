def answer(arr):
  total = sum(arr)
  arr.sort()
  right_sum = 0
  res = []
  r = len(arr) - 1
  while right_sum < total:
    right_sum += arr[r]
    total -= arr[r]
    res.append(arr[r])
    r -= 1
return reversed(res)