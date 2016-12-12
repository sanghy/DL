from __future__ import print_function
import numpy as np

from keras.datasets import mnist
from keras.models import Sequential
# from keras.initializations import norRemal, identity
from keras.layers.recurrent import SimpleRNN, LSTM, GRU
from keras.optimizers import RMSprop, Adadelta
from keras.layers.convolutional import Convolution2D,MaxPooling2D
from keras.layers.core import Dense, Activation, TimeDistributedDense, Dropout, Reshape, Flatten,RepeatVector,Merge
from keras.layers import Embedding
from keras.layers.wrappers import TimeDistributed
from keras.models import model_from_json
from data import load_data,load_datateststr
import vocabulary as vocabulary
import numpy
import sys



max_caption_len = 9
vocab_size = 82

# first, let's define an image model that
# will encode pictures into 128-dimensional vectors.
# it should be initialized with pre-trained weights.
image_model = Sequential()
image_model.add(Convolution2D(32, 3, 3, border_mode='valid', input_shape=(1, 50, 200)))
image_model.add(Activation('relu'))
image_model.add(Convolution2D(32, 3, 3))
image_model.add(Activation('relu'))
image_model.add(MaxPooling2D(pool_size=(2, 2)))

image_model.add(Convolution2D(64, 3, 3, border_mode='valid'))
image_model.add(Activation('relu'))
image_model.add(Convolution2D(64, 3, 3))
image_model.add(Activation('relu'))
image_model.add(MaxPooling2D(pool_size=(2, 2)))

image_model.add(Flatten())
image_model.add(Dense(128))

# let's load the weights from a save file.
#image_model.load_weights('weight_file.h5')

# next, let's define a RNN model that encodes sequences of words
# into sequences of 128-dimensional word vectors.
language_model = Sequential()
language_model.add(Embedding(vocab_size, 256, input_length=max_caption_len))
language_model.add(GRU(output_dim=128, return_sequences=True))
# language_model.add(Dense(128))

# let's repeat the image vector to turn it into a sequence.
image_model.add(RepeatVector(max_caption_len))

# the output of both models will be tensors of shape (samples, max_caption_len, 128).
# let's concatenate these 2 vector sequences.
model = Sequential()
model.add(Merge([image_model, language_model], mode='concat', concat_axis=-1))
# let's encode this vector sequence into a single vector
model.add(GRU(256, 256, return_sequences=False))
# which will be used to compute a probability
# distribution over what the next word in the caption should be!
model.add(Dense(vocab_size))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop')


(X_train_raw, y_train_temp)=load_datateststr()
(X_test_raw, y_test_temp) = load_datateststr()
partial_captions=numpy.zeros(len(y_train_temp),dtype=numpy.int32)
next_words=numpy.zeros(len(X_train_raw),dtype=numpy.float)
for i in y_test_temp:
    caption_char=y_test_temp[i]
    caption_ids = numpy.zeros(9, dtype=numpy.int32)
    next_w=numpy.zeros(82,dtype=numpy.float)


    for j,char in enumerate(caption_char):
        CHAR_VOCABULARY, CHARS = vocabulary.GetCharacterVocabulary(sys.argv[2])
        caption_ids[j] = CHAR_VOCABULARY[char]
        next_w[CHAR_VOCABULARY[char]]=1

    partial_captions[i]=caption_ids
    next_words[i]=next_w

images=X_train_raw

# "images" is a numpy float array of shape (nb_samples, nb_channels=3, width, height).
# "captions" is a numpy integer array of shape (nb_samples, max_caption_len)
# containing word index sequences representing partial captions.
# "next_words" is a numpy float array of shape (nb_samples, vocab_size)
# containing a categorical encoding (0s and 1s) of the next word in the corresponding
# partial caption.
model.fit([images, partial_captions], next_words, batch_size=16, nb_epoch=100)