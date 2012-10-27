#!/usr/bin/env python
#
# Play the settings back from a json file recorded with record_codes.py,
# mainly used for testing various codes, and if they can be repeated a 
# number of times
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
    parser = argparse.ArgumentParser(description='Play pyirtoy codes from a file on the IR Toy')
    parser.add_argument('-d', '--device', dest='device', action='store',
                    default='/dev/ttyACM0',
                    help='Serial device to write the IR code to, must be an IR Toy running firmware rev. 22 or greater.')
    parser.add_argument('-i', '--input', dest='file', action='store', required=True,
                    help='Input JSON file containing a dictionary of named IR commands, recorded with record_codes.py.')
    parser.add_argument('-c', '--commands', dest='commands', action='store', required=True, nargs='+',
                    help='One or more commands to send to the toy, these are the keys in the JSON dictionary.')

    return parser.parse_args()

def main():

    args = getCommandLineArgs()

    device = serial.Serial(args.device)
    filename = args.file
    with open(filename, 'r') as inFile:
        codes = json.load(inFile)

        for codeKey in args.commands:
            toy = IrToy(device)
            toy.transmit(codes[codeKey])
            print('code:', codeKey, 'code length:', len(codes[codeKey]), 'handshake:', toy.handshake, 'bytecount:', toy.byteCount, 'complete:', toy.complete)

    device.close()

if __name__ == "__main__":
    main()
