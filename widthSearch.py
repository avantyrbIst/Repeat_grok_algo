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

def search(start_name):
    if start_name not in graph:
        print(f"{start_name} not in graph.")
        return False
    search_deque = deque(graph[start_name])
    searched = set()

    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a seller of mango.")
                return person
            else:
                search_deque += graph[person]
                searched.add(person)

    print("No seller found.")
    return False

search("blebe")
