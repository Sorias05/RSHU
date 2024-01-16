translation = str.maketrans({'*': '&', '&': '*'})

with open("input.txt", "r") as input, open("output.txt", "w") as output:
    for line in input:
        modified = line.translate(translation)
        output.write(modified)
