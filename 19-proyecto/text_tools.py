import os, re
from collections import Counter

def upload_file(file_path):
    # Upload a text file and return its content
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError( f"The file {file_path} doesn't exist." )
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print( f"❌ Error in {upload_file.__name__} function: {e}" )
        exit()

def analyze_text(text):
    # Analyze text and return key statistics
    lines = text.split('\n')
    words = re.findall(r'\b\w+\b', text)
    characters = len(text)

    words_frequency = dict(Counter(words))

    maxim = 0
    for i, j in words_frequency.items():
        if j > maxim:
            most_frequent_word = i
            maxim = j
    
    return {
        'Lines': len(lines),
        'Words': len(words),
        'Characters': characters,
        'Most frequent word': most_frequent_word,
    }

def search_replace(text, regex, replace_string):
    # Find a regex in text and replace with replace_string
    return re.sub(regex, replace_string, text)

def summary_generator(text):
    # Generate a summary of the text
    sentences = re.split(r'[.!?]', text)
    sentences = [sentence.strip() for sentence in sentences if sentence]

    words_frequency = dict(Counter(re.findall(r'\b\w+\b', text)))
    summary = sorted(
        sentences,
        key=lambda sentence: sum([words_frequency.get(word, 0) for word in sentence.split()]),
        reverse=True
    )

    # Get the 3 most relevant sentences
    return '. '.join(summary[:3])