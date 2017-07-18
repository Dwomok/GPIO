from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(17)
button = Button(2)

#while True:
 #   led.on()
  #  sleep(1)
   # led.off()
   # sleep(1)
button.when_pressed = led.on
#while button.when_pressed = led.on
#	exec MARGARET 
button.when_released = led.off

pause()
