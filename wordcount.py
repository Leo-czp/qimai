import re
import json


class sort:
    def __init__(self):
        pass

    def start(self):
        with open(r'data/test_data.json', 'r') as f:
            data = json.load(f)
        data = data['data']
        words = [i['1'] for i in data]
        pat = '[a-zA-Z]+'
        words_counts = {}
        for word in words:
            if word.isalpha():
                lst = re.findall(pat, word)
                for lword in lst:
                    word = word.strip(lword)
                    if lword not in words_counts:
                        words_counts[lword] = 1
                    else:
                        words_counts[lword] += 1

            for w in word:
                if w not in words_counts:
                    words_counts[w] = 1
                else:
                    words_counts[w] += 1
        for i in range(97,123):
            i = chr(i)
            del words_counts[i]
        del words_counts[' ']
        ls = sorted(words_counts.items(), key=lambda x: x[1], reverse=True)
        return ls

if __name__ == '__main__':
    print(sort().start())

