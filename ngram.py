from nltk import bigrams
from collections import Counter

text = "i Love Pizza i love cake i hate vegetables"
tokens = [t.lower() for t in text.split()]

bi_list = list(bigrams(tokens))
bi_count = Counter(bi_list)

res = {pair[1]: count for pair, count in bi_count.items() if pair[0] == 'i'}
print(res)  # -> {'love': 2, 'hate': 1}