numbers =list(range(1,11))
cubes=[]
print(numbers)
for cube in numbers:
    cubes.append(cube**3)
print(cubes)
for i in cubes:
    print(i)
    
cubes = [value**3 for value in range(1,31)]
print(cubes)
