#!/bin/bash

. ./grp-22-openrc.sh; ansible-playbook -i ./inventory/hosts deploy_harvester.yaml -K