import re
import sys

def tokenize(text):
    tokens = []
    word_regex = re.compile(r"\b\w+('\w+)?\b")
    matchs = re.finditer(word_regex, text)
    for match in matchs:
        word = match.group(0)
        pos = word.find("'")
        if pos != -1:
            tokens.append(word[:pos])
            tokens.append(word[pos+1:])
        else:
            tokens.append(word)
    return tokens

def filter_sort(words, prefix):
    filter_set = set()
    for word in words:
        if word.startswith(prefix):
            filter_set.add(word)
    return sorted(filter_set)

def main():
    input = sys.stdin.read
    data = input().split('\n')

    text = data[0]
    prefix = data[1]

    words = tokenize(text)
    result = filter_sort(words, prefix)

    if not result:
        print(prefix)
    else:
        print(result)

if __name__ == '__main__':
    main()