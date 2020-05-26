import collections


def readFile(fileName):
    f = open(fileName, "r")
    return f.readlines()


if __name__ == "__main__":

    lines = readFile("./data_tagged/nad-niemnem.txt")

    tags = [line.strip()[-1].strip() for line in lines]

    counter = collections.Counter(tags)

    print(counter)
