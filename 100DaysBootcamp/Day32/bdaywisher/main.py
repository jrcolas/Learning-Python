import pandas
import random
import datetime as dt
import smtplib

USERNAME = "ljbo####@gmail.com"
PASSWORD = "crxxdlxxcnvyrmml"

search_text = "[NAME]"
birthdays = pandas.read_csv("birthdays.csv")
bd_df = birthdays.to_dict(orient="list")
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt", "letter_4.txt"]

# Date Stuff
now = dt.datetime.now()
month = now.month
day = now.day

for i in range(len(birthdays.name)):
    if birthdays.day[i] == day and birthdays.month[i] == month:
        # Opening letter
        with open(f"letter_templates/{random.choice(letters)}", "r") as letter_file:
            letter = letter_file.read()
            letter = letter.replace(search_text, birthdays.name[i])

        # Send the letter
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USERNAME,
                to_addrs=birthdays.email[i],
                msg=f"Subject: Happy Birthday Homie!\n\n{letter}"
            )



