import csv

from utils import makeSentenceUppercase

with open('example.txt', 'r') as file:
    print(file)

sentence = input('write me a sentence: ')
print(makeSentenceUppercase(sentence))