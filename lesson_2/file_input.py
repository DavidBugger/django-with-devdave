# writing to a file 


with open('my_file.txt', 'w') as f:
    f.write("lorem ipsum dolor sit amet, consectetur adipiscing elit.\n")

# reading from a file
with open('my_file.txt', 'r') as f:
    content = f.read()
    print(content)