from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import io
import sys


def getUrl():
    urls = []
    for i in range(1,3):
        url = 'https://movie.douban.com/subject/6874741/comments?start=%s&limit=20&sort=new_score&status=P&percent_type=' %(i*20)
        urls.append(url)
    return urls
def getComment():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers = {"User-Agent": user_agent}
    # f = open('movie.txt', 'w')
    # f.write('name        lookconditions       rating       looktimes           comments')
    # f.write('\n')
    # csvfile = open("movie.csv", 'w',newline='')
    # spamwriter = csv.writer(csvfile)
    # spamwriter.writerow(["commentname", "conditions", "rating", "lookdate", "comment"])
    for urlnum in range(len(getUrl())):
        try:
            comments = []
            response = requests.get(getUrl()[urlnum],headers=headers).text
            soup = BeautifulSoup(response,'html.parser')
            data = soup.find('div',class_ = 'mod-bd').find_all('div',class_='comment-item')
            for datanum in range(len(data)):
                # print(datanum)
                comment=[]


                commentname = data[datanum].find_all('span',class_='comment-info')[0].find('a').text
                conditions = data[datanum].find_all('span',class_='comment-info')[0].find_all('span')[0].string
                rating = data[datanum].find_all('span',class_='comment-info')[0].find_all('span')[1]["title"]
                lookdate = data[datanum].find_all('span',class_='comment-info')[0].find_all('span')[2]["title"]
                commention = data[datanum].find_all('p')[0].string
                # comments.append(commentname+','+conditions+','+rating+','+lookdate+','+comment)
                comment.append(commentname)
                comment.append(conditions)
                comment.append(rating)
                comment.append(lookdate)
                comment.append(commention)
                comments.append(comment)
                # spamwriter.writerow(comments[-1])


                # f.write(comments[-1])

        except :
            continue
    # f.close()
    return comments


if __name__ == '__main__':
    print(getComment())