from nltk.corpus import wordnet as wn
import sentiwordnet
import wndomains
import geowordnet


def main():
    # Access Sentiwordnet Corpus
    able = wn.synset('able.a.01')
    print "Sentiment for: ", able, " -> ", able.sentiment()

    # Access eXtended WordNet Domains (XWND)
    book = wn.synset('book.n.01')
    print "Top 5 domains for:", book, " -> ", book.domains()[:5]

    # Access GeoWordnet Corpus
    washington = wn.synset('washington.n.01')
    print "Geo info for: ", washington, " -> ", washington.geo(), "[", washington.definition, "]"

if __name__ == "__main__":
    main()