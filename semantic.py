import spacy

nlp = spacy.load('en_core_web_md')
print("Example 1")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("\n")

print("Example 2")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
"""
Its interesting that its that the several different associations between words has such an effect on similarity.
I expected high similarity of banana and apple but was surprised by the similarity between monkey and banana       
"""
print("\n")

print("Example 3")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
print("\n")


print("Own Example!")
fruit1 = nlp("orange")
fruit2 = nlp("lemon")
fruit3 = nlp("banana")
fruits = [fruit1, fruit2, fruit3]
for fruit in fruits:
    for fruit_2 in fruits:
        print(fruit.text, fruit_2.text, fruit.similarity(fruit_2))
"""
It's interesting that the similarity between the lemon and banana is greater than the lemon and orange and lemon. 
I expected the orange and lemon to be greater as they are both citrus fruits. 
"""