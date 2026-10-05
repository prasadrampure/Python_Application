######################################
# Step 1 => Import required Libraries
######################################

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

###########################################
#   X_train : reviews used for traning
#   Y_train : Actual sentiments of traning
#   X_test  : Reviews used for testing
#   Y_test  : Actual sentiments of testing

# Sentiments :
# 0 -> Negative Sentiment
# 1 -> Positive Sentiment
###########################################

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

    print("-"*50)

######################################
# Step 8 => Padding 
######################################

X_train_padded = pad_sequences(
    X_train,
    maxlen = MAX_LENGHT
) 

X_test_padded = pad_sequences(
    X_test,
    maxlen = MAX_LENGHT
)

print("Training data shape :",X_train_padded.shape)
print("Testing data shape :",X_test_padded.shape)
print("-"*50)

######################################
# Step 9 => Create LSTM Model 
######################################

model = Sequential()

model.add( 
    Embedding(
        input_dim=VOCAB_SIZE,
        output_dim=32     # each word is represented in 32 values
    )
)

model.add(
    LSTM(
        units = 64,   # Size of LSTM hidden state
    )
)

model.add(
    Dense(
        units = 1,          # One output
        activation="sigmoid"    # used to produce probablity
    )
)

# Project Architecture

# Review -> Embeding -> LSTM -> Dence -> Sigmoid ->Positive/Negative

######################################
# Step 10 => Compile the model  
######################################

model.compile(
    optimizer = "adam",            # algorithem to update weights
    loss = "binary_crossentropy",  # Loss function
    metrics = ["accuracy"]         # measure classification accuracy
    )

print("Model Compiled Successfully")
print("-"*50)

######################################
# Step 11 => Train the model  
######################################

print("Model Traning")

model.fit(
    X_train_padded,         # Input traning reviews
    Y_train,                # Actual Sentiments labels
    epochs = 3,             # Complete dataset gets process 3 times
    batch_size = 64,        # Process 64 reviews in one batch
    validation_split = 0.2  # Use 20% training for vlidation
)

print("Model Training Gets Completed")
print("-"*50)

######################################
# Step 12 => Evaluate the model  
######################################

accuracy = model.evaluate(  
    X_test_padded,          # Testing Reviews
    Y_test,                 # Actual Testing labels
    verbose = 0             # Dont display the process
)

print("Testing Accuracy :",accuracy)
print("-"*50)

######################################
# Step 13 => Predict the review  
######################################

TEST_REVIEW_NUMBER = 0

original_review = X_test[TEST_REVIEW_NUMBER]
decoded_review = DecodeReview(original_review)

print("Review given to the model :")
print(decoded_review)

######################################
# Step 14 => get the actual sentiment  
######################################

actual_value = Y_test[TEST_REVIEW_NUMBER]

if actual_value == 1:
    actual_sentiment = "POSITIVE"
else:
    actual_sentiment = "NEGATIVE"

print("Actual Sentiment :",actual_sentiment)

######################################
# Step 15 => Predict the sentiment   
######################################

review_for_prediction = X_test_padded[TEST_REVIEW_NUMBER : TEST_REVIEW_NUMBER + 1]

prediction = model.predict(
    review_for_prediction,
    verbose = 0
)

probablity = prediction[0][0]

if probablity >= 0.5:
    predicted_sentiment = "POSITIVE"
else:
    predicted_sentiment = "NEGATIVE"

print("-"*50)

print("Final Result")

print("-"*50)

print("Prediction Probablity :",probablity)
print("Actual Sentiment :",actual_sentiment)
print("Predicted Sentiment :",predicted_sentiment)

print("-"*50)