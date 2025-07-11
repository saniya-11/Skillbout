
'''data = "my name is saniya"
f1 = data
f2 = f1.split(" ")
print("Words:", f2)
print("Number of words:", len(f2)) '''


with open("data.txt", "r") as file:
    f1 = file.read()
words = f1.split()
word_count = len(words)
print("Total number of words:", word_count)

