import random
books = ["Harry Potter", "Percy Jackson", "The Giver", "The House of the Scorpion", "To Kill a Mockingbird", "Naruto", "The Secret Garden"]
friends = ["James", "Jacob", "Adam", "Henry", "David", "John", "Ben"]
while len(books) != 0:
    b = random.choice(books)
    f = random.choice(friends)
    print(f"{b} is assigned to {f}.")
    books.remove(b)
    friends.remove(f)