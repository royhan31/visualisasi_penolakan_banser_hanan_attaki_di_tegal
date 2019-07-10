import tweepy
import time
import pandas as panda
from twitter import Twitter
import itertools

import csv
API = Twitter().instance()
waitQuery = 100
waitTime = 2.0
engineBlow = 1
csvFile = open('hasil_crawl.csv', 'w', encoding='utf-8')
csvWriter = csv.writer(csvFile)

def search() :
    global API, waitQuery, waitTime, engineBlow
    query = str(input("Search something : "))
    total_number = int(input("n : "))
    cursor = tweepy.Cursor(API.search, query + " -RT", tweet_mode = "extended",lang = "id").items()
    count = 0
    error = 0
    secondcount = 0
    idvalues = [0] * total_number
    while secondcount < total_number:
        try:
            c = next(cursor)
            count += 1
            if count % waitQuery == 0:
                time.sleep(waitTime)
        except tweepy.TweepError:
            print("Sleeping...")
            time.sleep(60 * engineBlow)
            c = next(cursor)
        except StopIteration:
            break

        try:
            text_val = c._json['full_text']
            text_val = str(text_val).lower()
            screen_name = c.user.screen_name


            if "rt" not in text_val:
                if len(text_val) != 0:
                    secondcount += 1
                    csvWriter.writerow([secondcount,str(text_val),str(screen_name)])
                    print("[INFO] Getting a tweet : " + str(secondcount) + " = " + text_val)
        except Exception as e:
            error += 1
            print('[EXCEPTION] Stream data: ' + str(e))


def paginate(iterable, page_size):
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (itertools.islice(i1, page_size, None),
                list(itertools.islice(i2, page_size)))
        if len(page) == 0:
            break
        yield page

search()
