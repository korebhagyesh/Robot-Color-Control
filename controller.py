from controller import Robot
import socket

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Setup UDP Receiver
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(False)
sock.bind(("127.0.0.1", 5005))

while robot.step(timestep) != -1:
    try:
        data, _ = sock.recvfrom(1024)
        x = float(data.decode())
        
        # Drive logic
        if x < 0.4: # Left
            left_motor.setVelocity(-2)
            right_motor.setVelocity(2)
        elif x > 0.6: # Right
            left_motor.setVelocity(2)
            right_motor.setVelocity(-2)
        else: # Forward
            left_motor.setVelocity(5)
            right_motor.setVelocity(5)
    except:
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)