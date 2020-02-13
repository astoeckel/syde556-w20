import nengo
import numpy as np

# This code has been adapted from nengolib; https://github.com/arvoelke/nengolib
def make_delay_network(q, theta):
    Q = np.arange(q, dtype=np.float64)
    R = (2 * Q + 1)[:, None] / theta
    j, i = np.meshgrid(Q, Q)
    A = np.where(i < j, -1, (-1.)**(i - j + 1)) * R
    B = (-1.)**Q[:, None] * R
    return A, B

def make_nef_lti(tau, A, B):
    Ap = tau * A + np.eye(A.shape[0])
    Bp = tau * B
    return Ap, Bp
    
q = 6 # Number of state dimensions in the delay network
theta = 0.33 # Window being represented
tau = 0.1 # Synaptic filter time constant

# Compute the LTI system
A, B = make_delay_network(q, theta)
Ap = tau * A + np.eye(q)
Bp = tau * B

with nengo.Network() as model:

    # Stimulus alternating between a sine wave of frequencies f1 and f2
    def stim(t):
        f1 = 3.0 # Frequency 1
        f2 = 6.0 # Frequency 2
        phase = t % 4.0
        if phase < 1.0:
            return 0.0
        elif phase < 2.0:
            return np.sin(f1 * 2.0 * np.pi * (phase - 1.0))
        elif phase < 3.0:
            return 0.0
        elif phase  < 4.0:
            return np.sin(f2 * 2.0 * np.pi * (phase - 3.0))

    # Training signals
    def target_1(t):
        return 1.0 < (t % 4.0) < 2.0

    def target_2(t):
        return 3.0 < (t % 4.0) < 4.0

    # Build the delay network
    nd_stim = nengo.Node(stim)
    ens_x = nengo.Ensemble(
        n_neurons = 500,
        dimensions = q,
        intercepts = nengo.dists.CosineSimilarity(q + 2),
    )
    nengo.Connection(nd_stim, ens_x, transform=Bp, synapse=tau)
    nengo.Connection(ens_x, ens_x, transform=Ap, synapse=tau)

    # Nodes representing which tone has been playing
    ens_tone_1 = nengo.Ensemble(
        n_neurons = 100,
        dimensions = 1
    )
    ens_tone_2 = nengo.Ensemble(
        n_neurons = 100,
        dimensions = 1
    )

    # Nodes containing the training signal
    nd_target_1 = nengo.Node(target_1)
    nd_target_2 = nengo.Node(target_2)

    # Connections from the Delay Network onto the ensembles deciding which tone
    # has been played
    con_tone_1 = nengo.Connection(
        ens_x, ens_tone_1,
        transform=np.zeros((1, q)),
        learning_rule_type=nengo.PES(
            learning_rate=1e-4,
        ),
    )
    con_tone_2 = nengo.Connection(
        ens_x, ens_tone_2,
        transform=np.zeros((1, q)),
        learning_rule_type=nengo.PES(
            learning_rate=1e-4,
        ),
    )

    # Nodes representing the training error
    nd_err_1 = nengo.Node(size_in=1)
    nd_err_2 = nengo.Node(size_in=1)

    nengo.Connection(nd_target_1, nd_err_1, transform=-1)
    nengo.Connection(ens_tone_1, nd_err_1)
    nengo.Connection(nd_err_1, con_tone_1.learning_rule)

    nengo.Connection(nd_target_2, nd_err_2, transform=-1)
    nengo.Connection(ens_tone_2, nd_err_2)
    nengo.Connection(nd_err_2, con_tone_2.learning_rule)
