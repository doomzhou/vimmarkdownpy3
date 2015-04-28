#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : 1.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1391689291
# Last Modified :
# Release By : Doom.zhou


import sys, os, time
sys.path.append('./md_instant/')
import md_instant
print("import md_instant")
md_instant.main()
print("end md_instant.main()")
md_instant.startbrowser()
print("end md_instant.startbrowser()")
print("input interrupt")

while True:
    try:
        intert = input("anykey continue:")
        if intert == 'quit':
            md_instant.stopserver()
            sys.exit(0)
        print('start md_instant.sendall("input")')
        md_instant.sendall(intert)
    except KeyboardInterrupt:
        md_instant.stopserver()
