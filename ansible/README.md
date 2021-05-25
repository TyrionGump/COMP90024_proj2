# System Deployment

All the system deployments are accomplished using Ansible. The files and command line executed below are all in path relative to this directory. Variables are configured in *host_vars/instance_config.yaml*, including volumes configuration, security groups, instances configuration, and other common variables. The deployment playbooks are organized as follows.

### 1 Create instances

First, we configure the local host and create instances in this step. The following roles are for the local host.

*openstack-common*: install and update python-pip; install openstacksdk; add group key to default ssh directory on host (install dependencies on the host).

*openstack-images*: show all available Openstack images.

*create_instances* (with following tasks included): 

*openstack-volume*: create volumes on MRC.

*openstack-security-group*: create all the security groups we need and the corresponding rules.

*openstack-instance*: create instances on MRC and create a file with the IP addresses of the instances created .

##### 1.1  How to run

*. ./create_instances.sh*

Or run the command written in the *create_instances.sh* file directly.

### 2  Config instances

Then we need to configure the created remote instances. 

*set-proxy*: edit proxy settings to allow the instances to have access to external network.

*setup-docker* (with following tasks included): 

*common*: install dependencies on the remote host

*mount-volumes*: format the volumes with specified file system and mount them to corresponding instances

*docker*: create required environment for on remote instances, including install dependencies and add Docker apt repository, etc. Then install and configure Docker.

##### 2.1 How to run

*. ./config_instances.sh*

Or run the command written in the *config_instances.sh* file directly.

### 3  Set up CouchDB cluster

For setting up a CouchDB cluster, first we run the *setup-couchdb* role on all remote instances to start a Docker container with a CouchDB. Then on the masternode specified before, we run the *setup-couchdb-cluster* role to set up a cluster and all other nodes to the cluster.

##### 3.1How to run

*. ./setup_couchdb.sh*

Or run the command written in the *setup_couchdb.sh* file directly.

### 4 Deploy twitter harvester

For deployment of twitter harvester, we first install dependencies required such as tweepy and couchdb. Then we copy the harvester scripts to remote instances and execute.

##### 4.1 How to run

*. ./* *deploy_harvester.sh*

Or run the command written in the *deploy_harvester.sh* file directly.

### 5 Frontend deployment

To deploy frontend, we first copy the files we need to remote instances and then install dependencies required such as flask and gunicorn. Then enable the web server.

##### 5.1 How to run

*. ./* *deploy_frontend.sh*

Or run the command written in the *deploy_frontend.sh* file directly.