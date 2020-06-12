#Create a new books array
#O(1)
books = []

#Add elements to array
#O(n)
books = ["Novels","textbooks","Exercise books",1,2,4]
#print(books)

#Array Methods
"""Append: Add element to end of list"""
""" O(1)"""

books.append("Notebooks")
#print(books)

"""Insert: Add element at given index"""
""" O(n)"""
books.insert(1,300)
print(books)

"""Delete"""
""" O(n)"""
del books[1]
print(books)

"""Loop through a list"""
""" O(n)"""
for i in books:
    print(i)

"""Len of a list"""
"""O(1)"""
print(len(books))

"""Membership"""
"""O(n)"""
print("Textbooks" in books)

"""Sort"""
numbers = [1,4,6,8,4,8]
numbers.sort()
print(numbers)

"""Concatenation"""
print(numbers+books)


"""Equality"""
print(numbers == numbers)


