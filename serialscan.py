import serial
import sys

# PORT = "/dev/pts/6"
PORT = "/dev/ttyUSB0"
BAUDRATE = "115200"

if sys.argv[1] is None:
    FILE = "capture_default"
else:
    FILE = sys.argv[1]

ser = serial.Serial(
    port=PORT,
    baudrate=BAUDRATE
)

f = open(FILE, 'wb')

count = 0

try:
    while True:
        if ser.in_waiting > 0:
            this_byte = ser.read(1)
            f.write(this_byte)
            count += 1
            print(this_byte)
except KeyboardInterrupt:
    print(f"\nProcessed {count} bytes.")
    print(f"Binary wrote to file {FILE}.")
    ser.close()
    f.close()
