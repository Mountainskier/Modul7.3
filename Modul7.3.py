import string


class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words_list = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char in string.punctuation:
                        line = line.replace(char, "")
                    words_list.extend(line.split())
            all_words[file_name] = words_list
        return all_words

    def find(self, word):
        result = {}
        lower_word = word.lower()
        for file_name, words_list in self.all_words.items():
            if lower_word in words_list:
                result[file_name] = words_list.index(lower_word) + 1
        return result

    def count(self, word):
        result = {}
        lower_word = word.lower()
        for file_name, words_list in self.all_words.items():
            result[file_name] = words_list.count(lower_word)
        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('capTAIN'))
print(finder1.count('CAptaIN'))
