import nengo
import numpy as np
from nengo.processes import Piecewise

with nengo.Network() as model:
    tau = 100e-3
    omega = 1.0 * (2.0 * np.pi)

    nd_stim = nengo.Node(Piecewise({
        0.0: 100.0,
        0.1: 0.0,
    }))
    nd_speed = nengo.Node(lambda t: 1.0)

    ens_x = nengo.Ensemble(
        n_neurons=500, dimensions=3,
    )
    def fp(x):
        return np.array([
            [1.0, -x[2] * tau * omega],
            [x[2] * tau * omega, 1.0]
        ], dtype=float) @ x[0:2]


    nengo.Connection(ens_x, ens_x[0:2], function=fp, synapse=tau)
    nengo.Connection(nd_stim, ens_x[0])
    nengo.Connection(nd_speed, ens_x[2])
