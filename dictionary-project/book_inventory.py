# Problem: Manage a bookstore's inventory.

# ✅ Create a dictionary books with 3 book names as keys and number of copies available as values.
books = {
    "novel" : 2,
    "comics" : 5,
    "autobiography": 9
}
# ✅ A book is sold, reduce its quantity.
books.update({"autobiography": 4})
# ✅ New book arrives, add it.
books["crimes"] = 3
# ✅ A book goes out of stock, remove it.
books.pop("novel")
# ✅ Print updated inventory.
print(f"the available books in inventory are : {books}")