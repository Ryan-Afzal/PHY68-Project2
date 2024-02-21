from typing import Callable
import scipy.integrate as integrate
import math

hbar = 1
m = 1

def solve_ode(V: Callable[[float], float], E: float, x0: float, xf: float, y0: float, dy0: float) -> Callable[[float], float]:
	"""Solve the TISE system of first-order ODEs.
	Parameters:
		V: The potential function V(x)
		E: The specified energy level
		x0: Start x
		xf: Final x
		y0: Value of ψ(x0)
		dy0: Value of ψ'(x0)
	"""
	# Create the ODE system
	f = lambda x, y: [y[1], -((2*m)/(math.pow(hbar, 2)))*(E - V(x))*y[0]]

	# Solve the ODE system
	solution = integrate.solve_ivp(f, [x0, xf], [y0, dy0], dense_output=True)

	if (not solution.success):
		print (f'Integration Failed, status={solution.status}')
		print ("\t" + solution.message)

	# Return the function containing its values.
	psi = lambda x: solution.sol(x)[0]

	return psi

