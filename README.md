## Single Cell - Channel tester

The .py file ([scct.py](https://github.com/borismarin/single-comp-channel-tester/blob/master/scct.py)) compares different ion channels (specified in .mod/.channel.nml files), listed in a .yaml file using [NEURON](https://www.neuron.yale.edu/neuron/) as simulation environment.

The script can be run locally using python after [installing NEURON](https://www.neuron.yale.edu/neuron/download)

    git clone https://github.com/borismarin/single-comp-channel-tester.git # clone GitHub repository
    cd single-comp-channel-tester
    python scct.py  # will run the example file (Saraga.yaml), or:
    python scct.py "filename.yaml"

> Note: if you want to use the script only with .mod files, set nml=False in the code!

The example .yaml file ([Saraga2003.yaml](https://github.com/borismarin/single-comp-channel-tester/blob/master/Saraga2003.yaml)) compares the original .mod from Saraga et al. 2003 [J Physiol 552(3):673-689](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2343469/pdf/tjp0552-0673.pdf) hippocampal CA1 O-LM interneuron with the NeuroML2 channel.nml version of the same model, hosted by [OpenSourceBrain](http://opensourcebrain.org/projects/ca1-oriens-lacunosum-moleculare-saraga-et-al-2003) 

![](https://raw.githubusercontent.com/borismarin/single-comp-channel-tester/master/compare_channels.png)

> Note: to use the script to compare .mod files with .nml files one has to install [pyNeuroML](https://github.com/NeuroML/pyNeuroML) and [libNeuroML](https://github.com/NeuralEnsemble/libNeuroML) !

