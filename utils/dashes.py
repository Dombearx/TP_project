f = open(".//data_tagged//nad_niemniem_lines.txt", "r")

lines = f.readlines()

print(len(lines[216]))

converted = [line for line in lines if len(line) > 3]

f.close()
f = open(".//data_tagged//nad_niemniem_lines.txt", "w")
f.writelines(converted)
