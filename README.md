# Github Trends

The script finds 20 repositories created in the last week, selects the repositories with the largest number of stars, 
and for each count the number of open questions. And displays them along with the links.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3

python github_trending.py

dthree - mailit 1739 
7
Optional SMTP Auth https://api.github.com/repos/dthree/mailit/issues/9
No SMTP auth https://api.github.com/repos/dthree/mailit/issues/8
Greeting never received https://api.github.com/repos/dthree/mailit/issues/7
Does it support Self-signed certificates and CRAM-MD5 auth? https://api.github.com/repos/dthree/mailit/issues/6
Not reading from the config.json https://api.github.com/repos/dthree/mailit/issues/5
What have you used for interactive api docs? https://api.github.com/repos/dthree/mailit/issues/2
Does it support file attachments? https://api.github.com/repos/dthree/mailit/issues/1

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
