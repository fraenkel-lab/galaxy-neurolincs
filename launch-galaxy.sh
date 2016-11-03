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

# for testing with globus integration: 
# docker run -d -p 80:80  -p 21:21 -p 8800:8800 -p 9002:9002 -p 2811:2811 -p 2223:2223 -p 7512:7512 -p 50000-51000:50000-51000 alenail/galaxy-neurolincs

