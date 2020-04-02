import nengo
from nengo.dists import Uniform
import numpy as np

mm=1
mp=1
me=1
mg=1

#connection strengths from original model
ws=1
wt=1
wm=1
wg=1
wp=0.9
we=0.3

#neuron lower thresholds for various populations
e=0.2  
ep=-0.25
ee=-0.2
eg=-0.2

le=0.2
lg=0.2

D = 10
tau_ampa=0.002
tau_gaba=0.008
N = 50
radius = 1.5

model = nengo.Network('Basal Ganglia', seed=4)

with model:
    stim = nengo.Node([0]*D)

    StrD1 = nengo.networks.EnsembleArray(N, n_ensembles=D, intercepts=Uniform(e,1), 
                                 encoders=Uniform(1,1), radius=radius)
    StrD2 = nengo.networks.EnsembleArray(N, n_ensembles=D, intercepts=Uniform(e,1), 
                                 encoders=Uniform(1,1), radius=radius)
    STN = nengo.networks.EnsembleArray(N, n_ensembles=D, intercepts=Uniform(ep,1), 
                                 encoders=Uniform(1,1), radius=radius)
    GPi = nengo.networks.EnsembleArray(N, n_ensembles=D, intercepts=Uniform(eg,1), 
                                 encoders=Uniform(1,1), radius=radius)
    GPe = nengo.networks.EnsembleArray(N, n_ensembles=D, intercepts=Uniform(ee,1), 
                                 encoders=Uniform(1,1), radius=radius)

    nengo.Connection(stim, StrD1.input, transform=ws*(1+lg), synapse=tau_ampa)
    nengo.Connection(stim, StrD2.input, transform=ws*(1-le), synapse=tau_ampa)
    nengo.Connection(stim, STN.input, transform=wt, synapse=tau_ampa)
    
    def func_str(x): #relu-like function
        if x[0]<e: return 0
        return mm*(x[0]-e)
    strd1_out = StrD1.add_output('func_str', func_str)
    strd2_out = StrD2.add_output('func_str', func_str)
    
    nengo.Connection(strd1_out, GPi.input, transform=-wm, synapse=tau_gaba)
    nengo.Connection(strd2_out, GPe.input, transform=-wm, synapse=tau_gaba)
    
    def func_stn(x):
        if x[0]<ep: return 0
        return mp*(x[0]-ep)
    stn_out = STN.add_output('func_stn', func_stn)
    
    tr=[[wp]*D for i in range(D)]    
    nengo.Connection(stn_out, GPi.input, transform=tr, synapse=tau_ampa)
    nengo.Connection(stn_out, GPe.input, transform=tr, synapse=tau_ampa)

    def func_gpe(x):
        if x[0]<ee: return 0
        return me*(x[0]-ee)
    gpe_out = GPe.add_output('func_gpe', func_gpe)
    
    nengo.Connection(gpe_out, GPi.input, transform=-we, synapse=tau_gaba)
    nengo.Connection(gpe_out, STN.input, transform=-wg, synapse=tau_gaba)

    Action = nengo.networks.EnsembleArray(N, n_ensembles=D, intercepts=Uniform(0.2,1), 
                             encoders=Uniform(1,1))
    bias = nengo.Node([1]*D)
    nengo.Connection(bias, Action.input)
    nengo.Connection(Action.output, Action.input, transform=(np.eye(D)-1), synapse=tau_gaba)
    
    def func_gpi(x):
        if x[0]<eg: return 0
        return mg*(x[0]-eg)
    gpi_out = GPi.add_output('func_gpi', func_gpi)
    
    nengo.Connection(gpi_out, Action.input, transform=-3, synapse=tau_gaba)
