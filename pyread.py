import serial

# Define your serial port settings
port = 'COM4'  # Change this to your serial port, e.g., 'COM1' on Windows
baudrate = 9600  # Change this to match your device's baud rate

# Initialize the serial port
ser = serial.Serial(port, baudrate)

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode().strip()

        # Print the received line
        print(line)

        if int(line) ==1:
            print('hai')

except KeyboardInterrupt:
    # Close the serial port when KeyboardInterrupt is detected (Ctrl+C)
    ser.close()