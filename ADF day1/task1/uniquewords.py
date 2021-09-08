text_file = open('data.txt', 'r')
text = text_file.read()

#cleaning
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

#finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
#sorting of list
unique.sort()
#opening of text file in writing mode
textfile = open("output.txt", "w")
#appending the elements and its length
for element in unique:
    textfile.write(element + "  ")
    textfile.write(str(len(element)))
    textfile.write("\n")
textfile.close()
