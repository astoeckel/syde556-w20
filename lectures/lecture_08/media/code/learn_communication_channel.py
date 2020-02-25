import nengo
import numpy as np
import matplotlib.pyplot as plt

η = 1e-5
T = 10.0
f = lambda x: x

with nengo.Network() as model:
    nd_stim = nengo.Node(nengo.processes.WhiteSignal(
        period=T, high=1.0, rms=0.5))
    ens_x = nengo.Ensemble(n_neurons=100, dimensions=1)
    ens_y = nengo.Ensemble(n_neurons=100, dimensions=1)

    ens_err = nengo.Ensemble(n_neurons=100, dimensions=1)
    ens_tar = nengo.Ensemble(n_neurons=100, dimensions=1)

    nengo.Connection(nd_stim, ens_x)
    nengo.Connection(nd_stim, ens_tar, function=f)
    nengo.Connection(ens_tar, ens_err, transform=-1.0)
    nengo.Connection(ens_y,   ens_err, transform= 1.0)

    con = nengo.Connection(ens_x, ens_y,
                           learning_rule_type=nengo.PES(learning_rate=η),
                           transform=np.zeros((1, 1)))
    nengo.Connection(ens_err, con.learning_rule)
