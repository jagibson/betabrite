#!/usr/bin/env python
import alphasign
import time
import itertools

sign_device='/dev/ttyUSB0'

colors = ["RED", "GREEN", "AMBER", "RAINBOW_1", "RAINBOW_2", "COLOR_MIX", "AUTOCOLOR"]
modes = ["ROTATE", "HOLD", "ROLL_UP", "ROLL_DOWN", "ROLL_LEFT", "ROLL_RIGHT", "WIPE_UP", "WIPE_DOWN", "WIPE_LEFT", "WIPE_RIGHT", "SCROLL", "ROLL_IN", "ROLL_OUT", "WIPE_IN", "WIPE_OUT", "TWINKLE", "SPARKLE", "SNOW", "INTERLOCK", "SWITCH", "SPRAY", "STARBURST", "WELCOME", "SLOT_MACHINE", "THANK_YOU", "NO_SMOKING", "DONT_DRINK_DRIVE", "RUNNING_ANIMAL", "FIREWORKS", "TURBO_CAR"]
fonts = ["FIVE_HIGH_STD", "SEVEN_HIGH_STD", "SEVEN_HIGH_FANCY"]

msg = "THIS IS A TEST"
msg_color = 'GREEN'
msg_mode = 'HOLD'
msg_font = 'SEVEN_HIGH_STD'

#print len(fonts)

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
		time.sleep(2)

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

def ask_for_input(msg_color):
	msg_font = 'FIVE_HIGH_STD'
	msg = "Type your message"
	out_to_sign(msg, msg_color, msg_mode, msg_font)
	msg = raw_input()
	out_to_sign(msg, msg_color, msg_mode, msg_font)

def colorchoice(colorstring):
	global msg_color
	end_loop = False
	input_color = raw_input()
	if input_color in (["l","L"]):
		msg_mode = 'ROTATE'
		for color in colors:
			colorstring = colorstring + "(" + str(colors.index(color)) + ")-" + color + "   "
		msg = colorstring
		out_to_sign(msg, msg_color, msg_mode, msg_font)
		time.sleep(11)
	elif input_color in (["d","D"]):
		colordemo()
	elif input_color in str(range(len(colors))):
		#msg_color = input_color
		print "color is " + input_color
		msg_color = colors[int(input_color)]
		end_loop = True
	else:
		print "failed to match"
	return (msg_color, end_loop)


def ask_for_color():
	colorstring = ''
	msg_font = 'FIVE_HIGH_STD'
	msg_mode = 'HOLD'
	msg_color = 'RED'
	colors_zero_indexed = len(colors) -1
	end_loop = False
	while True:
		msg = "Color? (0-" + str(colors_zero_indexed) + "), l,d"
		out_to_sign(msg, msg_color, msg_mode, msg_font)
		choicereturn = colorchoice(colorstring)
		print(choicereturn)
		end_loop = choicereturn[1]
		if end_loop:
			return choicereturn[0]
			break



def main():
	#msg = "THIS IS A TEST"
	#msg_color = 'GREEN'
	#msg_mode = 'HOLD'
	#msg_font = 'SEVEN_HIGH_STD'
	#colordemo()
	#modedemo()
	#fontdemo()
	#reset_sign()
	#static_test()
	msg_color=ask_for_color()
	ask_for_input(msg_color)

if __name__ == "__main__":
 	main()
