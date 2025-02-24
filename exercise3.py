# moveies=["one piece","dr.stone","Dandadan","Sakamoto Days","Tokyo Revengers"]
# print(movies[0])
# for movie

# movie.sort()
# print(movies)
# movies.append("mid up leveling")
# print(movies)
# movies.pop()
# print(movies)
# movies.remove("one piece")
# print(movies)
# movies.insert(1,"bleach")
# print(movies)
# movies[0:2]=["naruto"]
# print(movies)
# name="noah hagiwara"
# for letter in name:
#     print(letter)

groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]
print(groceries)
while True:
    ans=input("What do you want to remove?")
    if(ans=="stop"):
        break
    elif ans in groceries:
        groceries.remove(ans)
        print(groceries)
    else:
        print("NOT IN THE LIST!")