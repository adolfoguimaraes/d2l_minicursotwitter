import nltk

from unicodedata import normalize, category
from nltk.tokenize import regexp_tokenize
from collections import Counter, Set
from nltk.corpus import stopwords

from repeatreplacer import RepeatReplacer
from spellingreplacer import SpellingReplacer

from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures

import pytz

class Processing():

    def __init__(self):
        self.pattern = r'(https://[^"\' ]+|www.[^"\' ]+|http://[^"\' ]+|\w+|\@\w+|\#\w+)'
        self.portuguese_stops = stopwords.words(['portuguese'])

        self.users_cited = []
        self.links_appears = []
        self.hashtags = []


    def get_words(self, list_text):

        patterns = []
        all_tokens = []

        for text in list_text:
            text = text.lower()

            local_patterns = regexp_tokenize(text, self.pattern)

            patterns += local_patterns

            self.users_cited += [e for e in local_patterns if e[0] == '@']
            self.links_appears += [e for e in local_patterns if e[:4] == 'http']
            self.hashtags += [e for e in local_patterns if e[0] == '#']


            final_tokens = [e for e in local_patterns if e[:4] != 'http']
            final_tokens = [e for e in final_tokens if e[:4] != 'www.']
            final_tokens = [e for e in final_tokens if e[0] != '#']
            final_tokens = [e for e in final_tokens if e[0] != '@']

            all_tokens += final_tokens

        words = [word for word in all_tokens if word not in self.portuguese_stops]

        word_set = set(words)

        return words, word_set


    def correct_text(self, word_set):

        replacer_spelling = SpellingReplacer()
        replacer_repeat = RepeatReplacer()

        map_words = {}


        for word in word_set:
            new_word = replacer_repeat.replace(word)
            new_word = replacer_spelling.replace(new_word)

            map_words[word] = new_word

        return map_words

    def get_final_words(self, list_text, correct=True):

        words, word_set = self.get_words(list_text)

        if correct:
            map_words = self.correct_text(word_set)
            words_temp = [map_words[word] for word in words]
        else:
            words_temp = words

        words_temp = [word for word in words_temp if len(word) >= 3]

        final_words = []

        for word in words_temp:
            try:
                new_word = normalize('NFKD', word.lower()).encode('ASCII', 'ignore')
            except UnicodeEncodeError:
                new_word = normalize('NFKD', word.lower().decode('utf-8')).encode('ASCII', 'ignore')

            final_words.append(new_word)


        return final_words

    def get_frequence_terms(self, final_words, limit=None):

        frequence_terms = nltk.FreqDist(final_words)

        if limit:
            return frequence_terms.most_common(limit)
        else:
            return frequence_terms.most_common()


    def get_frequence_users(self, list_user, limit=50):
        frequence_users = nltk.FreqDist(list_user)

        return frequence_users.most_common(limit)


    def get_frequence_users_cited(self, limit=50):
        frequence_users_cited = nltk.FreqDist(self.users_cited)

        return frequence_users_cited.most_common(limit)

    def get_frequence_hashtags(self, limit=50):
        frequence_hashtags = nltk.FreqDist(self.hashtags)

        return frequence_hashtags.most_common(limit)

    def get_bigrams_trigrams(self, final_words, limit=10):

        bcf = BigramCollocationFinder.from_words(final_words)
        tcf = TrigramCollocationFinder.from_words(final_words)

        bcf.apply_freq_filter(3)
        tcf.apply_freq_filter(3)

        result_bi = bcf.nbest(BigramAssocMeasures.raw_freq, limit)
        result_tri = tcf.nbest(TrigramAssocMeasures.raw_freq, limit)

        return result_bi, result_tri