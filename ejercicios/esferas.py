from vpython import *
# Creacion de esferas
sphere(pos = vec(0, -1, 0), radius=0.5, color=color.blue)
# Creacion de flechas
arrow(pos = vec(0, -1, 0), axis=vec(+1, -1, 0), color=color.blue)

# Asinacion de objetos a variables
particula1 = sphere(pos=vec(3, -1, 0), radius=0.5, color=color.green)
particula2 = sphere(pos=vec(0, -1, 4), radius=0.5, color=color.red)

# Asignacion de posicion de un objeto a otro
arrow(pos = particula1.pos, axis=particula2.pos-particula1.pos , color=color.blue)

n=1
r=vec(1, -1, 0)

while r.x < 10:
    rate(10)
    # Varias esferas en simultaneo
    # sphere(pos=r, radius=0.5, color=color.blue)
    r.x = r.x + 1
    # Animacion de esfera
    particula1.pos = r

# GlowScript 1.1 VPython

L0 = 1.1  # the natural length of the spring
k = 15  # spring constant

# the holder is the top plate for the spring
holder = box(pos=vec(-0.1, 0.1, 0), size=vec(1.1, .5, 1.1))

# the ball and the spring should be obvious
# note that the ball has a trail
ball = sphere(pos=vec(-0.1, -L0 + 0.1, 0), radius=0.02, color=color.red)
spring = helix(pos=holder.pos, axis=ball.pos - holder.pos, radius=0.02, coils=10)

ball.m = 0.1  # mass of the ball in kg
ball.p = ball.m * vec(0, 0, 0)  # starting momentum mass times velocity

dr = vec(0, -0.05, 0)  # this is the displacement of the spring
ball.pos = ball.pos + dr

g = vec(0, -9.8, 0)  # gravitational field
t = 0
dt = 0.01  # size of the time step

# putting the loop as "while True" means it runs forever
# you could change this to while t< 10: or something
while t < 3:
    rate(100)  # this says 100 calculations per second

    # L is the length of the spring, from the holder to the ball
    L = ball.pos - holder.pos

    # remember that mag(R) gives the magnitude of vector R
    # remember that norm(R) gives the unit vector for R
    Fs = -k * (mag(L) - L0) * norm(L)  # this is Hooke's law

    # this calculates the net force
    F = Fs + ball.m * g

    # update the momentum
    ball.p = ball.p + F * dt

    # update the position of the ball
    ball.pos = ball.pos + ball.p * dt / ball.m
    # this next line updates the spring
    spring.axis = ball.pos - holder.pos