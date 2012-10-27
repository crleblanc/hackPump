#!/usr/bin/env python
#
# Record the settings used for any 38 or so KHz remote and save the results in a json file,
# not compatible with Lirc or anything else but very simple for us to parse.
#
# Chris LeBlanc, 2012
#
#--
#
# This work is free: you can redistribute it and/or modify it under the terms 
# of Creative Commons Attribution ShareAlike license v3.0
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the License for more details. You should have received a copy of the License along 
# with this program. If not, see <http://creativecommons.org/licenses/by-sa/3.0/>.

import sys
import json
import serial
import argparse
from irtoy import IrToy

def getCommandLineArgs():
    parser = argparse.ArgumentParser(description='Record pyirtoy codes from the IR Toy and store in a JSON file')
    parser.add_argument('-d', '--device', dest='device', action='store',
                    default='/dev/ttyACM0',
                    help='Serial device to receive the IR code from, must be an IR Toy running firmware rev. 22 or greater.')
    parser.add_argument('-o', '--outfile', dest='outfile', action='store', required=True,
                    help='Ouptut JSON file containing a dictionary of named IR commands')

    return parser.parse_args()

def recordCodes(deviceName):
    '''Ask the user what the button press should be called and return as a dict of 
    name:code key/value pairs.  Similar to the Lirc irrecord tool'''

    serialDevice = serial.Serial(deviceName)
    toy = IrToy(serialDevice)
    codes = {}
    while True:
        
        try:
            input = raw_input
        except NameError:
            pass

        label = input('Please enter a name for the button you will press, or Enter to finish:\n')
        
        if label == '':
            break
        else:
            toy.reset()
            print('press the remote control button once for the %s button:' % label)
            codes[label] = toy.receive()

    serialDevice.close()

    return codes

def main():

    args = getCommandLineArgs()
    codes = recordCodes(args.device)
    
    with open(args.outfile, 'w+') as outFile:
        json.dump(codes, outFile)

    print('Recording complete, results saved in: %s' % args.outfile)
    

if __name__ == "__main__":
    main()
