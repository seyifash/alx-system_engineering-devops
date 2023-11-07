#!/usr/bin/python3
"""get count"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """get total count of word present in the wordlist which are also present
    in the hot post
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
            subreddit, after)
    headers = {
        'User-Agent': 'YourBotName/1.0 (by YourUsername)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            tl = post['data']['title']
            tl = tl.lower()
            for word in word_list:
                word = word.lower()
                if word in tl:
                    counts[word] = counts.get(word, 0) + tl.count(word.lower())

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        pass
