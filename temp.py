import fcntl
import struct
import sys
from subprocess import Popen, PIPE
import termios

struct.unpack("HHHH", fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, struct.pack("HHHH", 0, 0, 0, 0)))

Popen(['/usr/lib/w3m/w3mimgdisplay', "-test"], stdout=PIPE, universal_newlines=True).communicate()
