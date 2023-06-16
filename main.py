import string
import os
import sys


def main():
    dir = 'small'
    file1 = dir + '/' + '1.txt'
    file2 = dir + '/' + '2.txt'
    file3 = dir + '/' + '3.txt'
    #file1 = 'doc1.txt'
    #file2 = 'doc2.txt'

    index = {}
    file_titles = {}

    # term --> filename where de term exists
    # 'we'      --> ['doc1.txt']
    # 'stong'   --> ['doc1.txt','doc2.txt']


    create_index(file3, index, file_titles)

    create_index(file2, index, file_titles)

    create_index(file1, index, file_titles)
    print(index)

    print("File_titles\n", file_titles)


def create_index(filename, index, file_titles):
    with open(filename) as file:
        # open file to read
        first_line = file.readline()
        if filename not in file_titles:
            file_titles[filename] = first_line.strip()
        get_terms(first_line, filename, index)

        for line in file:
            get_terms(line, filename, index)


def get_terms(line, filename, index):
    words = line.split()
    for word in words:
        word = word.strip(string.punctuation)
        term = word.lower()
        if len(term) > 0:
            if term not in index:
                index[term] = [filename]
            else:
                if filename not in index[term]:
                    index[term].append(filename)


if __name__ == "__main__":
    main()