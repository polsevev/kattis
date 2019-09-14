import time
import webbrowser
import random

while True:
    sites = random.choice(["pornhub.com", "youporn.com", "youtube.com", "google.com", "vg.no", "fronter.com"])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(30, 60)
    time.sleep(seconds)
