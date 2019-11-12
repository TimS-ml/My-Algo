import time
import requests
import datetime
try:
    import cPickle as pickle
except:
    import pickle

from bs4 import BeautifulSoup


LOGIN = "jxueba@outlook.com"
PASSWD = "rfcpdq1995"
LOGIN_URL = "https://leetcode-cn.com/accounts/login/"


# def login(email, password):
#     client = requests.session()
#     client.encoding = "utf-8"

#     while True:
#         try:
#             client.get(sign_in_url, verify=False)
#             csrftoken = client.cookies['csrftoken']
#             login_data = {'login': email, 
#                 'password': password
#             }
#             result = client.post(sign_in_url, data=login_data, headers=dict(Referer=sign_in_url))
            
#             if result.ok:
#                 print ("Login successfully!")
#                 break
#         except:
#             print ("Login failed! Wait till next round!")
#             time.sleep(sleep_time)

#     return client


now = datetime.datetime.now()

session = requests.Session()
# Get cookies
session.get(LOGIN_URL)
# csrftoken = session.cookies['csrftoken']

login_data = {'login': LOGIN, 'password': PASSWD}
session.post("https://leetcode-cn.com/accounts/login/", data=login_data, headers=dict(Referer=LOGIN_URL))


def getSubmissionPage(pageNum):
    s = session.get("https://leetcode-cn.com/submissions/%d/" % (pageNum))
    soup = BeautifulSoup(s.text)

    table = soup.find('table')
    rows = table.find_all('tr')

    records = []
    for row in rows[1:]:
        cols = row.find_all('td')
        time = cols[0].text
        question = cols[1].text
        link = cols[1].find('a')['href']
        status = cols[2].text
        submission = cols[2].find('a')['href']
        runTime = cols[3].text
        language = cols[4].text
        record = [time, question, link, status, submission, runTime, language]
        record = map(lambda x: x.strip().replace(u'\xa0', u' '), record)
        records.append(record)
    return records


submissions = []
page = 1
while True:
    try:
        submissions += getSubmissionPage(page)
        page += 1
        print("Retrived page %d" % (page))
        # Adjust to whatever you like
        time.sleep(5)
    except AttributeError:
        # Reaches the end
        break

# Save "now" for calcualting the timestamp
# [u'2 years, 11 months ago', u'Two Sum', u'/problems/two-sum/', u'Accepted', u'/submissions/detail/xxxx/', u'40 ms', u'cpp']
pickle.dump((now, submissions), open("submissions.p", "wb"))
