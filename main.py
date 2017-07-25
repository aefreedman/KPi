from dothat import lcd
from dothat import backlight
from dothat import touch

import krpc

# pylint: disable-msg=C0103

print krpc.__version__

IP_ADDR = '192.165.1.125'
KRPC_PORT = 5000

_conn = krpc.connect(name='RPi', address=IP_ADDR)

vessel = _conn.space_center.active_vessel


# LCD
lcd.set_contrast(50)
lcd.set_cursor_position(0, 0)
backlight.rgb(200, 0, 0)
lcd.write(vessel)
