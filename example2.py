import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
#from database_call import vorticity,velocity
from VAWT_Wake_Model import velocity_field
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'

# Enter the values desired

velf = 15.0 # free stream wind speed (m/s)
dia = 6.0  # turbine diameter (m)
tsr = 4.0  # tip speed ratio
B = 3. # number of blades
chord = 0.25 # chord lenth (m)
solidity = (chord*B)/(dia/2.)

# Enter the positions of the turbine and velocity calculation
xt = 0. # downstream position of turbine in flow domain (m)
yt = 0. # later position of turbine in flow domain (m)
x0 = 0. # downstream distance from turbine for velocity calculation (m)
y0 = 1000000. # lateral distance from turbine for velocity calculation (m)

# Choose whether CFD vorticity or velocity data will be used as the basis
#cfd_data = 'vort'
cfd_data = 'velo'

if cfd_data == 'vort':
    loc,spr,skw,scl = vorticity(tsr,solidity)
    param = np.array([loc,spr,skw,scl])
elif cfd_data == 'velo':
    #men,spr,scl,rat,tns = velocity(tsr,solidity)
    men = np.array( [-0.0006344223751663201, 0.01055675755786011, -0.004073212523707764] )
    spr = np.array( [-0.005187125854670714, 0.06397918461247416, 0.543874357807372] )
    scl = np.array( [6.667328694868336, 5.617498827673229, 21.520026361522778] )
    rat = np.array( [-2.129054494312758, 45.17191461412915] )
    tns = np.array( [-1.5569348878268718, 31.913143231782648] )
    param = np.array([men,spr,scl,rat,tns])

# print param
# print tsr,solidity
# import time
# time.sleep(10)
vel = velocity_field(xt,yt,xt + x0,yt + y0,velf,dia,tsr,solidity,cfd_data,param)

print '\nNormalized velocity at (',x0,',',y0,') from the turbine =',vel,'\n' # output velocity (normalized by free stream wind speed)

## Plotting
fs = 18 # font size for plots

# Option to plot velocity profiles
vel_slice = False
vel_slice = False # comment this out if desired on

# Option to plot a full velocity domain
plot_dist = False
# plot_dist = False # comment this out if desired on

# Plotting velocity profiles
if vel_slice == True:
    leng = 100 # data points in the velocity profile
    wide = 2.0*dia # width of the profile
    
    d_lab1 = str(wide/dia) # y-axis label
    d_lab2 = str(wide/(2*dia)) # y-axis label
    
    x = np.array([2*dia,4*dia,6*dia,8*dia,10*dia,15*dia]) # plotting at 2D, 4D, 6D, 8D, 10D, and 15D (changeable)
    y = np.linspace(-wide,wide,leng)
    
    color = np.array(['b','c','g','y','r','m']) # identifying six colors to use for differentiation
    
    iterp = 0
    for i in range(int(np.size(x))):
        vel = np.array([])
        val = str(x[i]/dia)
        lab = '$x/D$ = '+val
        for j in range(int(np.size(y))):
            velp = velocity_field(xt,yt,x[i],y[j],velf,dia,tsr,solidity,cfd_data,param)
            vel = np.append(vel,velp)
            iterp += 1
            print 'Vel Slice ('+str(iterp)+' of '+str(leng*np.size(x))+')'
        plt.figure(1)
        plt.plot(vel,y,color[i],label=lab)
    
    tix = np.array([-wide,-wide/2.,0.,wide/2.,wide])
    tixl = np.array([d_lab1,d_lab2,'0.0',d_lab2,d_lab1])
    # plt.legend(loc="upper left",bbox_to_anchor=(1, 1),fontsize=fs) # legend off to the side
    plt.legend(loc=2,fontsize=fs) # legend in the plot
    plt.xlim(0.,1.2)
    plt.ylim(-wide,wide)
    plt.xticks(fontsize=fs)
    plt.yticks(tix,tixl,fontsize=fs)
    plt.xlabel(r'$u/U_\infty$', fontsize=fs)
    plt.ylabel('$y/D$',fontsize=fs)

    # Plotting full velocity domain
if plot_dist == True:
    xi = -3.*dia # starting point in downstream direction
    xf = 17.0*dia # ending point in downstream direction
    yd = -2.5*dia # lateral extent on down side
    yu = 2.5*dia # lateral extent on up side
    
    N = 100 # N**2 = number of data points in domain
    
    xp = np.linspace(xi,xf,N)
    yp = np.linspace(yd,yu,N)
    [X, Y] = np.meshgrid(xp,yp)
    VEL = np.zeros((N, N)) # initiallizing velocity data point array
    
    iter = 0
    for i in range(N):
        for j in range(N):
            VEL[i,j] = velocity_field(xt,yt,X[i,j],Y[i,j],velf,dia,tsr,solidity,cfd_data,param)
            iter = iter +1
            print 'Plot ('+str(iter)+' of '+str(N*N)+')'
    
    plt.figure(2)
    lb = 0.15 # lower bound on velocity to display
    ub = 1.15 # upper bound on velocity to display
    ran = 32 # number of contours between the velocity bounds
    bounds = np.linspace(lb,ub,ran)
    v = np.linspace(lb,ub,6) # setting the number of tick marks on colorbar
    CS = plt.contourf(X/dia,Y/dia,VEL,ran,vmax=ub,vmin=lb,levels=bounds,cmap=plt.cm.coolwarm) # plotting the contour plot
    CB = plt.colorbar(CS, ticks=v) # creating colorbar
    CB.ax.set_ylabel(r'$u/U_\infty$',fontsize=fs)
    CB.ax.tick_params(labelsize=fs)
    CB.ax.set_aspect(40)
    plt.xlabel('$x/D$',fontsize=fs)
    plt.ylabel('$y/D$',fontsize=fs)
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    circ = plt.Circle((xt/dia,yt/dia),0.5,edgecolor='k',fill=False)
    plt.gca().add_patch(circ)

plt.show()
