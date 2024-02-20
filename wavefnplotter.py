import matplotlib.pyplot as plt
import numpy as np



def plot(psi, V, x0, xf, dx):
	plt.clf()
	plt.ioff()
	fig = plt.figure(figsize=(10, 20), layout='constrained')
	plots = fig.subplot_mosaic([["psiPlot1"]])

	plotId = "psiPlot1"

	plots[plotId].set_title("Placeholder Title")
	plots[plotId].set_xlabel("Position (*units*)")
	plots[plotId].set_ylabel("Y-axis title")
	
	xArray = np.arange(x0, xf, dx)
	nsteps = len(xArray)
	VArray = np.zeros(nsteps)
	psiArray = np.zeros(nsteps)

	for i in range(nsteps):
		VArray[i] = V(xArray[i])
		psiArray[i] = psi(xArray[i])
	
	plots[plotId].plot(xArray, VArray, label="Potential V(x)")
	plots[plotId].plot(xArray, psiArray, label="Wavefunction Ψ(x)")
	plots[plotId].legend()

	plt.show()





#ψ(x)