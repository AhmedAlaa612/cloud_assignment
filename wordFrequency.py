import nltk
from nltk.corpus import stopwords

def readParagraph(text):
    """Read a paragraph from a file and remove stopwords and return the paragraph as a string"""
    with open(text, 'r') as file:
        paragraph = file.read().replace('\n', ' ')
        stopWords = stopwords.words('english')
        paragraph = paragraph.lower()
        # remove punctuations
        paragraph = ''.join([char for char in paragraph if char.isalnum() or char == ' '])
        paragraph = ' '.join([word for word in paragraph.split() if word not in stopWords])
    return paragraph

def wordFrequency(paragraph):
    """Count the frequency of each word in a paragraph"""
    word_freq = {}
    for word in paragraph.split():
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

def main():
    nltk.download('stopwords')
    paragraph = readParagraph('paragraphs.txt')
    word_freq = wordFrequency(paragraph)
    for word in word_freq[:100]:
        print(word[0], ":", word[1])

if __name__ == '__main__':
    main()
