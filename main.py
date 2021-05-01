# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2021 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333

import sys
import requests
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = re.findall(r"https://github.com/(.*?)'", sys.argv[1])[0]
    response = requests.get("https://github.com/" + url)
    soup = BeautifulSoup(response.text, features='lxml')
    fork_path = soup.find('span', {'class': 'text-small lh-condensed-ultra no-wrap mt-1'}).text.strip()
    sys.exit(0 if 'forked from SDUOJ-Team/hw-githubRepoForkAndIssue' in fork_path else -1)



