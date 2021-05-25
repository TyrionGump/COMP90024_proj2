#!/bin/bash

. ./grp-22-openrc.sh; ansible-playbook -i ./inventory/hosts copy_frontend.yaml -K