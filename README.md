#The Button Monitor

A simple Python script and Arduino project to monitor the status of [The Button](http://www.reddit.com/r/thebutton/).     
Based on ALPSquid's GitHub project (https://github.com/ALPSquid/thebutton-monitor).

## Hardware
This project was tested with an Arduino Uno, but should work with any recent Arduino model. 
Six LEDs (Purple, Blue, Green, Yellow, Orange, and Red) are connected to digital IO pins 2 through 7 (Purple to 2 and Red to 7) 
through current limiting resistors (150 Ohms or so). Arduino is connected to a PC through USB.

## Dependencies
This project was tested on Python 2.7 and requires Python [Websocket Client](https://pypi.python.org/pypi/websocket-client) to
handle communication with Reddit and [pySerial](https://pypi.python.org/pypi/pyserial) to communicate with Arduino. 
