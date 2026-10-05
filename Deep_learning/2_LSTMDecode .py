# Step 1 => Import required Libraries

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

#####################################
# Step 2 => configuration of values
#####################################

VOCAB_SIZE = 10000    # consider most frequent 10000 unique words
MAX_LENGHT = 200      # consider maximum 200 wordsin review

#####################################
# Step 3 => Load the IMDB dataset
#####################################

print("-"*50)
print("Movie Review Sentiment Analysis using LSTM")
print("-"*50)

print("Loading the dataset")

(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words = VOCAB_SIZE)

print("IMDB dataset loaded successfully")

print("Number of Training Reviews :",len(X_train))
print("Number of Testing Reviews :",len(X_test))

######################################
#   X_train : reviews used for traning
#   Y_train : Actual sentiments of traning
#   X_test  : Reviews used for testing
#   Y_test  : Actual sentiments of testing
######################################

#####################################
# Step 4 => Load the word dictionary
#####################################

word_index = imdb.get_word_index()

# Dictonary contains mapping of word and its corresponding number
# Drisham is good movie    -> (20 56 78 43)
# 20  ->   Drisham
# 56  ->   is
# 78  ->   good
# 43  ->   movie

######################################
# Step 5 => Create reverse dictionary
######################################

reverse_word_index = {}

for word,index in word_index.items():
    reverse_word_index[index+3] = word

######################################
# Step 6 => Function to decode the review (number to word)
######################################

def DecodeReview(encoded_review):
    words = []

    for number in encoded_review:
        if number >= 3:  # ignore first 3
            word = reverse_word_index.get(number,"?")
            words.append(word)

    return " ".join(words)  # join the list of words

######################################
# Step 7 => Display sample revirws 
######################################

print("-"*50)
print("--------- Sample Reviews ---------")
print("-"*50)

for i in range(3,7):
    review = DecodeReview(X_train[i])

    print("-"*50)

    print("Review number :",i+1)
    print("Review :")
    print(review)

    print("-"*50)

    if Y_train[i] == 1:
        print("Sentiment : POSITIVE")
    else:
        print("Sentiment : NEGATIVE")
