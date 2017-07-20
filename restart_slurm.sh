
#!/bin/bash

sudo /usr/sbin/munged -f --key-file=/etc/munge/munge.key --num-threads=10

sudo /etc/init.d/slurmd stop
sudo /etc/init.d/slurmctld stop
sudo /etc/init.d/slurmd start
sudo /etc/init.d/slurmctld start

