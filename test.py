import alphasign

msg = "another sign"
msg_color = 'GREEN'
msg_mode = 'HOLD'
msg_font = 'FIVE_HIGH_STD'


color = getattr(alphasign.colors, msg_color)
mode = getattr(alphasign.modes, msg_mode)
font = getattr(alphasign.charsets, msg_font)

def main():
	sign = alphasign.Serial(device='/dev/ttyUSB0')
	sign.connect()

	text = alphasign.Text("%s%s%s" % (color, font, msg), label="A", mode=mode)

	sign.write(text)

if __name__ == "__main__":
 	main()
