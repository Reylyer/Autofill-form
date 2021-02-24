import requests
import datetime
import sys
import os
import time
import random




masih = True
clear = lambda: os.system('cls')

class Siswa():
    def __init__(self, NIS, nama, kelas):
        self.NIS = NIS
        self.nama = nama
        self.kelas = kelas
        self.kehadiran = "HADIR"



urlTest = "https://docs.google.com/forms/d/e/1FAIpQLSd3JM9wXietuo5L9X37qIFjotqKaH27bXt5gg6hKCzO2EPC5g/formResponse"
urlAbsenPagi = "https://docs.google.com/forms/d/e/1FAIpQLSeT5IB0STSo4sdkGxoTQndwAfvRUiHwY9LzesQxxVRsCaWLTQ/formResponse"


urlAbsenBing = "https://docs.google.com/forms/d/e/1FAIpQLSdZtn4xHrbMFSgjnCqV17PtoiJWInukZD2fM2HeQXr2SLxKWg/formResponse"

urlAbsenPKWU = "https://docs.google.com/forms/d/e/1FAIpQLSfwQANMWD8rHbZ3LuA2lxQUZsjSA8mF0snsJQdoVG3XSnNe8A/formResponse"
urlAbsenSejarah = "https://docs.google.com/forms/d/e/1FAIpQLSeBIiutnf4vuYJFC7OUU74JHC9FCtIzvmzgL853TD9PG_V47g/formResponse"
urlAbsenMatjib = "https://docs.google.com/forms/d/e/1FAIpQLSd8la2MJ3Vn-q8Uppz1vEsUuF2jxn6OIG5HUlnqKk6atu0NlA/formResponse"


urlAbsenBio = "https://docs.google.com/forms/d/e/1FAIpQLSdEKVydKLGcb6LAwIJQcZnKSnS3Ccc20gvZ1bdrB_8XLCQZqA/formResponse"
urlAbsenPKN = "https://docs.google.com/forms/d/e/1FAIpQLSfsh_exyYg3g8654o7Tkfpz2VWSgMLy9KJp2SFIc5Hslpvp3g/formResponse"
urlAbsenBjep = "https://docs.google.com/forms/d/e/1FAIpQLSdTXyiIIkh3vJjoJlz4H6de5h4mPRlg7QKQ-z4fHf1mo5iiBQ/formResponse"

urlAbsenFisika = "https://docs.google.com/forms/d/e/1FAIpQLSfRYVxB5j2mE1b_Tf0BVNl3fX8o_PMse5kO_XsPeMOU9Skp7A/formResponse"
urlAbsenMatmin = "https://docs.google.com/forms/d/e/1FAIpQLScE9OJhFZNGyHt6ESiIidH9ap_FzBPtNkAMJpeLn3TZYneknw/formResponse"
urlAbsenBsun = "https://docs.google.com/forms/d/e/1FAIpQLSeT5IB0STSo4sdkGxoTQndwAfvRUiHwY9LzesQxxVRsCaWLTQ/formResponse"

urlAbsenBindo = "https://docs.google.com/forms/d/e/1FAIpQLScoI2XiNvEjC2FiCukhVEQgRpRftqkd0l6lrhkSJQ0QaBGv7g/formResponse"
urlAbsenPJOK = "https://docs.google.com/forms/d/e/1FAIpQLSc8YEyLHwqy66NINGJ4QbG7alRfhsQAplvDbeP_sGbXuMc4DA/formResponse"
urlAbsenPAI = "https://docs.google.com/forms/d/e/1FAIpQLSdK4RPrwDD5nem7nhx3kSduqHkB6CY5ELM3uEDiPQEUqs5D7g/formResponse"

urlAbsenSBK = "https://docs.google.com/forms/d/e/1FAIpQLSdTJ6o-0nl88atYVkRkVjPiJdZL1awsfAVudQQtP7IXXZDQDg/formResponse"


urlAbsenPMBing ="https://docs.google.com/forms/d/e/1FAIpQLScaJfYXDlV9ObjIfkcCseozJ9M6ULSBQfGHM2SsEHrNDkl1BQ/viewform"



def get_entry_absen(siswa):
    # Target POST -> form sekolah
    entryAbsen = {
        "entry.1404348575" : siswa.NIS,       #NIS
        "entry.1214830987" : siswa.nama,      #NAMA LENGKAP
        "entry.1067880870" : siswa.kelas,     #KELAS
        "entry.893774694"  : siswa.kehadiran  #KEHADIRAN
    }
    return entryAbsen

def get_entry_test(siswa):
    entryAbsen = {
        "entry.204222402" : siswa.NIS,
        "entry.1906862676" : siswa.nama, 
        "entry.290170554" : siswa.kelas, 
        "entry.165880829" : siswa.kehadiran  
    }
    return entryAbsen

def postEntry(entryInt, url, urlTest ="https://docs.google.com/forms/d/e/1FAIpQLSd3JM9wXietuo5L9X37qIFjotqKaH27bXt5gg6hKCzO2EPC5g/formResponse"):
    random.shuffle(entryInt)
    for x in entryInt:
        try:
            entrytest = get_entry_test(x)
            entry = get_entry_absen(x)
            
            requests.post(urlTest, entrytest)
            requests.post(url, entry)
            print("form submitted : " + x.nama)
        except:
            print("error")


muridIpa1Int = [
    #Siswa(181910198, "ALFIAN SALIM", "XII IPA 1"),
    #Siswa(181910123, "ALIFA NADYA SALSABILA", "XII IPA 1"),
    #Siswa(181910206, "ANNISA SAYYIDINA RAHMA", "XII IPA 1"),
    #Siswa(181910207, "ANWAR SAID PINTRANDHITA", "XII IPA 1"),
    #Siswa(181910086, "ARALI TYASNING PRASTITA", "XII IPA 1"),
    #Siswa(181910208, "ARDILAH", "XII IPA 1"),
    #Siswa(181910126, "ARYANTI KHARIDAH MUMTAZ", "XII IPA 1"),
    #Siswa(181910045, "ASTRI YUNITA NUR'AENI", "XII IPA 1"),
    #Siswa(181910047, "BISMA ARYA URIP PRAMUDITHA", "XII IPA 1"),
    #Siswa(181910163, "CHRISTINA RAISSA DONGORAN", "XII IPA 1"),
    #Siswa(181910048, "CINTA RABBAINA AL-FITRI", "XII IPA 1"),
    #Siswa(181910214, "DEA PUSPITASARI", "XII IPA 1"),
    #Siswa(181910050, "DEWI MURTI", "XII IPA 1"),
    #Siswa(181910216, "ERIDIA SURYADINATA", "XII IPA 1"),
    #Siswa(181910053, "EZRA TRIDARA", "XII IPA 1"),
    #Siswa(181910054, "FADHIEL HAYKAL NUN IFTIKHAR", "XII IPA 1"),
    #Siswa(181910167, "FAUZAN TARRICO INDRAPURI RUCHIYAT", "XII IPA 1"),
    #Siswa(181910090, "FITRIA MOZA PARAMITA", "XII IPA 1"),
    Siswa(181910168, "GIVANDRA HAIKAL ADJIE", "XII IPA 1"),
    #Siswa(181910058, "HANI MUJAHIDAH", "XII IPA 1"),
    #Siswa(181910059, "HANIFAH MUTHMAINNAH", "XII IPA 1"),
    #Siswa(181910170, "HANNA APRILIANA ARIFIN", "XII IPA 1"),
    #Siswa(181910410, "HANNI APRILIANI ARIFIN", "XII IPA 1"),
    #Siswa(181910017, "HASNA ROFIFAH", "XII IPA 1"),
    #Siswa(181910220, "HAUZAN ARIQ BAKRI", "XII IPA 1"),
    #Siswa(181910172, "HIDAYAT", "XII IPA 1"),
    #Siswa(181910135, "I GUSTI AGUNG AYU BINTANG PUTRI MAHARANI", "XII IPA 1"),
    #Siswa(181910061, "IDELIA ELVIKA UTOMO", "XII IPA 1"),
    #Siswa(181910173, "KEISYARIQ RAMATHA ATSIL", "XII IPA 1"),
    #Siswa(181910178, "MUHAMMAD DAULAH IZZATHURRAHMAN", "XII IPA 1"),
    #Siswa(181910176, "MUHAMMAD RIFQI CIKAL RESWARA", "XII IPA 1"),
    #Siswa(181910224, "NABILA SALMA NAJWAGITA WIDYANDINI SUNARDI", "XII IPA 1"),
    #Siswa(181910100, "NAUFAL BAGHIZ MURFID", "XII IPA 1"),
    #Siswa(181910185, "RAFIF JAHFAL AL FARIZ", "XII IPA 1"),
    #Siswa(181910147, "RISKA AZIJAH", "XII IPA 1"),
    #Siswa(181910108, "ROSSI AMALIA", "XII IPA 1"),
    #Siswa(181910077, "SARAH ASHIRA TSAQIBAH", "XII IPA 1"),
    #Siswa(181910115, "WIDYA HANA SUNARYA", "XII IPA 1"),
    #Siswa(181910233, "YAHYA AYAS FIRDAUSI", "XII IPA 1"),
    #Siswa(181910079, "YORIN WAHYUNI ANITASYAH", "XII IPA 1"),
]

while (True):
    today = datetime.datetime.today().weekday()
    now = datetime.datetime.now().time().strftime("%H:%M")
    date  = datetime.date.today()
    
    if (today == 0): #senin
        if(now == "07:12"):
            postEntry(muridIpa1Int, urlAbsenBing)
        elif(now == "08:11"):
            postEntry(muridIpa1Int, urlAbsenPKWU)
        elif(now == "09:04"):
            postEntry(muridIpa1Int, urlAbsenSejarah)
        elif(now == "10:05"):
            postEntry(muridIpa1Int, urlAbsenMatjib)
        
    elif(today == 1): #selasa
        if(now == "07:08"):
            postEntry(muridIpa1Int, urlAbsenBio)
        elif(now == "09:07"):
            postEntry(muridIpa1Int, urlAbsenPKN)
        elif(now == "10:12"):
            postEntry(muridIpa1Int, urlAbsenBjep)
            
    elif(today == 2): #rabu
        if(now == "07:06"):
            postEntry(muridIpa1Int, urlAbsenFisika)
        elif(now == "09:13"):
            postEntry(muridIpa1Int, urlAbsenMatmin)
        elif(now == "11:09"):
            postEntry(muridIpa1Int, urlAbsenBsun)
            
    elif(today == 3): #kamis
        if(now == "07:15"):
            postEntry(muridIpa1Int, urlAbsenBindo)
        elif(now == "09:12"):
            postEntry(muridIpa1Int, urlAbsenPJOK)
        elif(now == "11:08"):
            postEntry(muridIpa1Int, urlAbsenPAI)
            
    elif(today == 4): #jumat
        if(now == "07:11"):
            postEntry(muridIpa1Int, urlTest)
            #kimia ga ada link
        elif(now == "09:04"):
            postEntry(muridIpa1Int, urlAbsenSBK)
        elif(now == "10:07"):
            postEntry(muridIpa1Int, urlTest)
            #BK ga da link absen
            
    if (today in [0,1,2,3,4]):
        if(now == "06:47"):
            postEntry(muridIpa1Int, urlAbsenPagi)
    
    for i, hari in enumerate(["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu",]):
        if(today == i):
            print(f"{date} {hari}, {now}")
            continue
    time.sleep(60)
    
