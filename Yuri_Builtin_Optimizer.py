from Main_Obj import *
from scipy.optimize import minimize


if __name__=="__main__":

	xHAWT = np.array([0, 0])
	yHAWT = np.array([0, 300])
	xVAWT = np.array([50])
	yVAWT = np.array([50])


	#Define Xin so that the optimizer understands it
	xin = np.hstack([xVAWT, yVAWT, xHAWT, yHAWT])

	#set input parameters
	nVAWT = len(xVAWT)
	nHAWT = len(xHAWT)
	rh = 40.
	rv = 3.
	rt = 5.
	direction = 15.   # Degrees
	dir_rad = (direction+90) * np.pi / 180.
	U_vel = 8.
	params = [nVAWT, rh, rv, rt, dir_rad, U_vel]
	print "Original Power: ", obj(xin, params)

	#-------------------------Optimization----------------------------------
	xupper = 2000 #x upper bound of the wind farm (lower set at 0)
	yupper = 1950 #y upper bound of the wind farm (lower set at 0)
	bound_con = bounds(xin, params, xupper, yupper)
	ineq_con = {'type': 'ineq', 'fun': con, 'args': (params,)}
	options = {'disp': True, 'maxiter': 2000}
	res = minimize(obj, xin, args = (params,), method = 'SLSQP', jac = False, bounds = bound_con, constraints = ineq_con, tol = 1e-6, options = options)
	optX = res.x
	optCON = con(optX, params)


	#--------------------------Plots-----------------------------------
	xVAWT_opt = optX[0 : nVAWT]
	yVAWT_opt = optX[nVAWT: 2*nVAWT]
	xHAWT_opt = optX[2*nVAWT: 2*nVAWT + nHAWT]
	yHAWT_opt = optX[2*nVAWT + nHAWT : len(xin)]

	plt.figure()
	plt.scatter(xVAWT, yVAWT,s=(np.pi*rv**2.), c = 'k')
	plt.scatter(xVAWT_opt, yVAWT_opt,s=(np.pi*rv**2.), c = 'r')
	plt.scatter(xHAWT, yHAWT,s=(15*np.pi*rt**2.), c = 'c')
	plt.scatter(xHAWT_opt, yHAWT_opt,s=(15*np.pi*rt**2.), c = 'g')
	plt.show()

