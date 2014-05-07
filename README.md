# Template render

## Overview

Python program that can be used to render templates with variable values. Program will take template, extract variables and ask user to enter values for these variables. After all variables have values, program generate text file with those values.

## Requirements

Template must be in text format and all variables should be in format {{ variable }}.

## Example

Store the following configuration in text file with the name template:
!
interface FastEthernet 0/0
 ip address {{ ip_address }} {{ network_mask }}
 no shutdown
! 


Run program with -t option:

`python template_render.py -t template`


Program will ask you to enter values for ip_address and network_mask variable, for example 192.168.1.1 and 255.255.255.0.

The program will generate the following text output:

!
interface FastEthernet 0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!

