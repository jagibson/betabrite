import random
import string

import cherrypy
import json


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">Give it now!</button>
            </form>


            <form method="get" action="publish_to_iot">
              Message:<br>
              <input type="text" name="message"><br>

            <br>

            Color:<br>
            <select name="color"><br>
              <option value="RED" selected>red</option>
              <option value="GREEN">green</option>
              <option value="AMBER">amber</option>
              <option value="RAINBOW_1">rainbow vertically</option>
              <option value="RAINBOW_2">raidbow diagonally</option>
              <option value="COLOR_MIX">alternate</option>
              <option value="AUTOCOLOR">randomize</option>
            </select>

            <br>

            Font:<br>
            <select name="font"><br>
              <option value="FIVE_HIGH_STD">5 pix</option>
              <option value="SEVEN_HIGH_STD" selected>7 pix</option>
              <option value="SEVEN_HIGH_FANCY">7 pix, fancy</option>
             </select>

            <br>

            Mode:<br>
            <select name="mode"><br>
            <option value="ROTATE">rotate</option>
            <option value="HOLD" selected>hold</option>
            <option value="ROLL_UP">roll up</option>
            <option value="ROLL_DOWN">roll down</option>
            <option value="ROLL_LEFT">roll left</option>
            <option value="ROLL_RIGHT">roll right</option>
            <option value="WIPE_UP">wipe up</option>
            <option value="WIPE_DOWN">wipe down</option>
            <option value="WIPE_LEFT">wipe left</option>
            <option value="WIPE_RIGHT">wipe right</option>
            <option value="SCROLL">scroll</option>
            <option value="ROLL_IN">roll in</option>
            <option value="ROLL_OUT">roll out</option>
            <option value="WIPE_IN">wipe in</option>
            <option value="WIPE_OUT">wipe out</option>
            <option value="TWINKLE">twinkle</option>
            <option value="SPARKLE">sparkle</option>
            <option value="SNOW">snow</option>
            <option value="INTERLOCK">interlock</option>
            <option value="SWITCH">switch</option>
            <option value="SPRAY">spray</option>
            <option value="STARBURST">starburst</option>
            <option value="WELCOME">welcome</option>
            <option value="SLOT_MACHINE">slow machine</option>
            <option value="THANK_YOU">thank you</option>
            <option value="NO_SMOKING">no_smoking</option>
            <option value="DONT_DRINK_DRIVE">don't drink and drive</option>
            <option value="RUNNING_ANIMAL">running animal</option>
            <option value="FISH_ANIMATION">fish animation</option>
            <option value="FIREWORKS">fireworks</option>
            <option value="TURBO_CAR">turbo car</option>
            <option value="BALLOON_ANIMATION">balloon animation</option>
            <option value="CHERRY_BOMB">cherry bomb</option>
            </select>

            <button type="submit">Publish!</button>
          </form>

          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

    @cherrypy.expose
    def publish_to_iot(self, color, message, font, mode):
        #return (color, message, font, mode)
        publish_values = dict(zip(("message", "color", "font", "mode"), (message, color, font, mode)))
        publish_desired = {'desired': publish_values}
        publish_state = {'state': publish_desired}
        jsonned = json.dumps(publish_state)
        return jsonned
        
if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())