import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

def dl_profile(user):
    url = "https://www.datacamp.com/profile/" + user
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    return soup
