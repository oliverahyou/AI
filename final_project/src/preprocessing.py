import re
import string
import emoji
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

slang_dict = {
    "ngl": "honestly", #tokenizing not gonna lie >>>'not gon na lie' then lemmmatizing would result in loss of information
    "tbh": "honestly",#similarly here, so a single word summary is used instead
    "imo": "opinion",
    "idk": "unknown"
}

def expand_slang(text):
    for word, replacement in slang_dict.items():
        text = re.sub(
            rf"\b{word}\b",
            replacement,
            text
        )
    return text

def clean_text(text):
    # Lowercasing
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove HTML
    text = re.sub(r"<.*?>", "", text)

    # Remove emojis
    text = emoji.replace_emoji(text, replace="")

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text




def preprocess_text(text):

    text = expand_slang(text)

    text = clean_text(text)

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(tokens)