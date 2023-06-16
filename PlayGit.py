import numpy as np
import matplotlib.pyplot as plt
import random
import math as math

xcoor = [0]
ycoor = [0]

vf = [0,0,0]
v_f = np.array(vf)

thymes = int(input("Diffusion has occurred!\nHow many times would you like to ray trace? "))
while thymes > 0:
    z1 = random.uniform(0,1)
    z2 = random.uniform(0,1)
    fi = (math.acos(math.sqrt(z1))) 
    theta = z2 * np.pi
    print(fi,"\n",theta)
    direction1 = [math.cos(fi),math.sin(fi),1]
    direction2 = [math.sin(theta),math.cos(theta),math.cos(theta)]
    d1 = np.array(direction1)
    d2 = np.array(direction2)
    direction = d1 * d2
    print("\n",direction1,"\n",direction2)
    print("This is the direction ",direction,"\n")
    addition = 1 * direction
    finalstep = v_f + addition
    xcoor.append(finalstep[0])
    ycoor.append(finalstep[2])
    plt.plot(xcoor,ycoor)
    xcoor.pop()
    ycoor.pop()
    thymes = thymes - 1


plt.axvline(x=0,color='black')
plt.axhline(y=0,color='black')
plt.show() 