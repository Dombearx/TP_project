import collections
from stempel import StempelStemmer
import re
from stop_words import get_stop_words
import pprint as pp
import os


class pieceOfData():

    def __init__(self, line, tag):
        self.line = line
        self.tag = tag
        self.words = []
        # self.vector = []

    def __repr__(self):
        return "line: " + self.line + " \ntag: " + self.tag + "\n" + "words: " + " ".join(self.words) + "\n"

    def __str__(self):
        return "line: " + self.line + " \ntag: " + self.tag + "\n" + "words: " + " ".join(self.words) + "\n"


def readFile(fileName):
    f = open(fileName, "r")
    return f.readlines()


def makeFile(lines, filename):
    f = open(filename, "w", encoding="utf-8")
    for line in lines:
        f.write(line)
    f.close()


if __name__ == "__main__":

    dir_path = os.path.dirname(os.path.realpath(__file__))
    readed = readFile(dir_path+"\\data_tagged\\nad_niemniem_lines.txt")

    lines = [line.strip()[:-1].strip().lower() for line in readed]

    # for l in lines:
    #     print(l+"\n")

    tags = [line.strip()[-1].strip() for line in readed]

    # for l in tags:
    #     print(l+"\n")

    data = [pieceOfData(line, tag) for line, tag in zip(lines, tags)]

    punctuationMarks = [".", ";", ":", "!", ",", "\"", "?", "-", "—"]

    # print(data[0])

    for mark in punctuationMarks:
        for piece in data:
            piece.line = piece.line.replace(mark, "")
            piece.line = piece.line.strip()
            piece.line = re.sub(' +', ' ', piece.line)


    picesToRemove = []
    for index, piece in enumerate(data):
        if(piece.line == ""):
            picesToRemove.append(index)

    for index in reversed(picesToRemove):
        del data[index]
        print("removing", index)


    for piece in data:
        piece.words = piece.line.split(" ")

    # usuwanie stop-words
    stop_words = get_stop_words('pl') # dodać "i" "z" !!!  zmienić zbiór stop words?
    # print(stop_words)
    for stop_word in stop_words:
        for piece in data:
            if stop_word in piece.words:
                piece.words.remove(stop_word)

    # lematyzacja
    stemmer = StempelStemmer.polimorf()
    for piece in data:
        piece.words = [stemmer.stem(word) for word in piece.words]

    # count = 0
    # for piece in data:
    #     for word in piece.words: count += 1
    # print("liczba słów: ",count)

    # usuwanie stop-words drugi raz
    stop_words = get_stop_words('pl') 
    # print(stop_words)
    for stop_word in stop_words:
        for piece in data:
            if stop_word in piece.words:
                piece.words.remove(stop_word)

    # count = 0
    # for piece in data:
    #     for word in piece.words: count += 1
    # print("liczba słów: ",count)

    num = 0
    for d in data:
        num += 1
        l = len(str(num))
        zeros = "0"*(5-l)
        name = str(d.tag) + zeros + str(num) + ".txt"

        if len(d.words) > 0: # utworzył się plik, który był pusty, więc to dodałem

            # usuwanie None - wersja wstępna
            for w in d.words:
                if w is None: 
                    d.words.remove(w)

            try:
                makeFile(" ".join(d.words), dir_path+"\\training_set\\"+str(d.tag)+"\\"+name)
            except:
                print("num: "+ str(num))
                print("name: "+ str(d.tag) + zeros + str(num) + ".txt")
                print("line: "+d.line)
                print("tag: "+d.tag)
                print("words: ")
                print(d.words)

        if num % 100 == 0: print("postęp: "+str(num)+"\n")
        
    print("\nfinish\n")

    # bagOfWords = {}

    # for piece in data:
    #     for word in piece.words:
    #         if word == None:
    #             continue
    #         if word not in bagOfWords:
    #             bagOfWords[word] = 1
    #         else:
    #             bagOfWords[word] += 1

    # listOfWords = list(bagOfWords.keys())

    # assert len(listOfWords) == len(bagOfWords)

    # for piece in data:
    #     for word in listOfWords:
    #         piece.vector.append(piece.words.count(word))

    # vectors = []
    # for piece in data:
    #     vectors.append("".join(map(str, piece.vector)))

    # makeFile(vectors, "vectorized_data2.txt")

    # makeFile(listOfWords, "bagOfWords2.txt")
