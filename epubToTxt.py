from epub_conversion.utils import open_book, convert_epub_to_lines, convert_lines_to_text

book = open_book("data/nad-niemnem.epub")

lines = convert_epub_to_lines(book)

print(len(lines))

print(lines[6])

#max = 24
#min = 7
converted = []
for line in lines[7:25]:
    converted.append(convert_lines_to_text(line))

f = open("./data_conv/nad-niemnem.txt", "w")

x = 0
for conv in converted:
    print(x)
    x += 1
    for line in conv:
        f.write(line)
f.close()
