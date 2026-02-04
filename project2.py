import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

sentence = "The quick,Brown foxes...\n    they are JUMPING over\n    10 lazy dogs!"

sentence = sentence.lower()

sentence = re.sub(r'[^a-z\s]', ' ', sentence)

words = sentence.split()

stop_words = set(stopwords.words('english'))
words = [word for word in words if word not in stop_words]

lemmatizer = WordNetLemmatizer()
clean_words = [lemmatizer.lemmatize(word) for word in words]

print(clean_words)