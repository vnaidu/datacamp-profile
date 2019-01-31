import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def dl_profile(user):
    url = "https://www.datacamp.com/profile/" + user
    page = requests.get(url)
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def parse_topics(soup, criteria=None):
    if criteria is None:
        criteria = 'xp >= 0'

    return pd.DataFrame(
        columns=['topic', 'xp'],
        data=[(t[0], int(t[1].split()[0]))
            for t in [topic.get_text().strip().split('\n')
                for topic in soup.find_all(
                    class_='topic-block__content')]]
    ).set_index('topic').query(criteria)


def parse_tracks(soup):
    df = (pd.DataFrame(
        columns=['track', 'description', 'badge_url'],
        data=[((track
                .find(class_='track-block__main')
                .get_text()
                .replace('\n', '')
                .strip()),
               (track
                .find(class_='track-block__description')
                .get_text()
                .replace('\n', '')
                .strip()),
               (track
                .img
                .get('src')))
              for track in soup.find_all(
                  class_=['profile-tracks', 'track-block'])]))
    return (df
            .drop_duplicates()
            .assign(
                track_id=df.badge_url.str.split('\/').str.get(5),
                cert_id=df.badge_url.str.split('?').str.get(-1),
                badge_url=df.badge_url.str.split('?').str.get(0),
                badge_filename=df.badge_url.str.split('\/').str.get(-1))
            .set_index('track_id'))
