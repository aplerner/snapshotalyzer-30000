#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:42:31 2020

@author: aaronlerner
"""

import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='shotty')
    ec2 = session.resource('ec2')
    for i in ec2.instances.all():
        print(i)
    
