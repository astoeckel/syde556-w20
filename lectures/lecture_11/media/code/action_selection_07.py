import nengo
import numpy as np

model = nengo.Network('Selection')

with open('statespace.svg', 'r') as f:
    svg = f.read()

with model:
    def statespace(t, x):
        statespace._nengo_html_ = \
            svg.replace("0.222", str(x[0] + 0.51)).replace("0.333", str(-x[1] + 0.30))
        return x
    nd_stim = nengo.Node(statespace, size_in=2)
    nd_in = nengo.Node(size_in=2)
    nengo.Connection(nd_in, nd_stim)

    ens_s = nengo.Ensemble(200, dimensions=2)
    nengo.Connection(nd_stim, ens_s)

    ear_Qs = nengo.networks.EnsembleArray(50, n_ensembles=4)
    nengo.Connection(ens_s, ear_Qs.input, transform=[[1,0],[-1,0],[0,1],[0,-1]])

    net_basal_ganglia = nengo.networks.BasalGanglia(dimensions=4)

    nengo.Connection(ear_Qs.output, net_basal_ganglia.input, synapse=None)
