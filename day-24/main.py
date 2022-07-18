with open("my_file.txt") as file: # By this there is no need to close the file
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="w") as file:
#     file.write("New text.") #replaces everything, if file does not exist it creates
#
# with open("my_file.txt", mode="a") as file:
#     file.write("\n New text.")  # appends
#
# with open("/Users/hazalsenturk/new_file.txt", mode="w") as file:
#     file.write("New text.") #replaces everything, if file does not exist it creates

with open("../../my_file.txt") as file:
    contents = file.read()
    print(contents)

