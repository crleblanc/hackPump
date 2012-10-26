# Configuration settings for the hack_pump program
import logging

# The path to the serial device that corresponds to the IR Toy.
# In Linux this is typically /dev/ttyACM0 or something similar.
# Windows will probably be COM1 or something similar, but this
# hasn't been tested.
serial_device='/dev/ttyACM0'

# The Google Calendar ID for the calendar you wish to use for
# controlling the heat pump.  This ID is available from 
# settings->calendars->[calendar name]->Calendar ID in the web 
# interface. Each event in the calendar should have a summary 
# (also called 'what') field that corresponds to a named code 
# in the ir_code_file below.  Only the summary and start/end 
# fields are used.
calendar_id='ABC123@group.calendar.google.com'

# The JSON file containing the named IR codes to transmit to 
# the IR toy.  These can be recorded using the record_codes.py 
# utility to capture all the useful IR codes from your remote.
# This path is relative to where the program is called from.
# NOTE: this file will not exist, you need to create one with 
# record_codes.py
ir_code_file='ir_codes.json'

# The file we use to store the previous settings for the heat 
# pump.  It will be created if it doesn't exist.
saved_settings='settings.json'

# the named IR code that corresponds to 'off', or what code 
# should be sent when there are no valid calendar events at the 
# current time.  Setting this to None means no IR code will be 
# sent.
off_setting='off'

# the filename to send logging messages to.  If set to None, logging
# will be disabled.
logfile='hackpump.log'

# the level of logging information to send to the logfile.
# See http://docs.python.org/library/logging.html for more information
# on debugging levels.  Levels are: DEBUG, INFO, WARNING, ERROR, CRITICAL.
# Set the level to logging.CRITICAL if you don't want much logging
# info.
logging_level=logging.ERROR
