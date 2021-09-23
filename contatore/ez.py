from telethon import TelegramClient
from datetime import date, time
import datetime
import time
from random import randint

idez = "qui metti tuo id"
hashid = "qui metti tuo hashid"
client = TelegramClient("Allah", idez, hashid)
finescuola=date(2022,6,21)

client.parse_mode = "md"
messdelgiorno=""
idcontatore="qui metti id del canale/gruppo/user a cui vuoi che vada il messaggio"
dialoghi = ["Qui metti", "i buongiorni","verranno scelti", "randomicamente"]

vacanze=[date(2021,11,1),date(2021,12,8),date(2022,4,17),date(2022,4,18),date(2022,4,25),date(2022,5,2)]
for i in range((date(2022,1,7)-date(2021,12,22)).days):
    vacanze+=[date(2021,12,22)+datetime.timedelta(days=i)]
oggi = date.today()
natale=date(2021,12,25)
grimasti=(finescuola-oggi).days
effgr=grimasti
for i in range(grimasti):
    giorniliberali = (oggi + datetime.timedelta(days=i)).weekday()
    if giorniliberali == 6 or giorniliberali in vacanze:
        effgr-=1

print((finescuola-oggi).days)

async def cummingtonite():
    global oggi
    global grimasti
    global effgr
    global messdelgiorno
    a=datetime.datetime("qui metti la data e ora dove vuoi che cominci a contare, es: 2021,8,19,7,0,0 (y,m,d,h,m,s)")
    b=datetime.datetime.today()
    print((a-b).seconds)
    time.sleep((a-b).seconds)
    while grimasti>0:
        oggi = date.today()
        grimasti-=1
        print("Giorno cominciato")
        if oggi not in vacanze or oggi.weekday!=6 or oggi.month!=6:
            messdelgiorno=dialoghi[randint(0,len(dialoghi)-1)]
            messdelgiorno+="\n  \nGiorni rimasti: "+str(effgr)+"\nMesi: "+str(int(grimasti/30))+"\nSettimane: "+str(int(grimasti/7))+"\nSecondi: "+str(grimasti*24*60*60)+"\nGiorni totali: "+str(grimasti)
            effgr-=1
            await client.send_message(idcontatore, messdelgiorno)
        elif (oggi-natale).days>0:
            await client.send_message(idcontatore, "Oggi è domenica, o come mi piace chiamarla, "+str((natale-oggi).days)+" giorni a natale")
        elif oggi == natale:
            await client.send_message(idcontatore, "Natale")
        elif oggi==finescuola:
            await client.send_message(idcontaatore, "Buon AmumuDay cowboys")
        time.sleep(24*60*60)


def main():
    print("mammt")
    client.start()
    client.loop.run_until_complete(cummingtonite())


if __name__=="__main__":
    main()
