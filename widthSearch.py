from collections import deque

graph = {
    "blebe": ["Bob", "Alice", "Clar"],
    "Bob": ["Anugj", "Page"],
    "Alice": ["Page"],
    "Clar": ["Tom", "Jonny"],
    "Anugj": [],
    "Page": [],
    "Tom": [],
    "Jonny": []
}


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    if name not in graph:
        print("Person not in graph.")
        return False

    search_deque = deque()
    search_deque += graph[name]
    searched = set()

    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " seller mango")
                return person
            else:
                search_deque += graph[person]
                searched.add(person)
    print("No seller found.")
    return False

search("blebe")
