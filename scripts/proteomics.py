import os, subprocess, multiprocessing
from pathlib import Path


def run(command):

    print(command)
    p = subprocess.Popen(command, shell=True)
    print(p.pid, end="\n\n")
    p.wait()


if __name__ == '__main__':

    proteomics_dir = Path("/pool/data/globus/proteomics")
    proteomics_input_dir = proteomics_dir / '1_wiff'
    wiffs = [f for f in proteomics_input_dir.glob('**/*.*') if f.is_file() and f.suffix == '.wiff']

    # ('/', 'pool', 'data', 'globus', 'proteomics', '1_wiff', '1_iPSC', 'iPSC', 'CTR-25_iPSC_rep3.wiff')
    # experiment = filepath.parts[6]
    # differentiation = filepath.parts[7]
    # filename = filepath.parts[8]

    for filepath in wiffs: os.makedirs(proteomics_dir / '2_mzml' / '/'.join(filepath.parts[6:8]), exist_ok=True)

    commands = [f"docker run -v {proteomics_dir}:/data:rw brightspark/wiffconverter:0.7 mono /usr/local/bin/sciex/wiffconverter/OneOmics.WiffConverter.exe WIFF /data/{'/'.join(filepath.parts[5:])} -profile MZML /data/2_mzml/{'/'.join(filepath.parts[6:8])}/{filepath.stem}.mzml" for filepath in wiffs]

    # print(commands)

    # pool = multiprocessing.Pool(processes=multiprocessing.cpu_count() / 8)

    # pool.map(run, commands)
