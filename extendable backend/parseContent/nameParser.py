import nltk
from nltk.corpus import wordnet as wn

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

sample = "Hi my name is Anda. They are Mihai Despotovici and Alexandru Stahie and they are my colleagues. We would like some cornbread."

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

food = wn.synset('food.n.02')

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
print (set(entity_names))
typesOfFood = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

foodPreferences = []

for sentence in tokenized_sentences:
    for token in sentence:
        if token in typesOfFood:
            foodPreferences.append(token)

print(foodPreferences)
