hackPump
========

Control a heat pump over the internet using a `Raspberry Pi <http://raspberrypi.org>`_ 
and an `IR Toy <http://dangerousprototypes.com/docs/USB_Infrared_Toy>`_.  Actually this
project could be used to control any IR device from a Google calendar, not just a heat
pump.  It can handle very long IR codes, so should be able to handle most 38 KHz signals.

Project Goals
-------------

- To make a simple utility that can poll a Google Calendar and get the summary for a
  current event.

- Send an IR Code to a device (in this case a Mitsubishi heat pump) based on the calendar
  event.

Why?
----

- My Mitsubishi heat pump is great but only has a very simple timer.  You can purchase a
  programmable thermostat, but it's expensive and doesn't do anything I'm after.
  Being able to control this with a Google Calendar would be ideal since it is a very 
  powerful calendar that is available from the web, smartphones, and has a well documented
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

- A Python module for transmitting and receiving IR codes from an IR Toy.  The IR Toy is
  an excellent USB IR transceiver, perfect for this application.  The module I wrote is 
  called PyIrToy.  See the github project page for more info: `PyIrToy <https://github.com/crleblanc/PyIrToy>`_.
  This simple module makes it easy to communicate with the IR Toy, and is worth looking into
  if you're using the IR Toy and don't feel the desire to work with C.  I decided to split
  this into two separate projects, since PyIrToy is far more generic than this project.

- A command line program called hack_pump.py.  This polls a public Google calendar and gets 
  the current calendar event.  It then transmits the corresponding IR code with the Ir Toy.
  Keeping things simple, I intend on having a cron job on the Pi that calls this program once 
  every few minutes to see if it should transmit a new IR code.

- Two command line utilities called record_codes.py and transmit_codes.py for recording and
  transmitting IR codes.  transmit_codes.py is mainly used for testing the recorded codes.
  record_codes.py records the IR codes to a JSON file that can be used by hack_pump.py.  Note:
  The IR utilities in this project do not use or supplement LIRC.  The codes from my heat pump 
  were too long to be used with LIRC, so I rolled my own solution.
