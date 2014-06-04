#!usr/bin/env python
# -*- coding: utf-8 -*-
#python version 2.7.6
#by Junior Montilla

from urllib import urlopen
from bs4 import BeautifulSoup
import sqlite3

database = sqlite3.connect('my_data1.db')
cursor = database.cursor()
output = urlopen('http://www.diariolibre.com/')
reading = output.read()
soup = BeautifulSoup(reading)
for elements in soup.find_all(id='boxmed'):
    data = elements.find_all('td',class_='value')

datatostorage = (
                    data[0].get_text(),
                    data[1].get_text(),
                    data[2].get_text(),
                    data[3].get_text(),
                )

cursor.execute('''
              CREATE TABLE IF NOT EXISTS Cupexchange 
              (dollar_demand text, dollar_offer text, euro_demand text, euro_offer text)
              ''')

cursor.execute('INSERT INTO Cupexchange VALUES(?,?,?,?)', datatostorage)
database.commit()
print 'The data have been stored properly'
