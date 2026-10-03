from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

print("Original Sequences :")
for sequence in sequences:
    print(sequence, "Lenght :", len(sequence))

print("All sequences are of diff lenght")

max_lenght = 4

padded_sequences = pad_sequences(
    sequences,
    maxlen = max_lenght,
    padding = "pre"
)

for sentence, sequence, padded in zip(sentences,sequences,padded_sequences):
    print("Sentence :",sentence)
    print("Original Sequence :",sequence)
    print("Padded sequence :",padded)
    print("-----------------------------------")
