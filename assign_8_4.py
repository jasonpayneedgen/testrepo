unique = list()
fhand = open("romeo.txt")
for line in fhand:
  words = line.split()
  for word in words:
    if not word in unique:
        unique.append(word)
unique.sort()        
print(unique)
