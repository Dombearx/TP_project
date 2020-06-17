from sklearn import datasets
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
training_set = datasets.load_files(dir_path+"\\training_data", encoding="utf-8", random_state=420)



# import os
# dir_path = os.path.dirname(os.path.realpath(__file__))
# f = open(dir_path+"\\folder\\plik.txt")
# print(f.readline)
# f.close()

