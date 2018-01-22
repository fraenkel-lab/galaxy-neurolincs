[![Docker Repository on Quay](https://quay.io/repository/fraenkel_lab/galaxy-neurolincs/status "Docker Repository on Quay")](https://quay.io/repository/fraenkel_lab/galaxy-neurolincs)

# The NeuroLINCS Galaxy

The [NeuroLINCS Consortium](http://neurolincs.org/) and [AnswerALS](http://answerals.org) use Galaxy to perform reproducible computational analysis.

This docker image inherits from [bgruening/docker-galaxy-stable](https://github.com/bgruening/docker-galaxy-stable) and adds:
- Configuration in the form of environment variables.
- A suite of tools we use, which you can find in [`tools.yml`](https://github.com/fraenkel-lab/galaxy-neurolincs/blob/master/tools.yml).
- Our standard workflows for each 'omic.
- A custom homepage.
- An additional set of ports we expose.

You can find examples of this image running at [answer.csbi.mit.edu/](http://answer.csbi.mit.edu/) and [galaxy.neurolincs.org](http://galaxy.neurolincs.org).


### Notes:

- Installing tools is done in the conventional way, but once a tool has been successfully installed, make sure to

	```
	$ docker exec <container-id> supervisorctl restart galaxy:
	```
