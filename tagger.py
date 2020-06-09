
def readFile(fileName):
    f = open(fileName, "r", encoding="utf-8")
    return f.readlines()


def tagSentence(sentence, tag):
    return sentence.rstrip() + " " + tag + "\n"


if __name__ == "__main__":
    lines = readFile("./data_conv/nad-niemnem.txt")

    print(lines[0])
    print(tagSentence(lines[0], "xd"))
