#!/bin/sh
# This script removes duplicate lines from an sql dump
awk '/INSERT/{if(!visited[$0]++)print $0} !/INSERT/ {print $0}' $1
