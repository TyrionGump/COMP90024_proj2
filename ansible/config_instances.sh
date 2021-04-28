#!/bin/bash

. ./grp-22-openrc.sh; ansible-playbook -i ./inventory/hosts config_instances.yaml -K