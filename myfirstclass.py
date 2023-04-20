
# My solution
class MyFirstClass:
    # Define string variable called index
    index = "Author-Book"    
    def __init__(self, philosopher, book) -> None:
        self.philosopher = philosopher
        self.book = book

    def hand_list(self):
        print(self.philosopher +  " wrote the book: "  + self.book)    
print(MyFirstClass.index)

whodunnit = MyFirstClass("Sun Tzu", "The Art of War")
whodunnit.hand_list()        

"""
# Sample Solution code
class MyFirstClass:
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")
"""