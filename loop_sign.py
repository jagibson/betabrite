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
        msg = "(" + str(colors.index(color)) + ")-" + color
        out_to_sign(msg, msg_color, msg_mode, msg_font)
        time.sleep(2)

def fontdemo():
    for font in fonts:
        msg_font = font
        #msg_mode = "HOLD"
        msg = "(" + str(fonts.index(font)) + ")-" + font
        out_to_sign(msg, msg_color, msg_mode, msg_font)
        time.sleep(5)

def modedemo():
    for mode in modes:
        msg_mode = mode
        msg = "(" + str(modes.index(mode)) + ")-" + mode
        #msg = mode
        out_to_sign(msg, msg_color, msg_mode, msg_font)
        time.sleep(4)

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
    #msg_font = 'FIVE_HIGH_STD'
    msg = "Type your message"
    out_to_sign(msg, msg_color, msg_mode, msg_font)
    msg = raw_input()
    out_to_sign(msg, msg_color, msg_mode, msg_font)

def colorchoice(colorstring):
    global msg_color
    end_loop = False
    input_color = raw_input()
    if input_color == '':
        msg_color = msg_color
        end_loop = True
    elif input_color in (["l","L"]):
        colordemo()
    elif input_color in str(range(len(colors))):
        print "color is " + input_color
        msg_color = colors[int(input_color)]
        end_loop = True
    else:
        msg_color = msg_color
    return (msg_color, end_loop)


def ask_for_color():
    colorstring = ''
    msg_font = 'FIVE_HIGH_STD'
    msg_mode = 'HOLD'
    msg_color = 'RED'
    colors_zero_indexed = len(colors) -1
    end_loop = False
    while True:
        msg = "Color? (0-" + str(colors_zero_indexed) + "), l"
        out_to_sign(msg, msg_color, msg_mode, msg_font)
        choicereturn = colorchoice(colorstring)
        print(choicereturn)
        end_loop = choicereturn[1]
        if end_loop:
            return choicereturn[0]
            break

def fontchoice(fontstring):
    global msg_font
    end_loop = False
    input_font = raw_input()
    if input_font == '':
        msg_font = msg_font
        end_loop = True
    elif input_font in (["l","L"]):
        fontdemo()
    elif input_font in str(range(len(fonts))):
        print "font is " + input_font
        msg_font = fonts[int(input_font)]
        end_loop = True
    else:
        print "failed to match"
    return (msg_font, end_loop)

def ask_for_font():
    #global msg_color
    #global msg_mode
    fontstring = ''
    msg_font = 'FIVE_HIGH_STD'
    msg_mode = 'HOLD'
    msg_color = 'RED'
    fonts_zero_indexed = len(fonts) -1
    end_loop = False
    while True:
        msg = "Font? (0-" + str(fonts_zero_indexed) + "), l"
        out_to_sign(msg, msg_color, msg_mode, msg_font)
        choicereturn = fontchoice(fontstring)
        print(choicereturn)
        end_loop = choicereturn[1]
        if end_loop:
            return choicereturn[0]
            break


def modechoice(modestring):
    global msg_mode
    end_loop = False
    input_mode = raw_input()
    if input_mode == '':
        msg_mode == msg_mode
        end_loop = True
    elif input_mode in (["l","L"]):
        modedemo()
    elif input_mode in str(range(len(modes))):
        print "mode is " + input_mode
        msg_mode = modes[int(input_mode)]
        end_loop = True
    else:
        print "failed to match"
    return (msg_mode, end_loop)

def ask_for_mode():
    modestring = ''
    msg_mode = 'FIVE_HIGH_STD'
    msg_mode = 'HOLD'
    msg_color = 'RED'
    modes_zero_indexed = len(modes) -1
    end_loop = False
    while True:
        msg = "Mode? (0-" + str(modes_zero_indexed) + "), l"
        out_to_sign(msg, msg_color, msg_mode, msg_font)
        choicereturn = modechoice(modestring)
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
    msg_font=ask_for_font()
    msg_mode=ask_for_mode()
    ask_for_input(msg_color)

#if __name__ == "__main__":
#   main()

#import threading
#user_input = [None]
#
#def get_user_input(user_input_ref):
#   print("In get_user_input: " + str(user_input_ref))
#   user_input_ref[0] = raw_input()
#
#mythread = threading.Thread(target=get_user_input, args=(user_input,))
#mythread.daemon = True
#mythread.start()
#
#while 1:
#   time.sleep(.1)
#   print(user_input)
#   if user_input[0] is "e":
#        main()
#        user_input = [None]

import thread

def input_thread(L):
    L.append(raw_input())

def do_print():
    L = []
    L.append("junk")
    thread.start_new_thread(input_thread, (L,))
    
    print("L is: " + str(L))
    time.sleep(.1)
    if L[0] is "e":
        main()
    del L

#while True:
do_print()

