import requests
import smtplib
from datetime import datetime
import time
time_now = datetime.now().hour

MY_LAT = 13.0843 #latitude
MY_LONG = 80.2705 #longitude


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #+5 pr -5
    if MY_LAT+5 <= iss_latitude <= MY_LAT-5 and MY_LONG+5 <= iss_latitude <= MY_LONG-5:
        return True



def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now >= sunset or time_now <= sunrise:
        return True

my_email = "lokispamzzzz@gmail.com"
passwd = "dnwmfvxpbhicuyjp"
while True:
    time.sleep(60)
    if is_night() and is_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwd)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="lokispamzzzz@gmail.com",
                msg="LOOK UP"
            )



