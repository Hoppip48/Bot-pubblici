from datetime import date
from telethon import TelegramClient
import datetime
from random import randint
import contatori
import asyncio
import aiocron

API_ID = contatori.API_ID
API_HASH = contatori.API_HASH
client = TelegramClient("contatore", API_ID, API_HASH)

client.parse_mode = "md"
messdelgiorno = ""
idgruppo=contatori.IDGRUPPO
dialoghi = contatori.DIALOGHI

natale = date(2021, 12, 25)
grimasti = (contatori.FINESCUOLA - date.today()).days
gpassati = (date.today() - contatori.INIZIO).days
effgr = grimasti
vacanze = [date(2021, 11, 1), date(2021, 12, 8), date(2022, 4, 17), date(2022, 4, 18), date(2022, 4, 25),
           date(2022, 5, 2)]
for i in range((date(2022, 1, 7) - date(2021, 12, 22)).days):
    vacanze += [date(2021, 12, 22) + datetime.timedelta(days=i)]
for i in range(grimasti):
    giorniliberali = date.today() + datetime.timedelta(days=i)
    if giorniliberali.weekday == 6 or giorniliberali in vacanze:
        effgr -= 1


@aiocron.crontab('0 7 * * *')
async def checkday():
    global grimasti
    global gpassati
    global effgr
    global messdelgiorno
    global idkkk
    global idcontatore
    oggi = date.today()
    grimasti -= 1
    gpassati += 1
    if oggi == contatori.COMPLEANNO:
        await client.send_message(idgruppo, "Auguri!")
    elif oggi == natale:
        await client.send_message(idgruppo, "Buon natale!")
    elif oggi == contatori.FINESCUOLA:
        await client.send_message(idgruppo, "è finita finalmente")
        client.close()
    elif oggi.weekday() == 6:
        await client.send_message(idgruppo, "buona domenica")
    elif oggi not in vacanze:
        messdelgiorno = dialoghi[randint(0, len(dialoghi) - 1)]
        messdelgiorno += "\n  \nGiorni di scuola rimasti: " + str(effgr) + "\nGiorni passati: " + str(
            int(gpassati)) + "\nSettimane rimaste: " + str(int(grimasti / 7)) + "\nGiorni totali rimasti: " + str(
            grimasti)
        effgr -= 1
        await client.send_message(idgruppo, messdelgiorno)


def main():
    client.start()
    print("connesso")
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
