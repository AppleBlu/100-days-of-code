sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words_from_sentence = sentence.split()

result = {word: len(word) for word in words_from_sentence}

"""Quicker way to do this is:
result = {word: len(word) for word in sentence.split()}"""

print(result)
