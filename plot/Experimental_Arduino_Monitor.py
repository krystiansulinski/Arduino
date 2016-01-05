import serial


class SerialData:
    def __init__(self):
        self.serial = serial.Serial(port='com6', baudrate=9600)  # opening serial port
        self.number_of_plots = len(self.receive())

    def receive(self):
        while True:
            buffer_string = self.serial.read(self.serial.inWaiting())
            # buffer_string = {str} '57 124 179 205\r\n58 119 171 190\r\n58 119 171 187\r\n'
            if '\n' in buffer_string:
                buffer_string = [float(i) for i in buffer_string.split()]
                return buffer_string

    def get(self, number_of_plot=None):
        if not self.serial:
            print "serial is not connected"
            return -1
        if number_of_plot > self.number_of_plots:
            print "demanding number_of_plot = {} is out of range. numbers_of_plot = {}".format(number_of_plot,
                                                                                               self.number_of_plots)
            return -1
        if number_of_plot is None:
            return self.receive()
        return self.receive()[number_of_plot]


if __name__ == "__main__":
    serial_data = SerialData()
    while True:
        print serial_data.get(0)
    # output:
    # [57, 124, 179, 205]
    # [58, 119, 171, 190]
    # [58, 119, 171, 187]
    # ...
