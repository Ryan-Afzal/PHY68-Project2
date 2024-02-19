import matplotlib.pyplot as plt
import numpy as np

plt.ioff()
fig = plt.figure(figsize=(10, 20), layout='constrained')
plots = fig.subplot_mosaic([["psiPlot1", "psiPlot1"],
                            ["psiPlot1", "psiPlot1"]])

plots["psiPlot1"].set_title("Placeholder Title")
plots["psiPlot1"].set_xlabel("Position (*units*)")
plots["psiPlot1"].set_ylabel("Y-axis title")
plots["psiPlot1"].set_ylim(0, 10)

def plot(psi, V, x0, xf, dx):
	plot("psiPlot1", psi, V, x0, xf, dx)

def plot(plotId, psi, V, x0, xf, dx):
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





#ψ(x)