import os
import subprocess
import json

from metaquantome.util.utils import BASE_DIR
from metaquantome.SampleGroups import SampleGroups


def run_viz(plottype, img, infile,
            mode=None, meancol=None, nterms='5', target_rank=None, barcol=None,  # barplot
            textannot=None, fc_name=None, flip_fc=False, gosplit=False,  # volcano
            sinfo=None, filter_to_sig=False, alpha='0.05',  # heatmap
            calculate_sep=False,  # pca
            width='5', height='5'):
    r_script_path = os.path.join(BASE_DIR, 'analysis', 'viz.R')
    FNULL = open(os.devnull, 'w')
    cmd = ['Rscript', '--vanilla', r_script_path, plottype, img, infile]
    if plottype == "bar":
        cmd += [mode, meancol, nterms, str(width), str(height), str(target_rank), str(barcol)]
    elif plottype == "volcano":
        cmd += [str(textannot), fc_name, str(flip_fc), str(gosplit), str(width), str(height)]
    elif plottype == "heatmap":
        samp_grps = SampleGroups(sinfo)
        all_intcols_str = ','.join(samp_grps.all_intcols)
        json_dump = json.dumps(samp_grps.sample_names)
        cmd += [all_intcols_str, json_dump, str(filter_to_sig), alpha, width, height]
    elif plottype == "pca":
        samp_grps = SampleGroups(sinfo)
        all_intcols_str = ','.join(samp_grps.all_intcols)
        json_dump = json.dumps(samp_grps.sample_names)
        cmd += [all_intcols_str, json_dump, str(calculate_sep), width, height]
    else:
        ValueError("Wrong plot type. Must be bar, volcano, heatmap, or pca.")
    subprocess.run(cmd, stdout=FNULL)
    FNULL.close()
    return 0