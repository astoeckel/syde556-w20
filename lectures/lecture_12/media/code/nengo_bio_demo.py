import nengo
import nengo_bio as bio
import numpy as np

with nengo.Network() as model:
    nd_in = nengo.Node(size_in=1)

    ens_A = bio.Ensemble(n_neurons=101, dimensions=1, p_exc=1.0)
    ens_B = bio.Ensemble(n_neurons=102, dimensions=1)
    ens_C = bio.Ensemble(n_neurons=102, dimensions=1, p_inh=1.0)

    nengo.Connection(nd_in, ens_A)
    bio.Connection(ens_A, ens_C)
    bio.Connection({ens_A, ens_C}, ens_B)

#    bio.Connection(
#        (ens_A, ens_C), ens_B, transform=[[1, 0]])