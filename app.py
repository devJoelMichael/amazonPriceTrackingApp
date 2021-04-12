import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Jujutsu-Kaisen-Vol-1/dp/1974710025/ref=sr_1_9?dchild=1&keywords=jujutsu+kasien+manga&qid=1618190609&sr=8-9'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}


def check_price():


page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[0:3])

if(converted_price < 5.00):
    send_mail()

print(converted_price)
print(title.strip())

if(converted_price < 5.00):
    send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mercybetweenvengeance@gmail.com', 'qlxpzjgjecxeazie')

    subject = 'Price fell down!'
    body = 'Check the amazon link: https://www.amazon.com/Jujutsu-Kaisen-Vol-1/dp/1974710025/ref=sr_1_9?dchild=1&keywords=jujutsu+kasien+manga&qid=1618190609&sr=8-9'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mercybetweenvengeance@gmail.com',
        'devjoelmichael@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60 * 60)
