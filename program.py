from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import re
from string import punctuation
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
# sns.set()
from pylab import *

def word_processing(text):
    words = text.split()
    for word in words:
        if str(word).__contains__('http'):
            text = text.replace(word, '')
    return text

def processTweet(tweet):
        tweet = re.sub(r'\&\w*;', '', tweet)
        tweet = re.sub('@[^\s]+','',tweet)
        tweet = re.sub(r'\$\w*', '', tweet)
        tweet = tweet.lower()
        tweet = re.sub(r'https?:\/\/.*\/\w*', '', tweet)
        tweet = re.sub(r'#\w*', '', tweet)
        tweet = re.sub(r'[' + punctuation.replace('@', '') + ']+', ' ', tweet)
        tweet = re.sub(r'\b\w{1,2}\b', '', tweet)
        tweet = re.sub(r'\s\s+', ' ', tweet)
        tweet = tweet.lstrip(' ')
        tweet = ''.join(c for c in tweet if c <= '\uFFFF')
        return tweet

#Load data lalu dibersihkan
data = pd.read_csv("hasil_crawl.csv")
data = data.dropna()
colnames = ["id","text", "screen_name"]
data.columns = colnames
data["text"] = data["text"].apply(processTweet)
#save dataframe sebagai excel
data.to_excel("data_hasil_crawel.xlsx", index= False)


#Frequensi kata
#freq_word = pd.Series(' '.join(data['text']).split()).value_counts()
#df = pd.DataFrame(data = freq_word)
#df.to_excel("freq_kata.xlsx", index= True)
#print('berhasil diexport')

factory = StopWordRemoverFactory()
stopwords = factory.create_stop_word_remover()
removed_stopword = pd.Series(" ".join(data['text'].apply(stopwords.remove)).split()).value_counts()
dfs = pd.DataFrame(data = removed_stopword)
dfs.to_excel("freq_stopwords.xlsx")
print('berhasil diexport')
frekuensi_kata = pd.read_excel("freq_stopwords.xlsx")
frekuensi_kata.columns = ['screen_name', "freq"]

objects = frekuensi_kata['screen_name'].head(7)
y_pos = np.arange(len(objects))
performance = frekuensi_kata['freq'].head(7)

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('n')
plt.title('Kata yang sering muncul')
plt.show()
savefig("kata yang sering muncul.png")



#tweet duplicate (tidak ada yang duplikat)
data["is_duplicate"] =  data.duplicated()
data_not_duplicate = data.drop_duplicates(['text'])
print(data_not_duplicate)
_dd = pd.DataFrame( data = data[data["is_duplicate"] == True])
_dd.to_excel("tweet_duplicated.xlsx", index= False)

user_who_tweet_most = data['screen_name'].value_counts()
print(user_who_tweet_most)
df_user_whot_weet_most = pd.DataFrame( data = user_who_tweet_most)
df_user_whot_weet_most.to_excel("user_who_tweet_most.xlsx")
most_tweet_by_user = pd.read_excel("user_who_tweet_most.xlsx")
most_tweet_by_user.columns = ['screen_name', "n"]

t = most_tweet_by_user['screen_name'].head(5)
s = most_tweet_by_user['n'].head(5)
plot(t, s)

xlabel('screen_name')
ylabel('n')
title('User yang paling banyak ngetweet')
grid(True)
show()


#tampilkan semua tweet dari rasjawa lalu simpan ke to_excel
rasjawatweet = pd.DataFrame(data = data[data['screen_name'] == "rasjawa"])
rasjawatweet.to_excel("ras jawa tweet.xlsx")
