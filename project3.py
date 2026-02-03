spam_words = ["win", "free", "prize"]

message = "you are winning a free prize now!"

def spam_filter(text, spam_list):
    text = text.lower()
    for word in spam_list:
        if word in text:
            return "spam"
    return "not spam"


result = spam_filter(message, spam_words)
print(result)