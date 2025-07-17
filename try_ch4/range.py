#for i in range(1,11):
 #   print(i)
numbers = list(range(1,21))
print(numbers)

cubes=[]
for number in range(1,11):
    cube = number**3
    cubes.append(cube)
print(cubes)

print(min(cubes))
print(max(cubes))
print(sum(cubes))
