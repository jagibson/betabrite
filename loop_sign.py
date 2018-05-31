#!/usr/bin/env python
import alphasign
import time

sign_device='/dev/ttyUSB0'

colors = ["RED", "GREEN", "AMBER", "RAINBOW_1", "RAINBOW_2", "COLOR_MIX", "AUTOCOLOR"]
modes = ["ROTATE", "HOLD", "ROLL_UP", "ROLL_DOWN", "ROLL_LEFT", "ROLL_RIGHT", "WIPE_UP", "WIPE_DOWN", "WIPE_LEFT", "WIPE_RIGHT", "SCROLL", "ROLL_IN", "ROLL_OUT", "WIPE_IN", "WIPE_OUT", "TWINKLE", "SPARKLE", "SNOW", "INTERLOCK", "SWITCH", "SPRAY", "STARBURST", "WELCOME", "SLOT_MACHINE", "THANK_YOU", "NO_SMOKING", "DONT_DRINK_DRIVE", "RUNNING_ANIMAL", "FIREWORKS", "TURBO_CAR"]
fonts = ["FIVE_HIGH_STD", "SEVEN_HIGH_STD", "SEVEN_HIGH_FANCY"]

msg = "THIS IS A TEST"
msg_color = 'GREEN'
msg_mode = 'HOLD'
msg_font = 'SEVEN_HIGH_STD'

def reset_sign():
	msg = ""
	out_to_sign(msg, msg_color, msg_mode, msg_font)

def static_test():
	msg = "THIS IS A TEST"
	msg_color = 'GREEN'
	msg_mode = 'SLOT_MACHINE'
	msg_font = 'SEVEN_HIGH_STD'
	out_to_sign(msg, msg_color, msg_mode, msg_font)

def colordemo():
	for color in colors:
		msg_color = color
		msg = color
		out_to_sign(msg, msg_color, msg_mode, msg_font)
		time.sleep(5)

def fontdemo():
	for font in fonts:
		msg_font = font
		msg = font
		out_to_sign(msg, msg_color, msg_mode, msg_font)
		time.sleep(5)

def modedemo():
	for mode in modes:
		msg_mode = mode
		msg = mode
		out_to_sign(msg, msg_color, msg_mode, msg_font)
		time.sleep(10)

def out_to_sign(msg, color, mode, font):
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
	#ask_for_input()
	#colordemo()
	#modedemo()
	fontdemo()
	#reset_sign()
	#static_test()

if __name__ == "__main__":
 	main()
