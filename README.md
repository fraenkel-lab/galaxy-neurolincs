[![Build Status](https://api.travis-ci.org/fraenkel-lab/galaxy-neurolincs.svg)](https://travis-ci.org/fraenkel-lab/galaxy-neurolincs)
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


## Notes for Future Administrators of this Galaxy

The following is documentation about how this instance was set up, for future maintainers.

### The architecture is as follows:

- There exists an Microsoft Azure VM (a computer) which we rent.
- On that computer is running a container, which is like a virtual machine, managed by software called docker. The container contains is an implementation of galaxy. This container is portable to other computers and VMs that are not Azure.
- Inside galaxy we have a set of workflows and tools which provide us the capacity to perform our analyses reproducibly.

### Azure:

Microsoft Azure is a cloud-computing host, providing a variety of services, such as access to "virtual machines" which are computational "real-estate" in Microsoft's datacenters.

We've set up a "D2_V2" virtual machine. It has an IP address of `13.68.103.194`, which you can use with `ssh` or `ftp`. The program `ssh` allows you to connect to the virtual machine via the command line and operate the machine. Azure's web portal will also allow you to configure the machine. The VM runs `Ubuntu 16.04 LTS` as the operating system.

### Docker:

After settig up the VM and using `ssh` to connect to it, I installed [docker](https://docs.docker.com) which describes itself as "An open platform for distributed applications for developers and sysadmins". The principal advantage of using docker is that [Björn Grüning](https://github.com/bgruening) built a ["dockerized" version of galaxy](https://github.com/bgruening/docker-galaxy-stable), which can run on any machine that can run docker. The Galaxy ecosystem of tools has a component named "cloudman" which makes it quite easy to set up galaxy on Amazon Web Services, but it seems difficult to set up galaxy on other platforms, but by using docker as an intermediary, setting up Galaxy on any system becomes as trivially simple.

I found documentation for intalling Docker [here](https://docs.docker.com/engine/installation/linux/ubuntulinux/) and instructions to run galaxy using docker [here](https://github.com/bgruening/docker-galaxy-stable/blob/master/README.md).

> Quick note: once you follow these steps, it's also important to go to the Azure web portal and make sure that the inbound and outbound rules on the network security group that the VM is in are correctly established so that the VM is willing to accept web traffic. The default setting of an Azure VM is to be closed to web traffic, so you'll need to add rules on the network security group that permitactivity on ports 80, as well as any other ports you'd like to access on the VM.
> Quick note: You may run into [this issue](https://github.com/docker/docker/issues/17645), but the first comment solvedmy problem.

### Installing tools:

Installing tools is done in the conventional way, but once a tool has been successfully installed, make sure to

```
$ docker exec <container-id> supervisorctl restart galaxy:
```
