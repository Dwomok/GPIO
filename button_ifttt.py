button= Button

def ifttt():
       urllib2.urlopen("https://maker.ifttt.com/trigger/button_pressed/with/key/cutcLtxyGUU91QdDEBKCWF").read()


button.when_pressed = ifttt

pause()
