# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# does the same thing as above
with open("/Users/Saleha/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
#IN DEXTOP LOCATIN IS WRITTEN WITH BACK SLASH BUT IN PYTHON IT USES FORWARD SLASH LIKE ABOVE
#IF USING BACKSLASH WRITE r"\LOCATION"


#what this does that it deletes all the content
# written in our text file and replaces it
# with the new text written under file.write
# with open("my_file.txt", mode="w") as file:
#      file.write("my fav kdrama is bloodhonds")

#it doesnt replaces the previous text
# but add the new one to the older one
with open("my_file.txt", mode="a") as file:
    file.write("\n and i like kim gyoen u")