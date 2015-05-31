Important Note
==============
This project relies on the IR Toy for transmitting and receiving IR signals.  Unfortunately this hardware seems to suffer from a firmware bug described here https://github.com/crleblanc/PyIrToy/issues/2, which seems especially bad on the Raspberry Pi.  I haven't been able to find a workaround for this stability problem, so cannot recommend using this project for long running tasks.

hackPump
========

Control any 38 KHz infrared device using Google Calendar for scheduling.  I'm using a 
Raspberry pi `Raspberry Pi <http://raspberrypi.org>`_ and an 
`IR Toy <http://dangerousprototypes.com/docs/USB_Infrared_Toy>`_ to manage my heat pump.

Highlights
-------------

- Simple and small python programs to query a Google Calendar for the current event.

- Gets the corresponding IR code from a JSON file of IR codes.  In my case this is a
  list of temperatures and codes.

- Sends the IR code to the device using the IR Toy.  It will only send a new signal if
  it's different from the last one sent.

- Can handle very long IR codes, much longer than Lirc or the IguanaIR can handle.  This
  is needed for the Mitsubishi heat pump IR codes.  Has been used to successfully send a
  15 second IR signal.  Note: this project is not compatible with Lirc, but the IR Toy
  can be used with Lirc directly.

Why?
----

- My Mitsubishi heat pump is great but only has a very simple timer.  You can purchase a
  programmable thermostat, but it's expensive and doesn't do anything I'm after.
  Being able to control this with a Google Calendar is ideal since it is a very 
  powerful calendar that is available from the web, smart phones, and has a well documented
  API for communicating with it.  No need to reinvent the wheel.

- I'm interested in being able to set the temperature of my house before I get home or
  before I get up in the morning.  There are some excellent products for this, such as the 
  Nest and Ecobee, but unfortunately they don't work with heat pumps like mine.  They're
  full of advanced features that I have no intention of implementing, like motion sensing.
  I'm simply after a good calendar integration with low cost open-source hardware.

- Both the Raspberry Pi and the IR Toy are low cost, low power, and have an excellent open 
  source community behind them.

- There are a few other projects doing similar things, but they don't have any calendar
  integration or require specialized hardware.

Project components
------------------

- A Python module for transmitting and receiving IR codes from an IR Toy.  See the github 
  project page for more info: `PyIrToy <https://github.com/crleblanc/PyIrToy>`_.
  I split this into a different project and added it to pypi to make it easy for others to
  use.

- A command line program called hack_pump.py.  This is the main part of this project, it
  queries the Calendar and sends an IR code if required.

- Two command line utilities called record_codes.py and transmit_codes.py for recording and
  transmitting IR codes.  transmit_codes.py is mainly used for testing the recorded codes.
  record_codes.py records the IR codes to a JSON file that can be used by hack_pump.py.
