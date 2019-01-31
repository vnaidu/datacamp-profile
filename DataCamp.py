import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def dl_profile(user):
    url = "https://www.datacamp.com/profile/" + user
    page = urlopen(url)
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