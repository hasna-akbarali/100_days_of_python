import datetime
import requests
import smtplib
import time

MY_LAT = 12.971599
MY_LONG = 77.594566

email = 'hasna.akbarali98@gmail.com'
password = 'gfksyaueznlsksju'

''' Will send an email to youngasu123@gmail.com '''


def send_email():
    # Start the connection in order to communicate with emails
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # Transfer security protocol in case someone attempts to interrupt and reaed the email
        connection.starttls()

        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs='youngasu123@gmail.com',
                            msg=f"Subject:Look Up!\n\nThe Internation Space Station is passing above you!\nLook Up!")


''' Function will let us know if ISS is nearby and if its night time.'''

def should_lookup():
    """ Check if our location is nearby the current location of ISS """

    # Get the current position of ISS (latitude and longitude)
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # iss_position = longitude, latitude

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    # Check if ISS is near our location as we can view it only if its nearby
    is_nearby = (MY_LAT - 5 <= latitude <= MY_LAT + 5) and \
                (MY_LONG - 5 <= longitude <= MY_LONG + 5)

    ''' Check if its day or night only if its night we can see the  ISS '''
    # Get details of when the sunset and sunrise is in our current location
    response_for_sunrise_sunset = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response_for_sunrise_sunset.raise_for_status()
    data_for_rise_and_set = response_for_sunrise_sunset.json()['results']

    # Convert the time into 24 hour format, then extract only time
    sunrise = int(data_for_rise_and_set['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data_for_rise_and_set['sunset'].split('T')[1].split(':')[0])

    # Gets the current hour in our location
    now = datetime.datetime.now().hour

    is_day = (sunset < now < sunrise)

    # if its night and the ISS is nearby return True
    return is_day and is_nearby
print(should_lookup())


while True:
    time.sleep(60)

    if should_lookup():
        send_email()
