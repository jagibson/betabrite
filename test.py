import time
import alphasign

colors = {
  "red": "alphasign.colors.RED",
  "green": "alphasign.colors.GREEN",
  "amber": "alphasign.colors.AMBER",
  "rainbow_vertical": "alphasign.colors.RAINBOW_1",
  "rainbow_diagonal": "alphasign.colors.RAINBOW_2",
  "alternate": "alphasign.colors.COLOR_MIX",
  "randomize": "alphasign.colors.AUTOCOLOR"
}

#print colors['red']

modes = {
  "hold": "HOLD"
}

# Supported fonts
# FIVE_HIGH_STD (5 high, all caps)
# FIVE_STROKE (looks like seven_high_std)
# SEVEN_HIGH_STD (normal)
# SEVEN_HIGH_FANCY (thicker letters)
# SEVEN_SHADOW (normal)
# FULL_HEIGHT_FANCY same as SEVEN_HIGH_FANCY
# FULL_HEIGHT_STD same as SEVEN_HIGH_STD
# SEVEN_SHADOW_FANCY same as SEVEN_HIGH_STD

msg = "test for sign"
msg_color = 'GREEN'
msg_mode = 'HOLD'
msg_font = 'FIVE_HIGH_STD'


color = getattr(alphasign.colors, msg_color)
mode = getattr(alphasign.modes, msg_mode)
font = getattr(alphasign.charsets, msg_font)

print color

#print colors

def main():
  sign = alphasign.Serial(device='/dev/ttyUSB0')
  sign.connect()

  #msg_color = 'alphasign.colors.' + color 

  text = alphasign.Text("%s%s%s" % (color, font, msg), label="A", mode=mode)

  sign.write(text)



if __name__ == "__main__":
  main()
