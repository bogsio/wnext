from __future__ import print_function
from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import Synset
from collections import defaultdict
import os


class SentiWordnetCorpusReader:
    """
    Corpus Reader for SentiWordnet
    """
    RESOURCES_FOLDER = 'resources'
    SENTIWORDNET_FILE = 'SentiWordNet_3.0.0.txt'

    def __init__(self, abspath=None):
        self.sentiwordnet = defaultdict(dict)

        if abspath is None:
            file_folder = os.path.dirname(os.path.realpath(__file__))
            abspath = os.path.join(file_folder,
                self.__class__.RESOURCES_FOLDER,
                self.__class__.SENTIWORDNET_FILE)

        with open(abspath, 'r') as swnf:
            for line in swnf:
                if not line or line.startswith('#'):
                    continue

                chunks = line.split()
                try:
                    pos, offset, pos_score, neg_score = chunks[:4]
                    self.sentiwordnet[pos][int(offset)] = (float(pos_score), float(neg_score))
                except ValueError:
                    continue

    def synset(self, offset, pos=wn.NOUN):
        """
        Get sentiment of synset by offset and part of speech
        """
        try:
            return self.sentiwordnet[str(pos)][offset]
        except:
            return None


def sentiwordnet_sentiment(self):
    """
    Method that decorates the Synset class, to get access to SentiWordnet
    """
    if not hasattr(self.__class__, 'sentiwordnet_reader'):
        self.__class__.sentiwordnet_reader = SentiWordnetCorpusReader()

    return self.__class__.sentiwordnet_reader.synset(self.offset(), self.pos())

# Decorate the Synset class with sentiment values from SentiWordnet
Synset.sentiment = sentiwordnet_sentiment


if __name__ == "__main__":
    able = wn.synset('able.a.01')
    print(able.sentiment())

    dog = wn.synset('dog.n.01')
    print(dog.sentiment())
