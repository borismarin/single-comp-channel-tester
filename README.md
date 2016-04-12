## Single Cell - Channel tester

The .py file ([scct.py](https://github.com/borismarin/single-comp-channel-tester/blob/master/scct.py)) compares different ion channels (specified in .mod/.channel.nml files), listed in a .yaml file ([Saraga2003.yaml](https://github.com/borismarin/single-comp-channel-tester/blob/master/Saraga2003.yaml)) using [NEURON](https://www.neuron.yale.edu/neuron/) as simulation environment.

The script can be run locally using python after [installing NEURON](https://www.neuron.yale.edu/neuron/download)
    git clone https://github.com/borismarin/single-comp-channel-tester.git # clone GitHub repository
    cd single-comp-channel-tester
    python scct.py  # will run the example file (Saraga.yaml), or:
    python scct.py "filename.yaml"

> Note: to use the script to compare .mod files with .nml files one has to install [pyNeuroML](https://github.com/NeuroML/pyNeuroML) and [libNeuroML](https://github.com/NeuralEnsemble/libNeuroML)!
