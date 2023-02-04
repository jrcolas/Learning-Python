'''
Email providers
Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com

Below are steps specific to users sending email from Gmail addresses.

2. Make sure you've enabled less secure apps if you are sending from a Gmail account. (Refer to the video in the next lesson for steps).

3. Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha

4. Add a port number by changing your code to this:

smtplib.SMTP("smtp.gmail.com", port=587)

'''

# import smtplib
#
# my_email = "ljbo####@gmail.com"
# my_password = "kongertertklqasdrasdfsajfghgfdfsadftsasdasdkvvqadsadasdib"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="ljbo####@yahoo.com",
#         msg="Subject: Men Koze\n\nYo bruh what's up?"
#     )


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1944, month=12, day=16)
#
# print(date_of_birth)


# -------------------- Send a Quote Services, Inc. ------------------ #
import random
import datetime as dt
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/colasf/Coding/ENVs/.env")
my_email = os.getenv("EMAIL")
my_password = os.getenv("E_PASSWORD")


# Display the quote if the day to send is today
now = dt.datetime.now()
day_of_week = now.weekday()

# Send the quote by email to some homie
if day_of_week == 5:
    # Random Quote Selection
    with open("bdaywisher/quotes.txt", "r") as data:
        quote_list = data.readlines()

    random_quote = random.choice(quote_list).split("-")
    msg_body = f"{random_quote[0]}\n-{random_quote[1]}"
    print(msg_body)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=os.getenv("EMAIL"),
            msg=f"Subject: Your Weekly Thingy\n\n{msg_body}"
        )

else:
    print("It's not time to send it yet.")

