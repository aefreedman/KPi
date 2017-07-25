import time
import krpc
conn = krpc.connect(name='sub-orbital-flight', address='192.168.1.125', rpc_port=50000, stream_port=50001)

vessel = conn.space_center.active_vessel
vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)

print 'Launch!'
vessel.control.activate_next_stage()

while vessel.resources.amount('SolidFuel') > 0.1:
    time.sleep(1)
print 'Booster separation'
vessel.control.activate_next_stage()

vessel.auto_pilot.target_pitch_and_heading(80, 90)

while vessel.resources.amount('LiquidFuel') > 0.1:
    time.sleep(1)

print 'Second stage separation' 
vessel.control.activate_next_stage()

while vessel.flight().surface_altitude > 1000:
    time.sleep(1)
vessel.control.activate_next_stage()

while vessel.flight(vessel.orbit.body.reference_frame).vertical_speed < -0.1:
    print 'Altitude = %.1f meters' % vessel.flight().surface_altitude
    time.sleep(1)
print 'Landed' 
