from bs4 import BeautifulSoup
import urllib2
import sched, time
import random


s = sched.scheduler(time.time, time.sleep)
def isDiploButtonLive():
    r = urllib2.urlopen('https://tickets.bijouboston.com/details/582331963ecd9a0d5762c761')
    soup = BeautifulSoup(r.read(), "html.parser")
    if "disabled" in str(soup.find_all(id="buy-tickets")[0]):
        print 'false'
    else:
        print 'true'
    sleep = random.randint(0, 5)
    s.enter(sleep, 1, isDiploButtonLive, ())

s.enter(5, 1, isDiploButtonLive, ())
s.run()


    # def periodicallyHit():

# print isDiploButtonLive()