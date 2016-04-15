import sys
import yaml
import pystache
from subprocess import Popen, PIPE

def preprocess(conf):

    conf["resistivity"] = 1.0/float(conf.get("passive", {'g':1})['g'])

    return conf


def convert_channels_to_mod(lems_file):

    from pyneuroml import pynml

    pynml.run_jneuroml("", lems_file, "-neuron")


def command_line(cmd):
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    [out, err] = p.communicate()
    print out


def compile_channel_files():
    
    cmd = ["rm", "-rf", "x86_64"]  # just to make sure: deletes existing x86_64
    command_line(cmd)

    cmd = ["nrnivmodl"]
    command_line(cmd)


def main(nml, nrn_file):

    try:
        input_file = sys.argv[1]
    except:
        input_file = 'Saraga2003.yaml'

    with open(input_file) as inpf:

        conf = yaml.load(inpf)
        conf = preprocess(conf)

        if nml:

            with open(".sccct_generated.cell.nml", "w") as outf:
                outf.write(pystache.Renderer().render_path('nml.cell.mustache', conf))

            with open(".sccct_generated.net.nml", "w") as outf:
                outf.write(pystache.Renderer().render_path('nml.net.mustache', conf))

            from neuroml.utils import validate_neuroml2
            validate_neuroml2(".sccct_generated.cell.nml")
            validate_neuroml2(".sccct_generated.net.nml")

            lems_file = "LEMS_sccct_generated.xml"        
            with open(lems_file, "w") as outf:
                outf.write(pystache.Renderer().render_path('lems.xml.mustache', conf))
        
            convert_channels_to_mod(lems_file)
   
        with open(nrn_file, "w") as outf:
            outf.write(pystache.Renderer().render_path('nrn.mustache', conf))

        compile_channel_files()



if __name__ == '__main__':

    nml = True  # set True to work with .channel.nml files instead of comparing only .mod files
    nrn_file = "compare_modfiles.nrn.py"

    main(nml, nrn_file)

    cmd = ["nrngui", nrn_file]
    command_line(cmd)

    









