menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}
def add(item,price):
    menu[(item)]=price
    print(menu)
add(input("What item do you want?"),input("How much does it cost?"))