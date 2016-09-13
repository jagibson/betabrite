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



#print colors

def main():
  sign = alphasign.Serial(device='/dev/ttyUSB0')
  sign.connect()

  #text = alphasign.Text("%sblah" % colors['red'], label="A")
  #text = alphasign.Text("Hello World!", label="A", mode=alphasign.modes.THANK_YOU)
  #text = alphasign.Text("%sthis text is fast" % alphasign.speeds.SPEED_2,
                     #label="A",
                     #mode=alphasign.modes.ROTATE)
  text = alphasign.Text("%sthis is wide" % alphasign.charsets.WIDE_STROKE_FIVE,
                     label="A")

  sign.write(text)



if __name__ == "__main__":
  main()
