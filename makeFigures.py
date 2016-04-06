import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from turbines import turbines

if __name__=="__main__":
    """
    #Starting Points 1 and 2
    xHAWT = np.array([0,0,0,200,200,200,400,400,400,600,600,600,800,800,800])
    yHAWT = np.array([0,200,400,600,800,0,200,400,600,800,0,200,400,600,800])
    xVAWT = np.array([50,50,50,50,150,150,150,150,250,250,250,250,350,350,350,350,450,450,450,450,550,550,550,550,650,650,650,650,750,750,750,750])
    yVAWT = np.array([50,150,250,350,450,550,650,750,50,150,250,350,450,550,650,750,50,150,250,350,450,550,650,750,50,150,250,350,450,550,650,750])
    """
    """
    #Starting Points 3
    xHAWT = np.array([0,0,0,250,250,250,500,500,500])
    yHAWT = np.array([0,250,500,0,250,500,0,250,500])
    xVAWT = np.array([62.5,62.5,62.5,62.5,62.5,62.5,125,125,125,125,125,125,187.5,187.5,187.5,187.,187.5,187.5,312.5,312.5,312.5,312.5,312.5,312.5,375,375,375,375,375,375,437.5,437.5,437.5,437.5,437.5,437.5])
    yVAWT = np.array([62.5,125,187.5,312.5,375,437.5,62.5,125,187.5,312.5,375,437.5,62.5,125,187.5,312.5,375,437.5,62.5,125,187.5,312.5,375,437.5,62.5,125,187.5,312.5,375,437.5,62.5,125,187.5,312.5,375,437.5])
    """
    """
    #Starting Points 4
    xHAWT = np.array([0,0,0,250,250,250,500,500,500])
    yHAWT = np.array([0,250,500,0,250,500,0,250,500])
    xVAWT = np.array([0,0,0,0,83.33,83.33,83.33,83.33,83.33,83.33,83.33,166.66,166.66,166.66,166.66,166.66,166.66,166.66,250,250,250,250,333.33,333.33,333.33,333.33,333.33,333.33,333.33,416.66,416.66,416.66,416.66,416.66,416.66,416.66,500,500,500,500])
    yVAWT = np.array([83.33,166.66,333.33,416.66,0,83.33,166.66,250,333.33,416.66,500,0,83.33,166.66,250,333.33,416.66,500,83.33,166.66,333.33,416.66,0,83.33,166.66,250,333.33,416.66,500,0,83.33,166.66,250,333.33,416.66,500,83.33,166.66,333.33,416.66])
    """
    #Dustan's starting point for 25 turbines
    xHAWT = np.array([0,0,250,500,500])
    yHAWT = np.array([0,500,250,0,500])
    xVAWT = np.array([0, 0, 0, 125, 125, 125, 125, 125, 250, 250, 250, 250, 375, 375, 375, 375, 375, 500, 500, 500])
    yVAWT = np.array([125, 250, 375, 0, 125, 250, 375, 500, 0, 125, 375, 500, 0, 125, 250, 375, 500, 125, 250, 375])

    #Optimal Points
    filename = "dk_25_turbine_optimization.txt"
    file = open(filename)
    xin = np.loadtxt(file)
    nVAWT = len(xVAWT)
    nHAWT = len(xHAWT)
    xVAWT_opt, yVAWT_opt, xHAWT_opt, yHAWT_opt = turbines(xin, nVAWT)

    plt.figure(1)
    plt.scatter(xHAWT, yHAWT, c='r', s=50, label = "HAWT")
    plt.scatter(xVAWT, yVAWT, c='b', s=30, label = "VAWT")
    plt.title('Starting Locations')
    plt.ylabel('Y (m)')
    plt.xlabel('X (m)')
    #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=9, ncol=2, borderaxespad=0.)

    plt.figure(2)
    plt.scatter(xHAWT_opt, yHAWT_opt, c='r', s=50, label = "HAWT")
    plt.scatter(xVAWT_opt, yVAWT_opt, c='b', s=30, label = "VAWT")
    plt.title('Optimized Locations')
    plt.ylabel('Y (m)')
    plt.xlabel('X (m)')
    #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    font = {'family' : 'sans',
        'weight' : 'bold',
        'size'   : 15}
    matplotlib.rc('font', **font)

    plt.show()
    
