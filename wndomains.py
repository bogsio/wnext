from __future__ import print_function
from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import Synset
from collections import defaultdict
import os


class WNDomainsReader:
    """
    Corpus Reader for Wordnet Domains
    """
    RESOURCES_FOLDER = 'resources'
    DOMAINS_FOLDER = 'domains'

    def __init__(self, abspath=None):
        self.domain_dict = defaultdict(lambda: defaultdict(list))

        if abspath is None:
            file_folder = os.path.dirname(os.path.realpath(__file__))
            abspath = os.path.join(file_folder,
                self.__class__.RESOURCES_FOLDER,
                self.__class__.DOMAINS_FOLDER)

        domain_files = [f for f in os.listdir(abspath) if f.endswith('.ppv')]

        self.domains = []

        for idx, filename in enumerate(domain_files):
            domain_name, _ = filename.split('.')

            with open(os.path.join(abspath, filename), 'r') as df:
                for line in df:
                    synset_idx, relevancy = line.split()
                    relevancy = float(relevancy)
                    offset, pos = synset_idx.split('-')
                    offset = int(offset)

                    self.domain_dict[pos][offset].append((domain_name, relevancy))

            self.domains.append(domain_name)

    def synset(self, offset, pos=wn.NOUN):
        """
        Get domains of synset by offset and part of speech
        Returs list of tuples (domain, relevancy) sorted by relevancy
        """
        try:
            return sorted(self.domain_dict[str(pos)][offset], key=lambda item: -item[1])
        except:
            return None


def wordnetextensions_domains(self):
    """
    Method that decorates the Synset class, to get access to WordnetDomains
    """
    if not hasattr(self.__class__, 'wndomains_reader'):
        self.__class__.wndomains_reader = WNDomainsReader()

    return self.__class__.wndomains_reader.synset(self.offset(), self.pos())

# Decorate the Synset class with sentiment values from SentiWordnet
Synset.domains = wordnetextensions_domains


if __name__ == "__main__":
    submarine = wn.synset('submarine.n.01')
    print('TOP DOMAINS for submarine: ', submarine.domains()[:5], '\n')

    book = wn.synset('book.n.01')
    print('TOP DOMAINS for book: ', book.domains()[:5], '\n')

    algorithm = wn.synset('algorithm.n.01')
    print('TOP DOMAINS for algorithm: ', algorithm.domains()[:5], '\n')
