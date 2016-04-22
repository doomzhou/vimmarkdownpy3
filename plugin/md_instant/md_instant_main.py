#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : md_instant.py
# Purpose :
# Creation Date : 1391562732
# Last Modified : Wed 05 Feb 2014 09:33:21 AM CST
# Release By : Doom.zhou

#import sys
#import os
#import vim
import time
import md_instant


def main():
    '''
    no
    '''
    #sys.path.append(vim.eval('s:scriptfolder'))
    #sys.stdout = open(os.path.devnull, 'w')
    #sys.stderr = open(os.path.devnull, 'w')
    #vim.command(':autocmd!')
    #vim.command('autocmd CursorMovedI * call UpdateMarkdown()')
    #vim.command('autocmd VimLeave * call CloseMarkdown()')
    md_instant.main()
    md_instant.startbrowser()
    md_instant.sendall("hello doom")

def updatemarkdown():
    '''
    no
    '''
    print('none')


def closemarkdown():
    '''
    no
    '''
if __name__ == "__main__":
    main()
    md_instant.sendall("hello doom")
