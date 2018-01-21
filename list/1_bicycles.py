# список
bicycles = ['mongoose', 'track', 'gt']
print(bicycles)

# первый элемент
print(bicycles[0])
# последний элемент
print(bicycles[-1])

# переопределение элемента
bicycles[0] = 'stern'

# добавление нового элемента в конец
bicycles.append('cannondale')

# добавление элемента на место
bicycles.insert(0, 'turbo')

# удаление элемента
del bicycles[0]

# работа с удаленным элементом
poped_bicycles = bicycles.pop()
# or
poped_this_bicycles = bicycles.pop(0)

# удаление из списка по значению
bicycles.remove('turbo')
