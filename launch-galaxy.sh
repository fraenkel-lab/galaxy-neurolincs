#!/bin/bash

docker run -d \
	--name=galaxy \
	--restart=on-failure \
	--privileged=true \
	-v /home/galaxy/galaxy_storage/:/export/ \
	-p 80:80 \
	-p 8021:21 \
	-p 8022:22 \
	-p 443:443 \
	-p 8800:8800 \
	-p 9002:9002 \
	alenail/galaxy-neurolincs

# for testing (and to keep data from persisting) this command is sufficient:
# docker run -d -p 80:80 -p 9002:9002 alenail/galaxy-neurolincs
