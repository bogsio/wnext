from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import Synset
from collections import defaultdict
import os


class GeoWordnetCorpusReader:
    """
    Corpus reader for GeoWN 3.1
    """
    RESOURCES_FOLDER = 'resources'
    GEOWORDNET_FILE = 'GeoWN_3.1.dat'

    def __init__(self, abspath=None):
        self.geowordnet = defaultdict(dict)

        if abspath is None:
            file_folder = os.path.dirname(os.path.realpath(__file__))
            abspath = os.path.join(file_folder,
                                   self.__class__.RESOURCES_FOLDER,
                                   self.__class__.GEOWORDNET_FILE)

        with open(abspath, 'r') as gwnf:
            for line in gwnf:
                if not line or line.startswith('#'):
                    continue

                chunks = line.split()
                try:
                    offset, geoname, lat, lon = chunks[:4]
                    self.geowordnet['n'][int(offset)] = (geoname, float(lat), float(lon))
                except ValueError:
                    continue

    def synset(self, offset):
        """
        Get sentiment of synset by offset and part of speech
        """
        try:
            return self.geowordnet['n'][offset]
        except:
            return None


def geowordnet_localize(self):
    """
    Method that decorates the Synset class, to get access to GeoWordnet
    Return tuple(Geonames_id, latitude, longitude)
    """
    if not hasattr(self.__class__, 'geowordnet_reader'):
        self.__class__.geowordnet_reader = GeoWordnetCorpusReader()

    return self.__class__.geowordnet_reader.synset(self.offset())

# Decorate the Synset class with localization data from GeoWordnet
Synset.geo = geowordnet_localize