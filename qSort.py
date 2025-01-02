import random


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def generate_random_array(length):
    return [random.randint(1, 100) for _ in range(length)]


def main():
    x = int(input("Write len mass: "))
    mass = generate_random_array(x)

    print("Original array:", mass)

    sorted_mass = quicksort(mass)
    print("Sorted array:", sorted_mass)


if __name__ == "__main__":
    main()
