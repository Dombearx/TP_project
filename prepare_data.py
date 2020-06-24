import collections
from stempel import StempelStemmer
import re
from stop_words import get_stop_words
import pprint as pp


class pieceOfData():

    def __init__(self, line, tag):
        self.line = line
        self.tag = tag
        self.words = []
        self.vector = []

    def __repr__(self):
        return "line: " + self.line + " tag: " + self.tag + "\n" + "words: " + " ".join(self.words) + "\n" + "vector: " + "".join(map(str, self.vector))

    def __str__(self):
        return "line: " + self.line + " tag: " + self.tag + "\n" + "words: " + " ".join(self.words) + "\n" + "vector: " + "".join(map(str, self.vector))


def readFile(fileName):
    f = open(fileName, "r")
    return f.readlines()


def makeFile(lines, filename):
    f = open(filename, "w")
    for line in lines:
        f.write(line + "\n")
    f.close()


if __name__ == "__main__":

    readed = readFile("./data_tagged/nad-niemnem.txt")

    lines = [line.strip()[:-1].strip().lower() for line in readed]

    tags = [line.strip()[-1].strip() for line in readed]

    data = [pieceOfData(line, tag) for line, tag in zip(lines, tags)]

    punctuationMarks = [".", ";", ":", "!", ",", "\"", "?"]

    print(data[0])

    for mark in punctuationMarks:
        for piece in data:
            piece.line = piece.line.replace(mark, "")
            piece.line = piece.line.strip()
            piece.line = re.sub(' +', ' ', piece.line)

    print(data[0])

    picesToRemove = []
    for index, piece in enumerate(data):
        if(piece.line == ""):
            picesToRemove.append(index)

    for index in reversed(picesToRemove):
        del data[index]
        print("removing", index)

    for piece in data:
        piece.words = piece.line.split(" ")

    stop_words = get_stop_words('pl')
    print(stop_words)
    for stop_word in stop_words:
        for piece in data:
            if stop_word in piece.words:
                piece.words.remove(stop_word)

    stemmer = StempelStemmer.polimorf()
    for piece in data:
        piece.words = [stemmer.stem(word) for word in piece.words]

    print(data[0])
    print(data[1])
    print(data[2])

    bagOfWords = {}

    for piece in data:
        for word in piece.words:
            if word == None:
                continue
            if word not in bagOfWords:
                bagOfWords[word] = 1
            else:
                bagOfWords[word] += 1

    listOfWords = list(bagOfWords.keys())

    assert len(listOfWords) == len(bagOfWords)

    for piece in data:
        for word in listOfWords:
            piece.vector.append(piece.words.count(word))

    vectors = []
    for piece in data:
        vectors.append("".join(map(str, piece.vector)))

    phrazes = []
    for piece in data:
        phrazes.append(" ".join(map(str, piece.words)))

    makeFile(phrazes, "lemmatized_data.txt")

    makeFile(vectors, "vectorized_data.txt")

    print(listOfWords[623])
    print(listOfWords[624])
    print(listOfWords[625])
    print(listOfWords[626])

    makeFile(listOfWords, "bagOfWords.txt")
