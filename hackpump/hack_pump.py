#!/usr/bin/env python
#
# Main program for polling a google calendar and controlling the heat pump

# TODO: save the time of last settings fetched from the calendar, 
# if too long since last setting (2 hours?) turn the heat pump off.

import os
import serial
import json
import logging
import traceback
import time
from calendar_events import current_calendar_events
from irtoy import IrToy
import conf

__author__ = 'Chris LeBlanc'
__version__ = '0.1'
__email__ = 'crleblanc@gmail.com'

def get_saved_settings(inputFile):
    last_temp = None
    if os.path.exists(inputFile):
        try:
            with open(inputFile, 'rb') as prevSettingsObj:
                last_temp = json.load(prevSettingsObj)
        except:
            pass

    return last_temp

def save_settings(outputFile, settings):
    if outputFile:
        with open(outputFile, 'wb') as prevSettingsObj:
            json.dump(settings, prevSettingsObj)

def set_temp(deviceName, jsonFile, temp):
    
    with open(jsonFile, 'r') as inFile:
        codes = json.load(inFile)
        irCode = codes[temp]
        if irCode:
            with serial.Serial(deviceName) as serialDevice:
                toy = IrToy(serialDevice)
                toy.transmit(codes[temp])

                logging.debug('response from IR Toy: handshake: %d bytecount: %d complete: %s' % (toy.handshake, toy.byteCount, toy.complete))

def main():
    last_temp = get_saved_settings(conf.saved_settings)
    
    if conf.logfile:
        logging.basicConfig(filename=conf.logfile, level=conf.logging_level, format='%(asctime)s %(message)s')
    
    try:
        events = current_calendar_events(conf.calendar_id, time_window=1)
        logging.info('getting calendar events from Calendar ID %s' % conf.calendar_id)
        logging.debug('calendar events: %s' % events)
        
        temp_now = None
        if events:
            temp_now = events[-1]['summary']
        else:
            temp_now = conf.off_setting

        logging.info('summary info from calendar event: %s' % temp_now)
        
        if temp_now != last_temp:
            logging.info('sending named IR code: %s' % temp_now)
            set_temp(conf.serial_device, conf.ir_code_file, temp_now)
            logging.info('saving code: %s to settings file: %s' % (temp_now, conf.saved_settings) )
            save_settings(conf.saved_settings, temp_now)
        else:
            logging.info('current event summary identical to last event, not sending IR command')
    except:
        logging.error(traceback.format_exc())
        raise

    finally:
        if conf.logfile:
            logging.shutdown()

if __name__ == '__main__':
    main()
