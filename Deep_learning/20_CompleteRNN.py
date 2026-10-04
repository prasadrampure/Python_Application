import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
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

train_sequence = tokenizer.texts_to_sequences(train_sentences)

print("Traing sequences :")

for sentance, sequence in zip(train_sentences,train_sentences):
    print(sentance, " -> ", sequence)

# Step 4 => Apply padding

max_lenght = 4

X_train = pad_sequences(
    train_sequence,
    maxlen = max_lenght,
    padding = "pre"
)

Y_train = np.array(train_labels)

print("Padded training data")
print(X_train)

print("Traning labels :")
print(Y_train)

# Step 5 => Calculate vocabulary size

vocab_size = len(tokenizer.word_index) + 1
print("Vocabulary size is :",vocab_size)

# Step 6 => Bulid RNN model

model = Sequential()

model.add(
    Embedding(
        input_dim=vocab_size,
        output_dim=8,
        input_length=max_lenght
    )
)

model.add(
    SimpleRNN(
        units = 8,
        activation = "tanh",
    )
)

model.add(
    Dense(
        units=1,
        activation="sigmoid"
    )
)

# Step 7 => Compile the model

model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
)

# Step 8 => Display model

model.build(input_shape = (None, max_lenght))

print("Model architecture")
model.summary()

# Step 9 +> Train the model

history = model.fit(
    X_train,
    Y_train,
    epochs = 100,
    verbose = 1
)

print("Model training completed")

# Step 10 => Create unseen data

test_sentences = [
    "service was amazing",
    "service was horrible",
    "Experiance was excellent",
    "Experiance was terrible"
    ]

# Step 11 : convert text to sequence

test_sequences = tokenizer.texts_to_sequences(test_sentences)

X_test = pad_sequences(
    test_sequences,
    maxlen = max_lenght,
    padding = "pre"
)

# Step 12 => Predict the enstiment

for text, sequence, padded in zip(test_sentences, test_sequences, X_test):
    input_data = np.array([padded])

    prediction = model.predict(input_data,verbose = 0)

    probablity = float(prediction[0][0])

    print("Sentence :",text)
    print("Sequence :",sequence)
    print("Padded sequence :",padded)
    print("Prediction :",probablity)

    if probablity >= 0.5:
        print("Sentiment : Positive")
    else:
        print("Negative ")