#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 08:22:22 2022

@author: ctall
"""

import mysql.connector

cnx = mysql.connector.connect(user='ekjc.ctall', password='CzM809$',
                              host='127.0.0.1',
                              database='employees')
# testing github new

cnx.close()