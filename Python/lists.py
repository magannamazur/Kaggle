flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold," \
          "tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
print(type(flowers))
print(flowers)

# String into list
print(flowers.split(","))

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold",
                "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)

# The list has ten entries
print(len(flowers_list))

# Indexing
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])

# Slicing
print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

# Removing items
flowers_list.remove("bird of paradise")
print(flowers_list)

# Removing last item
flowers_list.pop()
print(flowers_list)

# Adding items
flowers_list.append("snapdragon")
print(flowers_list)

# Is pink primrose a flower?
print("pink primrose" in flowers_list)

# Lists are not just for strings
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
print("Total books sold in one week:", sum(hardcover_sales))
print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)
print("Sorted:", sorted(hardcover_sales))
print("Index of 128:",hardcover_sales.index(128))

# loop "for" in list
test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings]
print(test_liked)

# Switching lists
a = [1, 2, 3]
b = [3, 2, 1]
a, b = b, a
print(a,b)