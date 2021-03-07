#!/usr/bin/env python
from bottle import route, run
import RPi.GPIO as GPIO
import yaml

# API routing
@route('/')
def apiRoot():
  return "Hello"

@route('/json')
def apiJson():
  readPins(pinMap)
  return {"gpio":pinMap}

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
  with open('pinmap.yaml') as f:
    global pinMap
    pinMap = yaml.safe_load(f)

  # Set's GPIO pins to BCM GPIO numbering, and input mode
  GPIO.setmode(GPIO.BCM)
  for pin in pinMap:
    GPIO.setup(pin["pin"], GPIO.IN, pull_up_down=GPIO.PUD_UP)

  # Start the bottle API server
  run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
  main()
