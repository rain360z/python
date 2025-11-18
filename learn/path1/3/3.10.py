rivers = []

print("Вывод пустого динамического списка рек")
print(rivers)

rivers.append('volga')

print(rivers[0].title())

rivers.append('the Nile')
rivers.insert(0, 'Oka')

print(rivers)

rivers.append('Obi')

print (rivers)

deleteriver = rivers.pop()

print(rivers)

rivers.append("Ob")

print(rivers)

rivers.remove('the Nile')

print(sorted(rivers))
print(rivers)
rivers.sort()
print(rivers)
print(len(rivers))



