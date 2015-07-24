import requests
import json

def adzan(args):
    # format: lat,lon,timezone
    locs = {
        "bandung":[-6.3253,106.4914,7],
        "bogor":[-6.58916,106.7929,7],
        "jakarta":[-6.2087634,106.8455989,7],
        "aceh":[4.695135,96.7493993,7],
        "samarinda":[-0.4948232,117.1436154,8],
        "balikpapan":[-1.2697669,116.83617149,8],
        "makassar":[-5.1308551,119.4165284,8]
    }
    try: 
        tz = 0
        lokasi = None
        if args[1] in locs.keys():
            lokasi = locs[args[1]]
            tz = lokasi[2]
        else:
            return "sementara lokasi tidak tersedia"
        
        url = "http://www.islamicfinder.org/prayer_service.php?latitude={0}&longitude={1}&timezone={2}&simpleFormat=json".format(lokasi[0],lokasi[1],tz)
        r = requests.get(url)
        if r.status_code == 200:
            data = json.loads(r.text[3:])
            res = """
            {0} / {1}
            Fajr:{2}
            Dhuhr:{3}
            Asr:{4}
            Maghrib:{5}
            Isha:{6}
            Source: {7}
            """.format(data['hijri'],data['date'],data['fajr'],data['dhuhr'],data['asr'],data['maghrib'],data['isha'],data['website'])
            return res
        else:
            return "something wrong"
    except:
        return "something wrong, coba masukan command dengan benar /adzan lokasi(bandung, bogor, jakarta, aceh, samarinda, balikpapan, makassar)"
