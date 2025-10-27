from pymavlink import mavutil

# Start connection through a UDP port
the_connection = mavutil.mavlink_connection("udpin:localhost:14551")

# Wait fo heartbeat
the_connection.wait_heartbeat()
print("heartbeat from (system %u component %u)" % 
      (the_connection.target_system, the_connection.target_component))

        