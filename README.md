# Github Trends

The script finds 20 repositories created in the last week, selects the repositories with the largest number of stars, 
and for each count the number of open questions. And displays them along with the links.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3

python github_trending.py

Repository: {name}, owner: {owner} - has {stars} stars and {issues} open issues. URL: {url}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
