from bs4 import BeautifulSoup
import urllib2
from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import TwilioRestClient
import sys

account_sid = # Your Account SID from www.twilio.com/console
auth_token  = # Your Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)

job = BlockingScheduler()

def isDiploButtonLive():
    r = urllib2.urlopen('https://tickets.bijouboston.com/details/582331963ecd9a0d5762c761')
    soup = BeautifulSoup(r.read(), "html.parser")
    if "disabled" in str(soup.find_all(id="buy-tickets")[0]):
        return False
    else:
        return True

@job.scheduled_job('cron', minute='10-20')
def timed_checker():
    phone_number = #Your phone number here
    twilio_number = #Your twilio number here
    if isDiploButtonLive():
        message = client.messages.create(body="Diplo tickets are live!!! GO BUY",
                                         to= phone_number, # Replace with your phone number
                                         from_= twilio_number)  # Replace with your Twilio number
    else:
        message = client.messages.create(body="Diplo tickets are not :(",
                                         to=phone_number,  # Replace with your phone number
                                         from_=twilio_number)  # Replace with your Twilio number

job.start()

