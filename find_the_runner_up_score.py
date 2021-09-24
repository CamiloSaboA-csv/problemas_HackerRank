n = int(input())
arr = map(int, input().split())

arr=sorted(set(arr))[-2]
print(arr)