#!/usr/bin/env bash

. ./grp-22-openrc.sh; ansible-playbook -i ./inventory/hosts remove_instances.yaml -K