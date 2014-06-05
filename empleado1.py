#!usr/bin/env python
# -*- coding: utf-8 -*-
#python version 2.7.6
#by Junior Montilla

from urllib import urlopen
from sys import argv
import json
import sqlite3

if len(argv)> 1:    
    database = sqlite3.connect('my_data2.db')
    cursor = database.cursor()
    output = urlopen('http://data.developers.do/api/v1/provincias/{0}'.format(argv[1]+'.json'))
    reading =  output.read()
    jsonobject = json.loads(reading)
    datatostorage = (jsonobject['nombre'],)
    cursor.execute('CREATE TABLE IF NOT EXISTS Province (name text)')
    cursor.execute('INSERT INTO Province VALUES(?)', datatostorage)
    database.commit()
    database.close()
    print 'the province {0} has been properly stored'.format(datatostorage[0])
