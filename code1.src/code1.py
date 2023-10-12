def selectionSort_min(list):
  n = len(list)
  for i in range(n):
    min_idx = i
    for j in range(i+1, len(list)):
      if list[min_idx] > list[j]:
        min_idx = j
    list[i], list[min_idx] = list[min_idx], list[i]

list = [44, 15, 41, 26, 53, 11, 67]
print("원래 리스트 = %s" %list)
selectionSort_min(list)
print("최소값 중심 정리 방법을 이용한 오름차순 정렬")
print(list)
