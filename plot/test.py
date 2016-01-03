__author__ = 'krystian'


for i in range(1, 2):
    buffer_string = "11 22 33 44\n 55 66 77 88\n 99 00 11 22\n"
    if '\n' in buffer_string:
        buffer_string = [int(i) for i in buffer_string.split()]
        buffer_string = str(buffer_string)
        s = buffer_string.split("55")
        print buffer_string
        print s
