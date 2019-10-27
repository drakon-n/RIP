item = [1, 2, 3, 4, 5]

print([(x, x*x) for x in item])
print(list(zip(item, [x*x for x in item])))
print(list(zip(item, (map(lambda x: x*x, item)))))
print(list(map(lambda x: (x, x*x), item)))