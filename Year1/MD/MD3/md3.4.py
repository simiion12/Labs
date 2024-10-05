import json
import nltk
from nltk import TweetTokenizer

class Twt:
    def __init__(self, text, likes, retweets, date):
        self.text, self.likes, self.retweets, self.date = text, likes, retweets, date


tt = TweetTokenizer()
special_chars = "1234567890.=?\",”$%^;&’*(…):!><"
special_chars_CSV = "1234567890.=?\",”;$%^&’*(…):@!>#@<"
words_tweet_tokenizer = []
words_per_tweet = {}
special_words = []
hashtags = []
wordsForCSV = []
checkedIDs = []
tod = {}
# Handles the tweet json, separates words into needed categories, and extracts hashtags
with open("C:\\Users\\Administrator\\Desktop\\psa3\\tweets.json", "r", encoding="utf-8") as tweetJson:
    tweetJsonData = json.load(tweetJson)
    for tweet in tweetJsonData:
        if tweet["id"] not in checkedIDs:
            tod[tweet["id"]] = Twt(tweet["text"], tweet["likes"], tweet["retweets"], tweet["created_at"][:7])
            checkedIDs.append(tweet["id"])
        tempAppend = []
        tempWords = tt.tokenize(tweet["text"])
        words_per_tweet[tweet["id"]] = tempWords
        for word in tempWords:
            if not any(c in special_chars for c in word) and len(word) > 1:
                words_tweet_tokenizer.append(word)
                if word[0] == '#':
                    hashtags.append(word)
            else:
                if len(word) > 1:
                    special_words.append(word)
            if not any(c in special_chars_CSV for c in word) and len(word) > 1:
                tempAppend.append(word)
        wordsForCSV.append(tempAppend)

# Counts hashtags and outputs the top
hashtag_dictionary = {x: 0 for x in hashtags}
for hashtag in hashtags:
    hashtag_dictionary[hashtag] += 1
hashtag_dictionary = dict(sorted(hashtag_dictionary.items(), key=lambda item: item[1], reverse=True))
print("===================")
print("Top 10 #hashtags:")
print("===================")
count = 0
for hashtag in hashtag_dictionary:
    if count < 10:
        print(hashtag, " ", hashtag_dictionary[hashtag])
    count += 1

# Analyzes each word
tweet_rated_emotion = {}
word_emotion_dict = {}
with open("C:\\Users\\Administrator\\Desktop\\psa3\\AFINN-111.txt", "r", encoding="utf-8") as AFINNdict:
    for line in AFINNdict:
        words = nltk.word_tokenize(line)
        nr = words[len(words) - 1]
        strn = ""
        for x in range(len(words) - 1):
            strn += words[x]
        word_emotion_dict[strn] = nr

for id in words_per_tweet:
    total_rating = 0
    for word in words_per_tweet[id]:
        if word.lower() in word_emotion_dict:
            total_rating += int(word_emotion_dict[word.lower()])
    tweet_rated_emotion[id] = total_rating

print("==========================")
print("Top 10 Positive :D Tweets:")
print("==========================")
tweet_rated_emotion = dict(sorted(tweet_rated_emotion.items(), key=lambda item: item[1], reverse=True))
count = 0
for tweet in tweet_rated_emotion:
    if count < 10:
        print(tod[tweet].text, " ", tweet_rated_emotion[tweet])
    count += 1
print("===========================")
print("Top 10 Negative >:D Tweets:")
print("===========================")
tweet_rated_emotion = dict(sorted(tweet_rated_emotion.items(), key=lambda item: item[1], reverse=False))
count = 0
for tweet in tweet_rated_emotion:
    if count < 10:
        print(tod[tweet].text, " ", tweet_rated_emotion[tweet])
    count += 1
print("=====================================")
print("All Tweets Rated by Emotional Damage:")
print("=====================================")
print(tweet_rated_emotion)

# Creates the CSV file
studentID = 23
startingPoint = studentID * int(200/7)
endingPoint = startingPoint + 200
graph_dict = {}
maxm = 0
for i in range(startingPoint, endingPoint):
    for x in wordsForCSV[i]:
        graph_dict[x] = []
filter_words = ["RT", "of", "it", "not", "but", "for", "are", "in", "my", "to", "by", "doing", "so"]
file = open("data.csv", "w", encoding="utf-8")
for i in range(startingPoint, endingPoint):
    for word in wordsForCSV[i]:
        for x in wordsForCSV[i]:
            if x is not word and x not in graph_dict[word] and x not in filter_words:
                graph_dict[word].append(x)
for x in graph_dict:
    for z in range(len(graph_dict[x])):
        if x not in filter_words:
            file.write(x + ",")
            file.write(graph_dict[x][z])
            if z != len(graph_dict[x]) - 1:
                file.write(",")
        file.write("\n")
    file.write("\n")