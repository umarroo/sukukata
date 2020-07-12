# Function ini memerlukan file "kata.txt" yang dapat digenerate melalui "getKBBIdb.py" dengan command seperti di README
def get_clean_sukukata() :
    f = open( "./data/kata.txt", "r"); lines = f.readlines(); f.close()
    for line in lines:
        if (not "<" in line) and (not "?" in line) and (not " " in line) :
            print( line.strip().lower())

get_clean_sukukata()
