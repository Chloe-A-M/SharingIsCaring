import numpy as np
import matplotlib.pyplot as plt
import random
import math as math
from operator import mul


x = int(input("Enter initial x coordinate: "))
y = int(input("Enter initial y coordinate: "))
z = int(input("Enter initial z coordinate: "))

initial = [x,y,z]

v_i = np.array(initial)

print("Your initial coordinates are ",v_i)

fid = int(input("Enter azimuthal angle in degrees: "))
thetad = int(input("Enter elevation angle in degrees: "))

fi = math.radians(fid)
theta = math.radians(thetad)

direction1 = [math.cos(fi),math.sin(fi),1]
direction2 = [math.sin(theta),math.cos(theta),math.cos(theta)]

d1 = np.array(direction1)
d2 = np.array(direction2)

direction = d1 * d2

print("Your direction vector is",direction)

raypath = int(input("Enter the spatial step in meters: "))

addition = raypath * direction

v_f = v_i + addition

xcoor = [initial[0]]
ycoor = [initial[1]]
zcoor = [initial[2]]

while v_f[2] > 0:
    xcoor.append(v_f[0])
    ycoor.append(v_f[1])
    zcoor.append(v_f[2])
    v_f = v_i + addition
    if v_f[2] <= 0:
        v_0 = v_i[2]
        v_d = direction[2]
        l = (-1*v_0) / v_d
        v_f = (direction * l) + v_i
        xcoor.append(v_f[0])
        ycoor.append(v_f[1])
        zcoor.append(v_f[2])
        nom = [0,0,1]
        break
    elif v_f[0] <= 0:
        v_0 = v_i[0]
        v_d = direction[0]
        l = (-1*v_0) / v_d
        v_f = (direction * l) + v_i
        xcoor.append(v_f[0])
        ycoor.append(v_f[1])
        zcoor.append(v_f[2])
        #this makes it do what we want, ask why, [1,0,1]
        nom = [1,0,1]
        break
    v_i = v_f

print(v_f)

thymes = int(input("Diffusion has occurred!\nHow many times would you like to ray trace? "))
while thymes > 0:
        z1 = random.uniform(0,1)
        z2 = random.uniform(0,1)
        theta = (math.acos(math.sqrt(z1)))
        fi = 2 * np.pi * z2
        direction1 = [math.cos(fi),math.sin(fi),1]
        direction2 = [math.sin(theta),math.cos(theta),math.cos(theta)]
        d1 = np.array(direction1)
        d2 = np.array(direction2)
        direction = d1 * d2
        if v_f[0] == 0:
            normal = np.array(nom)
            dots = sum(map(mul, normal, direction))
            dot = dots * -1
            norm = sum(map(mul, normal, normal))
            a = (dot/norm) * normal
            reflec = direction + (2*a)
            finalstep = v_f + reflec
        elif v_f[2] == 0:
            finalstep = v_f + direction
        xcoor.append(finalstep[0])
        ycoor.append(finalstep[1])
        zcoor.append(finalstep[2])
        plt.plot(xcoor,zcoor)
        xcoor.pop()
        ycoor.pop()
        zcoor.pop()
        thymes = thymes - 1
plt.show()














