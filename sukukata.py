


def get_unique_sukukata() :
    f = open( "./data/sukukata.txt", "r"); lines = f.readlines(); f.close()
    sukuk = []
    for line in lines:
        sk = line.strip().split("-")
        for s in sk :
            if not s in sukuk :
                sukuk.append( s )
                #print( s )
    sukuk = sorted( sukuk )
    for s in sukuk :
      print( s )

# get_unique_sukukata()

def get_unique_sukukata_example() :
    f = open( "./data/sukukata.txt", "r"); lines = f.readlines(); f.close()
    uf = open( "./data/uniksukuk1.txt", "r"); uulines = uf.readlines(); uf.close()

    ulines = {}  # ambil suku kata tanpa baris kosong
    for u in uulines :
        u = u.strip()
        if u != "" :
            #ulines.append( {u:[]} )
            ulines[ u ] = []

    for l in lines :
        line = l.strip().split("-")
        for li in line :
            if li in ulines : # apakah suku kata ini ada di tabel ?
              if len( ulines[li] ) < 5 : # contoh katanya tidak perlu terlalu banyak
                 ulines[ li ].append( l.strip() )
            else :
              print( "***", li.strip() , "***")
    for ul in ulines :
        print( ul, "=", ulines[ul] )

#! Versi lebih baik dari get_unique_sukukata()
def get_unique_sukukata_example2() :
    f = open( "./data/sukukata.txt", "r"); lines = f.readlines(); f.close()
    uf = open( "./data/manual_suku_kata_unik.txt", "r"); uulines = uf.readlines(); uf.close()
    from pprint import pprint

    ulines = {}  # ambil suku kata tanpa baris kosong
    for u in uulines :  # inisiasi seluruh suku kata 2000
        u = u.strip()
        if u != "" :
            #ulines.append( {u:[]} )
            ulines[ u ] = {'number':0, 'syl': []}
    
    for l in lines :
        line = l.strip().split("-")
        for li in line :
            if li in ulines : # apakah suku kata ini ada di tabel ?
              if len( ulines[li]['syl'] ) < 50 : # contoh katanya tidak perlu terlalu banyak
                 ulines[ li ]['syl'].append( l.strip() )
                 ulines[ li ]['number'] += 1
              else :
                 ulines[ li ]['number'] += 1

            else :
            #   print( "***", li.strip() , "*** suku kata kbbi yg kemungkinan perlu diperbaiki")
              pass 
    for ul in ulines :
        out = "{:<6} {:>5} {}".format(  ul, ulines[ul]['number'],  ulines[ul]['syl'] )
        print(out)

get_unique_sukukata_example2()