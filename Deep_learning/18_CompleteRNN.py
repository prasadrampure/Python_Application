import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Step 1 => Load the data

train_sentences = [
    "food was good",
    "food was bad",
    "food was excellent",
    "food was terrible",
    "service was good",
    "service was bad",
    "service was excellent",
    "service was terrible",
    "ambience was good",
    "ambience was bad",
    "ambience was excellent",
    "ambience was terrible"
]

train_labels = [
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0
]

# Step 2 : Tokenization

tokenizer = Tokenizer(oov_token = "<OOV>")

tokenizer.fit_on_texts(train_sentences)

# Step 3 : Convert training data into sequence

train_sequence = tokenizer.text_to_sequences(train_sentences)

print("Traing sequences :")

for sentance, sequence in zip(train_sentences,train_sentences):
    print(sentance, " -> ", sequence)


