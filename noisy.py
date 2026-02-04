import nltk
from nltk.corpus import words
from collections import Counter

word_counts={
    "the":5000,
    "tea":2000,
    "team":1000,
    "ten":200
}
summ = sum(word_counts.values())
print(summ)
def edit_distance(wrong_input,w):
    #likelihood --> how likely that particular word
    distance = nltk.edit_distance(w,wrong_input)
    if distance == 0: return 1.0
    return 1/(10**distance)

def prior_probability(w):
    #prior_probability --> repeated words in training model
    return word_counts.get(w,0)/summ


def suggested(wrong_input):
    candidates = list(word_counts.keys())
    correct_word = None
    high_prob = -1
    for w in candidates:
        likelihood = edit_distance(wrong_input, w)
        prior = prior_probability(w)
        result = likelihood * prior
        if result > high_prob:
            high_prob = result
            correct_word = w
    return correct_word

wrong_input = "teama"
correction = suggested(wrong_input)
print(correction)