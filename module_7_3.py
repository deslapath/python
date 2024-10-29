from pprint import pprint

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding="utf=8") as file:
                l = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    l = l.replace(j,'')
                    all_words[i] = l.split()
        return all_words

    def find(self, word):
        dict = {}
        for i, j in self.get_all_words().items():
            if word.lower() in j:
                dict[i] = j.index(word.lower())+1
        return dict

    def count(self, word):
        dict = {}
        for i, j in self.get_all_words().items():
            dict[i] = j.count(word.lower())
        return dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))







