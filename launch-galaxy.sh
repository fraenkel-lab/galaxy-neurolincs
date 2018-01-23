#!/bin/bash

sudo cp /etc/slurm-llnl/slurm.conf /pool/data/galaxy/
sudo cp /etc/munge/munge.key /pool/data/galaxy/

docker run -d \
	--name=galaxy \
	--restart=on-failure \
	--privileged=true \
	-v /pool/data/galaxy/:/export/ \
	-v /pool/data/globus/:/globus/ \
	-v /pool/data/galaxy_venv/:/galaxy_venv/ \
	-p 80:80 \
	-p 8021:21 \
	-p 8022:22 \
	-p 443:443 \
	-p 8800:8800 \
	-p 9002:9002 \
	-e "NONUSE=slurmd,slurmctld" \
	-e "USE_HTTPS_LETSENCRYPT=True" \
	-e "GALAXY_ROOT=/export/galaxy-central" \
        -e "GALAXY_CONFIG_GALAXY_INFRASTRUCTURE_URL=answer.csbi.mit.edu" \
	-e "galaxy_extras_config_condor=False" \
	-e "galaxy_extras_config_condor_docker=False" \
	quay.io/fraenkel_lab/galaxy-neurolincs


# for testing (and to keep data from persisting) this command is sufficient:
# docker run -d -p 80:80 -p 9002:9002 quay.io/fraenkel_lab/galaxy-neurolincs

# for testing with globus integration:
# docker run -d -p 80:80  -p 21:21 -p 8800:8800 -p 9002:9002 -p 2811:2811 -p 2223:2223 -p 7512:7512 -p 50000-51000:50000-51000 quay.io/fraenkel_lab/galaxy-neurolincs

