import sys
import yaml
import pystache

try:
    input_file = sys.argv[1]
except:
    input_file = 'conf.yaml'

with open(input_file) as inpf:
    conf = yaml.load(inpf)
    with open("/tmp/sccct.py", "w") as outf:
        outf.write(pystache.Renderer().render_path('nrn.mustache', conf))

    with open("/tmp/sccct.cell.nml", "w") as outf:
        outf.write(pystache.Renderer().render_path('nml.cell.mustache', conf))

    with open("/tmp/sccct.net.nml", "w") as outf:
        outf.write(pystache.Renderer().render_path('nml.net.mustache', conf))

    with open("/tmp/lems_sccct.xml", "w") as outf:
        outf.write(
            pystache.Renderer().render_path('lems.xml.mustache', conf))
