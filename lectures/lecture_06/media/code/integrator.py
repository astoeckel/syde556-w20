import nengo
import numpy as np
from nengo.processes import Piecewise

with nengo.Network() as model:
    nd_stim = nengo.Node(Piecewise({
        1.0: 1.0,
        2.0: 0.0,
    }))
    ens_x = nengo.Ensemble(
        n_neurons=100, dimensions=1,
    )
    
    tau = 100e-3

    A = np.array([
        [0.0]
    ], dtype=float)

    B = np.array([
        [1.0]
    ], dtype=float)

    Ap = tau * A + np.eye(A.shape[0])
    Bp = tau * B

    nengo.Connection(ens_x, ens_x, transform=Ap, synapse=tau)
    nengo.Connection(nd_stim, ens_x, transform=Bp, synapse=tau)
