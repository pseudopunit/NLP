**Tokenize Words and Sentences with NLTK**
Tokenization is the process by which big quantity of text is divided into smaller parts called tokens.
These tokens are useful for finding such patterns as well as is considered as a base step for stemming and lemmatization.
**Tokenization of words**
"""

import nltk
nltk.download("popular")

from nltk.tokenize import word_tokenize
text = "Splitting words in a sentence using the word_tokenize function which is a wrapper function that calls tokenize on an instance of the TreebankWordTokenizer class."
print(word_tokenize(text))

"""**Tokenization of Sentences**"""

from nltk.tokenize import sent_tokenize
text = "Splitting sentences in the paragraph. The sent_tokenize function uses an instance of PunktSentenceTokenizer from the nltk.tokenize.punkt module, which is already been trained and thus very well knows to mark the end and beginning of sentence at what characters and punctuation."
print(sent_tokenize(text))

"""**StopWords**
> Stopwords are the words in any language which does not add much meaning to a sentence.
They can safely be ignored without sacrificing the meaning of the sentence. For some search engines, 
these are some of the most common, short function words, such as the, is, at, which, and on. In this case,
stop words can cause problems when searching for phrases that include them, particularly in names such as
“The Who” or “Take That”.
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

print(stopwords.words('english'))

# random sentecnce with lot of stop words
sample_text = "Oh man, this is pretty cool. We will do more such things."
text_tokens = word_tokenize(sample_text)

tokens_without_sw = [word for word in text_tokens if not word in stopwords.words('english')]

print(text_tokens)
print(tokens_without_sw)

"""**Stemming** 
> Stemming is basically removing the suffix from a word and reduce it to its root word.
For example: “Flying” is a word and its suffix is “ing”, if we remove “ing” from “Flying” then we will get base word or root word which is “Fly”.
"""

from nltk.stem.porter import *

porterStemmer = PorterStemmer()

sentence="I'm breakable; Unbreakable I'm shaking yet Unshakable Until the day that you find me I'll stand here Existing and feeling wretched existence Consuming life-force 'til I grow distant Don't bother searching for somebody like me A fading no one I don't want to hurt you, it's not my nature A monster born from dusk to dawn can't be your saviour Remember the 'me', the way I used to be"
wordList = nltk.word_tokenize(sentence)

stemWords = [porterStemmer.stem(word) for word in wordList]

print(' '.join(stemWords))

"""**Lemmatization**
 
Both in stemming and in lemmatization, we try to reduce a given word to its root word. The root word is called a stem in the stemming process, and it is called a lemma in the lemmatization process.
In lemmatization,the algorithms refer a dictionary to understand the meaning of the word before reducing it to its root word, or lemma.
"""

#lemmatize excluding verbs
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
punctuations="?:!.,;"
sentence_words = nltk.word_tokenize(sentence)
for word in sentence_words:
    if word in punctuations:
        sentence_words.remove(word)

sentence_words
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word)))

#lemmatize including verbs with pos_tag function
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
txt = """Resumption of the session I declare resumed the session of the European Parliament adjourned on Friday 17 December 1999 , and I would like once again to wish you a happy new year in the hope that you enjoyed a pleasant festive period ."""
[wnl.lemmatize(i,j[0].lower()) if j[0].lower() in ['a','n','v'] else wnl.lemmatize(i) for i,j in pos_tag(word_tokenize(txt))]
