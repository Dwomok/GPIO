from gpiozero import LED,Button
from time import sleep
from signal import pause

led = LED(17)

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

def dot():
	led.on()
	sleep(1)
	led.off()
	sleep(1)

def dash():
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)

def A():
	dot()
	dash()

def M():
	dash()
	dot()
	dot()
	dot()
def S():
	dot()
	dash()
	

button = Button(2)

def name():
	S()
	A()
	M()

button.when_pressed = name
#utton.when_pressed = led.on
#utton.when_released = led.off

pause()


	
while True:
	i=6
	while i <6:
		dot()
		dash()
		





				
					
