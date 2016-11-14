list = []
n = int(raw_input().strip())
ls = raw_input().strip()
list = ls.split()
list.sort()

list = [int(x) for x in list]
a = max(list)
while list[-1] == a:
    list.pop()
print list[-1]

