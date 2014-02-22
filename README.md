wnext
=====

Seemlessly add extensions to NLTK's Wordnet implementation.

```
# Access Sentiwordnet Corpus
>>> from nltk.corpus import wordnet as wn
>>> from wnext import sentiwordnet
>>> able = wn.synset('able.a.01')
>>> print able.sentiment()
(0.125, 0.0)

# Access eXtended WordNet Domains (XWND) 
>>> from wnext import wndomains
>>> book = wn.synset('book.n.01')
>>> book.domains()[:5]
[('roman_catholic', 0.00319282), ('publishing', 0.00285319), ('philology', 0.00133688), ('literature', 0.00092217), ('pedagogy', 0.000497682)]
```

Extensions
==========

* SentiWordNet is a lexical resource for opinion mining. SentiWordNet assigns to each synset of WordNet three sentiment scores: positivity, negativity, objectivity. [Sentiwordnet website](http://sentiwordnet.isti.cnr.it/ "SWN")
* XWND is an ongoing work aiming to automatically improve WordNet Domains. First, the original domain labels aligned to WordNet 1.6 have been projected to WordNet 3.0 using the automatic mappings across WordNet versions. [XWND website](http://adimen.si.ehu.es/web/XWND "XWND")


Licence
=======
SentiWordNet is distributed under the [Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) license](http://creativecommons.org/licenses/by-sa/3.0/ "ASA3.0") .

XWND is distributed under [Attribution 3.0 Unported (CC BY 3.0) license](http://creativecommons.org/licenses/by/3.0, "A3U").
