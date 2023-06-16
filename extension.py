"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so. For the server extension, write your code in
extension_server.py
"""
FILE_STOP_WORDS = 'stop_words_english.txt'  # from countwordsfree 850 entries
#FILE_STOP_WORDS = 'stop_words.txt'         # from github 127 entries


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """


    l_stop_words = list_stop_words(FILE_STOP_WORDS)
    #print (l_stop_words)
    print ( len(l_stop_words))

def list_stop_words(filename):
    # create a list of english stop words

    stop_words = []

    with open(filename) as file:
        # open file to read
        for line in file:
            line = line.strip()
            #print (line)
            stop_words.append(line)
    return stop_words


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
