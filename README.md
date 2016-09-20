[![Build Status](https://api.travis-ci.org/fraenkel-lab/galaxy-neurolincs.svg](https://travis-ci.org/fraenkel-lab/galaxy-neurolincs)
[![Docker Repository on Quay](https://quay.io/repository/fraenkel_lab/galaxy-neurolincs/status "Docker Repository on Quay")](https://quay.io/repository/fraenkel_lab/galaxy-neurolincs)


# The NeuroLINCS Galaxy

The [NeuroLINCS Consortium](http://neurolincs.org/) uses Galaxy to perform reproducible computational analysis.

This image inherits from [bgruening/docker-galaxy-stable](https://github.com/bgruening/docker-galaxy-stable) and adds:
- Configuration in the form of environment variables.
- A suite of tools we use, which you can find in [`tools.yml`](https://github.com/fraenkel-lab/galaxy-neurolincs/blob/master/tools.yml).
- A custom homepage.
- An additional set of ports we expose.


<!--
## Pipelines

Our goal is to make our computational pipelines open and reproducible, which means we'd like to publish the source code (for openness) but go further and ensure those pipelines' reproducibility in the long, using a containerization strategy. For containerization we use docker, which is the default, open source standard.

A container is a program executable from any operating system, including any past or future operating systems. It bundles all the dependencies of a pipeline with the actual pipeline, meaning that future changes in operating systems or libraries relied on by the pipeline do not affect the pipeline's ability to execute to completion. A containerized pipeline is impervious to time, and exactly reproducible in any environment. See these  blog  posts for more.

Using galaxy, we publish our computational tools, both on github and the galaxy tool shed, and soon we will also be publishing them to the dockerhub. Other computational platforms use dockerization for their entire workflows by default (e.g. Arvados by Curoverse). We also have an easy to way to publish our pipelines to myExperiment and we're hoping to support Dockstore soon.
 -->
