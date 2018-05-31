#!/usr/bin/env python
import alphasign
import time

sign_device='/dev/ttyUSB0'

colors = ["RED", "GREEN", "AMBER", "RAINBOW_1", "RAINBOW_2", "COLOR_MIX", "AUTOCOLOR"]



#msg = "another sign"
#msg = raw_input()

msg_color = 'GREEN'
msg_mode = 'HOLD'
msg_font = 'SEVEN_HIGH_STD'

def reset_sign():
	msg = ""
	out_to_sign(msg, msg_color, msg_mode, msg_font)

#def getattrs(msg_color, msg_mode, msg_font):
#	color = getattr(alphasign.colors, msg_color)
#	mode = getattr(alphasign.modes, msg_mode)
#	font = getattr(alphasign.charsets, msg_font)
#	return (color, mode, font)

def colordemo():
	for color in colors:
		msg_color = color
		msg = color
		#getattrs(msg_color, msg_mode, msg_font)
		out_to_sign(msg, msg_color, msg_mode, msg_font)
		time.sleep(5)

def out_to_sign(msg, color, mode, font):
	#getattrs(msg_color, msg_mode, msg_font)
	color = getattr(alphasign.colors, color)
	mode = getattr(alphasign.modes, mode)
	font = getattr(alphasign.charsets, font)
	print msg, color, mode, font
	sign = alphasign.Serial(device=sign_device)
	sign.connect()
	text = alphasign.Text("%s%s%s" % (color, font, msg), label="A", mode=mode)
	sign.write(text)

def ask_for_input():
	msg = "Type your message"
	out_to_sign(msg, msg_color, msg_mode, msg_font)
	msg = raw_input()
	out_to_sign(msg, msg_color, msg_mode, msg_font)

def main():
	ask_for_input()
	colordemo()
	#reset_sign()

if __name__ == "__main__":
 	main()
