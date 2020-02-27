import nengo
import numpy as np

η = 0.5e-4

with nengo.Network() as model:
    nd_stim_us = nengo.Node(lambda t:
        (1.0 if 0.9 < (t % 1.0) < 1.0 else 0.0) *
        (1.0 if t < 15.0 else 0.0) *
        (1.0 if t > 1.0 else 0.0)
    )
    nd_stim_cs = nengo.Node(lambda t:
        (1.0 if 0.9 < (t % 1.0) < 1.0 else 0.0)
    )

    # Inputs
    ens_us = nengo.Ensemble(n_neurons=100, dimensions=1)
    ens_cs = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(nd_stim_us, ens_us)
    nengo.Connection(nd_stim_cs, ens_cs)

    # Unconditioned response
    ens_ur = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(ens_us, ens_ur)

    # Conditioned response
    ens_cr = nengo.Ensemble(n_neurons=100, dimensions=1)
    con = nengo.Connection(
        ens_cs,
        ens_cr,
        learning_rule_type=nengo.PES(η),
        transform=np.zeros((1, 1)))

    # Learning
    ens_err = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(ens_cr, ens_err, transform=1)
    nengo.Connection(ens_ur, ens_err, transform=-1)
    nengo.Connection(ens_err, con.learning_rule)

    # Total response
    ens_response = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(ens_cr, ens_response)
    nengo.Connection(ens_ur, ens_response)


