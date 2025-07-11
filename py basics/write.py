with open("data.txt", "w") as file:
    file.write(input())


with open("data.txt", "r") as file:
    print(file.read())

with open("data.txt", "a") as file:
    print(file.write(input()))

with open("data.txt", "r") as file:
    print(file.read())

