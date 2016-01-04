import serial


class SerialData:
    def __init__(self):
        self.serial = serial.Serial(port='com6', baudrate=9600)  # opening serial port

    def receive(self):
        while True:
            buffer_string = self.serial.read(self.serial.inWaiting())
            # buffer_string = {str} '57 124 179 205\r\n58 119 171 190\r\n58 119 171 187\r\n'
            if '\n' in buffer_string:
                buffer_string = [int(i) for i in buffer_string.split()]
                return buffer_string

    def get(self):
        if not self.serial:
            return -1
        return self.receive()


if __name__ == "__main__":
    serial_data = SerialData()
    while True:
        print serial_data.get()
        # output:
        # [57, 124, 179, 205]
        # [58, 119, 171, 190]
        # [58, 119, 171, 187]
