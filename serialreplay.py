import serial
import sys

PORT = "/dev/pts/5"
BAUDRATE = "9600"

if sys.argv[1] is None:
    FILE = "capture_default"
else:
    FILE = sys.argv[1]

ser = serial.Serial(
    port=PORT,
    baudrate=BAUDRATE
)

f = open(FILE, 'rb')

try:
    this_byte = f.read(1)
    while this_byte != b'':
        ser.write(this_byte)
        print(f"Wrote {this_byte} to serial buffer.")
        this_byte = f.read(1)
finally:
    f.close()
