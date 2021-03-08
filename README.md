# gpioapi
Simple API server written in python, that reports the status of raspberry
pi GPIO input pins.

## Pin mapping
GPIO pins to monitor are defined in pinmap.yaml.  

The `pin` numbers are BCM pin numbering and the `label` descriptors are
arbitrary.  You should modify them to reflect what's connected to that
input pin.

## Quick Start
```
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
cp config.yaml.sample config.yaml
./api.py
```
