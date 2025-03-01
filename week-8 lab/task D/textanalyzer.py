import re
from collections import Counter

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(r'\b\w+\b', text.lower())
        self.sentences = re.split(r'[.!?]', text)

    def get_word_count(self):
        return len(self.words)

    def get_sentence_count(self):
        return len([s for s in self.sentences if s.strip()])

    def get_average_word_length(self):
        if not self.words:
            return 0
        return sum(len(word) for word in self.words) / len(self.words)

    def get_top_words(self, n):
        word_counts = Counter(self.words)
        return word_counts.most_common(n)