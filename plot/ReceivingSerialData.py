# This module connects with Arduino through a serial port and generates data to draw four real-time plots.
# It works with uploaded through Arduino IDE (open-source Arduino Software) AnalogReadSerial.
# (In this IDE go to: File -> Examples -> 01. Basics -> AnalogReadSerial).
# Modify this file to print four values with a space in between and end with a new line.
# For example:
#       Serial.print(sensorValue0);
#       Serial.print(" ");
#       Serial.print(sensorValue1);
#       Serial.print(" ");
#       Serial.print(sensorValue2);
#       Serial.print(" ");
#       Serial.println(sensorValue3);
#
# Before running please check the setting for a serial port - COM1/COM2... and edit it if necessary.
# (By default is set on COM6)
#
# This module can run independently from DrawPlots.py. It just prints the read data to the console.
#
# author: Krystian Sulinski
# license: GNU GENERAL PUBLIC LICENSE
# last modified: 08.01.2016


import serial
import time
from threading import Thread
import itertools

received = ''


def receiving(serial_port):
    global received
    while True:
        buffer_string = serial_port.read(serial_port.inWaiting())
        # buffer_string = {str} '57 124 179 205\r\n58 119 171 190\r\n58 119 171 187\r\n'
        if '\n' in buffer_string:
            buffer_string = [int(i) for i in buffer_string.split()]
            received = buffer_string[0:4]


class SerialData(object):
    def __init__(self):
        self.start_time = time.time()
        self.buffer = ''
        try:
            self.serial = serial.Serial(port='com6', baudrate=9600)     # opens serial port, check this port
        except serial.serialutil.SerialException:
            self.serial = None
            print "No serial connection"

        else:       # if no exception is raised during the try block, the else clause is executed afterwards
            Thread(target=receiving, args=(self.serial, )).start()       # create and start the thread's activity
        self.number_of_plots = 4

    def next(self, number_of_plot):
        if not self.serial:
            print "Serial is not connected"
            return -1

        if number_of_plot > self.number_of_plots or number_of_plot < 0:
            print "Demanding number_of_plot = {} is out of range. numbers_of_plot = {}". \
                format(number_of_plot, self.number_of_plots)
            return -1

        for i in range(40):
            if len(received) <= number_of_plot:
                print "{:.3f} sec: ---------------- bogus data ----------------".format((time.time() - self.start_time))
                time.sleep(.005)
                return -1
            try:
                plot_data = float(received[number_of_plot])
                print "{:.3f} sec: {}".format(time.time() - self.start_time, received)
                return plot_data
            except ValueError:
                print "{:.3f} sec: ---------------- bogus data ----------------".format((time.time() - self.start_time))
                time.sleep(.005)
        return -1


if __name__ == "__main__":
    serial_data = SerialData()
    start_time = time.time()
    for i in itertools.count():
        time.sleep(0.015)
        print "{:.3f} sec: {}".format(time.time() - start_time, received)
