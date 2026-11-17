library = { 101: {"title: "python", "author": "john", "copies": 5},
102:{"title": "java", "author": "james","copies": 3},
103: {"title": "c++", "author": "bjarne", "copies": 4}
}
book_id = 101
library[book_id] ["copies"] -= 1
print(library)