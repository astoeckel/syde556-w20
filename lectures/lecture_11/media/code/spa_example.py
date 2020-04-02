import nengo
from nengo import spa

D = 16

def start(t):
    if t < 0.05:
        return 'A'
    else:
        return '0'
    
model = spa.SPA(label='Sequence_Module', seed=5)

with model:
    model.cortex = spa.Buffer(dimensions=D, label='cortex')
    model.input = spa.Input(cortex=start, label='input')

    actions = spa.Actions(
        'dot(cortex, A) --> cortex = B',
        'dot(cortex, B) --> cortex = C',
        'dot(cortex, C) --> cortex = D',
        'dot(cortex, D) --> cortex = E',
        'dot(cortex, E) --> cortex = A'
    )
    model.bg = spa.BasalGanglia(actions=actions)
    model.thal = spa.Thalamus(model.bg)

