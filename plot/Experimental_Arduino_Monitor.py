import serial
from threading import Thread
import time


class SerialData:
    def __init__(self):
        try:
            self.serial = serial.Serial(port='com6', baudrate=9600)  # opening serial port
        except serial.serialutil.SerialException:
            self.serial = None
            print "No serial connection"
        # If no exception is raised during the try block, the else clause is executed afterwards.
        else:
            # create and start the thread's activity
            Thread(group=None, target=self.receiving(), args=(self.serial,)).start()
        self.number_of_plots = 4

    def receiving(self):
        while True:
            buffer_string = self.serial.read(self.serial.inWaiting())
            # buffer_string = {str} '57 124 179 205\r\n58 119 171 190\r\n58 119 171 187\r\n'
            if '\n' in buffer_string:
                buffer_string = [int(i) for i in buffer_string.split()]
                return buffer_string

    def get_next(self, number_of_plot):
        if not self.serial:
            print "Serial is not connected"
            return -1

        if number_of_plot > self.number_of_plots or number_of_plot < 0:
            print "Demanding number_of_plot = {} is out of range. numbers_of_plot = {}".\
                format(number_of_plot, self.number_of_plots)
            return -1

        for i in range(40):
            try:
                return self.receiving(self.serial)[number_of_plot]
            except ValueError:
                print "No data"
                time.sleep(.005)
        return -1

if __name__ == "__main__":
    serial_data = SerialData()
    while True:
        print serial_data.get_next(0)
    # output:
    # [57, 124, 179, 205]
    # [58, 119, 171, 190]
    # [58, 119, 171, 187]
    # ...
