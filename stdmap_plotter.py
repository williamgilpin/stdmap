# This script generates phase space portraits for the standard map at many different values of the "kicking" parameter L
# William Gilpin, 2014

from numpy import *
from scipy import *
from matplotlib.pyplot import *

from random import randrange

# steps to run simulation for (generally only needs a few
# to sketch full limit cycles)

N = 150;

def stdmap((x, p)):
    pn = mod(p + K*sin(x), 2*pi)
    xn = mod(x + pn, 2*pi)
    return (xn, pn)

 # make the mesh for phase space
x0 = linspace(0, 2*pi, 7)
p0 = linspace(0, 2*pi, 8)
mesh = list()
for ii in xrange(len(x0)):
    for jj in xrange(len(p0)):
        mesh.append((x0[ii], p0[jj]))

Kvals = linspace(.1,2*pi,10)


for val in Kvals:
    K = val
    fig = figure(figsize=(5, 5))
    for item in mesh:
        traj = [item]
        for ii in xrange(N):
            traj.append(stdmap(traj[ii]))
        plot(array(traj).T[0], array(traj).T[1],'.')
        hold(True)

    xlim([0, 2*pi])
    ylim([0, 2*pi])
    xlabel('Position (rad)')
    ylabel('Momentum')
    show()
#   savefig('stdmap_'+ str(round(K, 5))+'.png')






