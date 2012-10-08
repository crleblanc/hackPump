hackPump
========

This is a Project for controlling a heat pump over the internet using a Raspberry Pi 
and an IR Toy.  Why am I doing this?

- My Mitsubishi heat pump is great but only has a very simple timer.  You can purchase a
  programmable thermostat, but it's expensive and far too basic.
- I'm interested in being able to set the temperature of my house before I get home or
  before I get up in the morning.  There are some excellent products for this, such as the 
  Nest and Ecobee, but unfortunately they don't work with heat pumps like mine.
- Both the Raspberry Pi and the IR Toy are low cost and powerful with an excellent open
  source community.

This is currently in early development, but the goal is to have the following components:

- A Python module for controlling the IR Toy, coming soon.  This will allow transmitting and 
  receiving of IR signals from the IR Toy in a very simple class.
- A Google AppEngine front end.  My home network is not reliable enough to host a server, 
  instead a GAE app will be used to control the settings.  I also plan to run the heat pump off 
  a Google Calendar, allowing a very simple but powerful way to manage the heat pump on a 
  schedule.
- A Python client running on the Raspberry Pi that will request the heat pump settings from the
  app engine instance.