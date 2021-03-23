#!/usr/bin/env python
from bottle import route, run, static_file
import RPi.GPIO as GPIO
import yaml

# API routing
@route('/')
def apiRoot():
  return static_file('index.html', root='.')

@route('/json')
def apiJson():
  return {"gpio": readPins(config["pinMap"])}

@route('/json/<thisPin:int>')
def apiJsonPin(thisPin):
  return {"gpio": [next((p for p in readPins(config["pinMap"]) if p.get('input') == thisPin), {})]}

# GPIO processing
def readPins(pinMap):
  for pin in pinMap:
    pin["state"] = 0 if (GPIO.input(pin["pin"])) else 1
  return pinMap

def main():
  """
  pin definitions are read in from pinmap.yaml
  """

  # Read our pinmap definition file, make it available globally
  with open('config.yaml') as f:
    global config
    config = yaml.safe_load(f)

  # Set's GPIO pins to BCM GPIO numbering, and input mode
  GPIO.setmode(GPIO.BCM)
  for pin in config["pinMap"]:
    GPIO.setup(pin["pin"], GPIO.IN, pull_up_down=GPIO.PUD_UP)

  # Start the bottle API server
  run(host=config["listen"]["host"], port=config["listen"]["port"], debug=True)

if __name__ == "__main__":
  main()
