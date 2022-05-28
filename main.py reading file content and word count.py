# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from posixpath import split


def read_file_content(filename):
    f= open("story.txt", 'r')
    filename = f. read()
    return filename
print (read_file_content('filename'))

def count_words():
    text = read_file_content("\story. txt")
    words_of_text  = text. split()
    count = dict ()
    for word in words_of_text :
        if word in count:
            count [word] +=1
            count[word] =1
            return count

    
