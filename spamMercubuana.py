import requests
import datetime
import sys
import os
import time


def get_entry():
    # Target POST -> form sekolah
    entryAbsen = {
        "entry.647763043" : "James",
        "entry.902214078" : "Lebih baik tidak disebut",
        "entry.386699121" : "Jl. Manggis",
        "entry.649375552"  : "-",
        "entry.1233194558"  : "-",
        "entry.1992761138"  : "-",
        "entry.574298786"  : "-",
        "entry.1162249157"  : "-",
        "entry.1588717721"  : "Pegawai Swasta",
        "entry.252889775"  : "suzuicross@gmail.com",
        "entry.1135944833"  : "089602748666",
        "entry.273962345"  : "SMAN 2 Bekasi",
        "entry.1904807535"  : "IPS",
        "entry.428885596"  : "X",
        "entry.557074302"  : "malas mengkopi",
        "entry.1819272071"  : "Bisa jadi",
        "entry.1367598407"  : "Luar negeri",
        "entry.1038095989"  : "Toilet mewah",
        "entry.1717076026"  : "sejeti",
        "entry.665293534"  : "Dulu, ditelpon",
        "entry.37248170"  : "ngga maaf",
        "entry.821380472"  : "dapet survei",
        "entry.1045252650"  : "Karena tidak tertarik",
        "entry.2066068529"  : "Dimana hayo",
        "entry.2064765051"  : "karena...(isi sendiri)",
        "entry.816735324"  : "S1 sikologi",
        "entry.1888783583"  : "nope.",
        "entry.392882458"  : "nope",
        "entry."  : "-",
        
    }
    return entryAbsen

entry = get_entry()

requests.post("https://docs.google.com/forms/d/e/1FAIpQLSdGdsCYcaOIz1xAGqyM_ELr97IeHGwNfoc3FTKnDPWxx0Mblw/formResponse", entry)