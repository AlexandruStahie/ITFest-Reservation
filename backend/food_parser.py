import nltk
from nltk.corpus import wordnet as wn
from no_people import getWords

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

food = wn.synset('food.n.02')

typesOfFood = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

def get_prefferences(msg):
    words = getWords(msg)
    foodPreferences = []

    word = None

    for token in words:
        if token in typesOfFood:
            word = token

            try:
                nextWord = words[words.index(word) + 1]
            except:
                nextWord = None
            try:
                prevWord = words[words.index(word) - 1]
            except:
                prevWord = None

            try:
                option1 = prevWord + "" + word + "" + nextWord
                if option1 in typesOfFood:
                    word = option1
            except:
                pass

            try:
                option2 = prevWord + "_" + word
                if option2 in typesOfFood:
                    word = option2
            except:
                pass

            try:
                option3 = word + "_" + nextWord
                if option3 in typesOfFood:
                    word = option3
            except:
                pass

            if word != None and word not in foodPreferences:
                foodPreferences.append(word)

    return foodPreferences