import random
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

x = int(input("Write len mass: "))
mass = []
for i in range(x):
    mass.append(random.randint(1, 100))

print(mass)

print(quicksort(mass))