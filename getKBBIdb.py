

# data diambil daris https://github.com/efenfauzi/django_kbbi/raw/master/db/kbbi.db

import sqlite3
from bs4 import BeautifulSoup
from copy import copy, deepcopy

def pd( data ) :
  for d in data :
    print( d, end='' )

conn = sqlite3.connect('./data/kbbi.db')
c = conn.cursor()

def select_kbbi(  connection  ) :
  c.execute("SELECT katakunci, artikata FROM datakata " ) # where katakunci like '" + word + "%' ")
  rows = c.fetchall()
  for row in rows:
    r = row[0].replace( "xb7", "-" )
    r2 = row[1].replace( "xb7", "-" )
    r2 = r2.replace("&gt", ">").replace("&lt","<").replace("<;","<").replace(">;",">")
    soup = BeautifulSoup( r2, 'html.parser')
    bs = list( soup.find_all( 'b' ))
    for b in bs :
      sb = str( b )
      if "·" in sb :
        sb = sb.replace( "·", "-").replace( "<b>","").replace( "</b>","")
        print(  sb  )

select_kbbi(  c )
