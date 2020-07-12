date
echo "Processing database"
python getKBBIdb.py > ./data/kata.txt
date
echo "Cleaning sukukata from database"
python cleaning.py > ./data/sukukata.txt
date
echo "Last step"
python sukukata.py > unik.txt
date