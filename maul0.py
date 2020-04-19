# -*- coding: utf-8 -*-

from linepy import *
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
#from gtts import gTTS
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests as uReq
from datetime import datetime
from googletrans import Translator
from zalgo_text import zalgo
import ast, codecs, json, os, pytz, re, LineService, random, sys, time, urllib.parse, subprocess, threading, pyqrcode, pafy, humanize, os.path, traceback
from threading import Thread,Event
import requests,uvloop
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
loop = uvloop.new_event_loop()

client = LINE("zahrasyafira52@gmail.com","ml1234")
client.log("Auth Token : " + str(client.authToken))

#sw = LINE("")
#sw.log("Auth Token : " + str(sw.authToken))

clientPoll = OEPoll(client)
call = client
clientMid = client.getProfile().mid
Bots = [clientMid]

owner = ["u8ca6c521561560230979746548425503"]
admin = ["u8ca6c521561560230979746548425503"]

protectantijs = []


mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

clientSettings = client.getSettings()
clientProfile = client.getProfile()

clientStart = time.time()

languageOpen = codecs.open("language.json","r","utf-8")
mentioOpen = codecs.open("tagme.json","r","utf-8")
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("setting.json","r","utf-8")
ownerOpen = codecs.open("owner.json","r","utf-8")
adminOpen = codecs.open("admin.json","r","utf-8")
stickerOpen = codecs.open("sticker.json","r","utf-8")
stickertOpen = codecs.open("stikerpt.json","r","utf-8")
textaddOpen = codecs.open("text.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
waitOpen = codecs.open("wait.json","r","utf-8")
answeOpen = codecs.open("autoanswer.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
unsendOpen = codecs.open("unsend.json","r","utf-8")

audios = json.load(audiosOpen)
language = json.load(languageOpen)
tagme = json.load(mentioOpen)
read = json.load(readOpen)
settings = json.load(settingsOpen)
owner = json.load(ownerOpen)
admin = json.load(adminOpen)
stickers = json.load(stickerOpen)
stickerstemplate = json.load(stickertOpen)
textsadd = json.load(textaddOpen)
images = json.load(imagesOpen)
wait = json.load(waitOpen)
autoanswer = json.load(answeOpen)
unsend = json.load(unsendOpen)


welcome = []
offbot = []
temp_flood = {}
ssnd = []
rynk = {
    "myProfile": {
        "displayName": "",
    }
}
RfuCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}
kasar = "kontol","memek","kntl","ajg","anjing","asw","anju","gblk","goblok","bgsd","bangsad","bangsat"

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd.startswith('ex\n'):
      if sender in clientMid:
        try:
            sep = text.split('\n')
            ryn = text.replace(sep[0] + '\n','')
            f = open('exec.txt', 'w')
            sys.stdout = f
            print(' ')
            exec(ryn)
            print('\n%s' % str(datetime.now()))
            f.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as r:
                txt = r.read()
            client.sendMessage(to, txt)
        except Exception as e:
            pass
      else:
        client.sendMessage(to, 'Apalo !')
    elif cmd.startswith('exc\n'):
      if sender in clientMid:
        sep = text.split('\n')
        ryn = text.replace(sep[0] + '\n','')
        if 'print' in ryn:
        	ryn = ryn.replace('print(','client.sendExecMessage(to,')
        	exec(ryn)
        else:
        	exec(ryn)
      else:
        client.sendMessage(to, 'Apalo !')

def logError(text):
    client.log("[ Viruѕ тeaм ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def waktu(self,secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

def DESKTOPMAC():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "DESKTOPMAC\t5.9.2\tAditmadzsToken\tTools\t10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers
def DESKTOPWIN():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "DESKTOPWIN\t5.10.0\tAditmadzsToken\tTools\t10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers
def IOSIPAD():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "IOSIPAD\t8.12.2\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def CHROMEOS():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "CHROMEOS\t2.1.5\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def WIN10():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "WIN10\t5.5.5\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def ANDROID():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "ANDROID\t8.12.5\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers

def token(to,nametoken,msg_id,sender):
    try:
        a = nametoken
        a.update({'x-lpqs' : '/api/v4/TalkService.do'})
        transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
        transport.setCustomHeaders(a)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        clienttoken = LineService.Client(protocol)
        qr = clienttoken.getAuthQrcode(keepLoggedIn=1, systemName='AditmadzsToken')
        link = "line://au/q/" + qr.verifier
        client.sendReplyMessage(msg_id, to, "Click This Link Only For 2 Minute :)\n\n{}".format(link))
        a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
        json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
        a.update({'x-lpqs' : '/api/v4p/rs'})
        transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
        transport.setCustomHeaders(a)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        clienttoken = LineService.Client(protocol)
        req = LoginRequest()
        req.type = 1
        req.verifier = qr.verifier
        req.e2eeVersion = 1
        res = clienttoken.loginZ(req)
        try:
            token = res.authToken
            contact = client.getContact(sender)
            client.sendMessage(sender, "Nama : {}\nMid : {}\nTOKEN : {}\n\nCreator".format(contact.displayName,contact.mid,token))
            client.sendContact(sender, clientMid)
        except Exception as e:
            client.sendMessage(to, str(e))
    except Exception as error:
        client.sendMessage(to, "Login Success")

def searchRecentMessages(to,id):
    for a in client.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost
def sendTextTemplate(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "zhr bots",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000033" #999999"
    },
    "header": {
      "backgroundColor": "#FF00FF" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#CCCCCC"            
      },
      {
        "type": "separator",
        "color": "#CCCCCC"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": "🚥 ZHR FAMILY BOTS 🚥",#.format(client.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {
       "contents": [              
         { 
           "type": "separator",
           "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": " ", #format(client.getContact(sender).displayName),
           "size": "xs",
           "align": "center",
           "color": "#0000A0",
           "wrap": True,
           "weight": "bold",
           "type": "text"
           },
           {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#CCCCCC"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate7(to, text, people, people1):
    data = {
                                        "type": "flex",
                                        "altText": "zhr bots",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000033" #999999"
    },
    "header": {
      "backgroundColor": "#FF00FF" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#CCCCCC"            
      },
      {
        "type": "separator",
        "color": "#CCCCCC"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": "🚥 ZHR FAMILY BOTS 🚥",#.format(client.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {
       "contents": [              
         { 
           "type": "separator",
           "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": " ", #format(client.getContact(sender).displayName),
           "size": "xs",
           "align": "center",
           "color": "#0000A0",
           "wrap": True,
           "weight": "bold",
           "type": "text"
           },
           {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#CCCCCC"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)


def sendTextTemplate5(to, text):
    data = {
            "type": "flex",
            "altText": "ZHR,BOTS",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xxs",
            "weight": "bold",
            "wrap": True,
            "color": "#FFFF00"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "sɪʟᴀʜᴋᴀɴ ᴘɪʟɪʜ",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "🎶SOUNDCLOUD🎶",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
    client.postTemplate(to, data)



def sendTextTemplate1(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "zhr bots",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000033" #999999"
    },
    "header": {
      "backgroundColor": "#FF00FF" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#CCCCCC"            
      },
      {
        "type": "separator",
        "color": "#CCCCCC"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": "🚥 ZHR FAMILY BOTS 🚥",#.format(client.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {
       "contents": [              
         { 
           "type": "separator",
           "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": " ", #format(client.getContact(sender).displayName),
           "size": "xs",
           "align": "center",
           "color": "#0000A0",
           "wrap": True,
           "weight": "bold",
           "type": "text"
           },
           {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#CCCCCC"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate2(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "zhr bots",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000033" #999999"
    },
    "header": {
      "backgroundColor": "#FF00FF" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#CCCCCC"            
      },
      {
        "type": "separator",
        "color": "#CCCCCC"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": "🚥 ZHR FAMILY BOTS 🚥",#.format(client.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {
       "contents": [              
         { 
           "type": "separator",
           "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": " ", #format(client.getContact(sender).displayName),
           "size": "xs",
           "align": "center",
           "color": "#0000A0",
           "wrap": True,
           "weight": "bold",
           "type": "text"
           },
           {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#CCCCCC"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate3(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "zhr bots",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000033" #999999"
    },
    "header": {
      "backgroundColor": "#FF00FF" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#CCCCCC"            
      },
      {
        "type": "separator",
        "color": "#CCCCCC"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": "🚥 ZHR FAMILY BOTS 🚥",#.format(client.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {
       "contents": [              
         { 
           "type": "separator",
           "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": " ", #format(client.getContact(sender).displayName),
           "size": "xs",
           "align": "center",
           "color": "#0000A0",
           "wrap": True,
           "weight": "bold",
           "type": "text"
           },
           {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#CCCCCC"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate9(to, text, people, people1):
    warna1 = ("#00ffff","#9933ff","#0033CC","#00ff33","#cc00ff","#ff0033","#003333")
    warnanya1 = random.choice(warna1)
    data = {
                                        "type": "flex",
                                        "altText": "zhr bots",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000033" #999999"
    },
    "header": {
      "backgroundColor": "#FF00FF" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#CCCCCC"            
      },
      {
        "type": "separator",
        "color": "#CCCCCC"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": "🚥 ZHR FAMILY BOTS 🚥",#.format(client.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {
       "contents": [              
         { 
           "type": "separator",
           "color": "#CCCCCC"
            },
           {
            "contents": [
              {
            "text": " ", #format(client.getContact(sender).displayName),
           "size": "xs",
           "align": "center",
           "color": "#0000A0",
           "wrap": True,
           "weight": "bold",
           "type": "text"
           },
           {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#00FF33",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#CCCCCC"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#CCCCCC"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#CCCCCC"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)


def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(client.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~maul-703"
           }                                                
 }
]
                          }
                      }
    client.postTemplate(to, data)

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "ayam"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"

    except Exception as error:
        client.sendMessage(to)
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "goreng"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
    except Exception as error:
        client.sendMessage(to)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"

    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def rynSplitText(text,lp=''):
    separate = text.split(" ")
    if lp == '':
        adalah = text.replace(separate[0]+" ","")
    elif lp == 's':
        adalah = text.replace(separate[0]+" "+separate[1]+" ","")
    else:
        adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
    return adalah


def Pertambahan(a,b):
    jum = a+b
    print(a, "+",b," = ",jum)
def Pengurangan(a,b):
    jum = a-b
    print(a, "-",b," = ",jum)
def Perkalian(a,b):
    jum = a*b
    print(a, "x",b," = ",jum)
def Pembagian(a,b):
    jum = a/b
    print(a, ":",b," = ",jum)
def Perpangkatan(a,b):
    jum = a**b
    print(a,"Pangkat ",b," = ",jum )

def urlEncode(url):
  import base64
  return base64.b64encode(url.encode()).decode('utf-8')

def urlDecode(url):
  import base64
  return base64.b64decode(url.encode()).decode('utf-8')

def removeCmdv(text, key=""):
    setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(" ")
    return text_.replace(sep[0] + " ", "")

def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''
    rmv = len(key + cmd) + 1
    return text[rmv:]

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def commander(text):
    pesan = text.lower()
    if settings["setKey"] == False:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

def backupData():
    try:
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = settings
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = unsend
        f = codecs.open('unsend.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        bekep = tagme
        f = codecs.open('tagme.json','w','utf-8')
        json.dump(bekep, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def GenPictureQRCode(to,url):
    fn=url+".png"
    wildan=pyqrcode.create(url)
    wildan.png(fn, scale=6, module_color=[0, 0, 0, 128], background="#00FFFF")
    wildan.show()
    client.sendImage(to,fn)
    os.remove(fn)

def google_url_shorten(url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    #return resp['id'].replace("https://","")

def generateLink(to, ryn, rynurl=None):
    path = client.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.jpg')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    url = 'https://fahminogameno.life/uploadimage/action.php'
    r = requests.post(url, data=data, files=files)
    client.sendMessage(to, '%s\n%s' % (r.status_code,r.text))
    client.sendMessage(to, '{}{}'.format(rynurl,urlEncode('https://fahminogameno.life/uploadimage/images/ryngenerate.png')))

def uploadFile(ryn):
    url = 'https://fahminogameno.life/uploadimage/action.php'
    path = client.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.png')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    r = requests.post(url, data=data, files=files)
    if r.status_code == 200:
        return path

def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output TeamAnuBot.mp3 {}'.format(link))
    try:
        client.sendAudio(to, 'TeamAnuBot.mp3')
        time.sleep(2)
        os.remove('TeamAnuBot.mp3')
    except Exception as e:
        client.sendMessage(to, 'ãERRORã\nMungkin Link salah cek lagi coba')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
    try:
        client.sendVideo(to, "TeamAnuBot.mp4")
        time.sleep(2)
        os.remove('TeamAnuBot.mp4')
    except Exception as e:
        client.sendMessage(to, ' 「 ERROR 」\nMungkin Link Nya Salah GaN~', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': '「 ERROR 」', 'AGENT_LINK': 'https://line.me/ti/p/~maul-703'})

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "「BOT ACTIVE AGAIN」"
                        client.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~maul-703", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)

def delExpirev2():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "「BOT ACTIVE AGAIN」"
                        client.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~maul-703", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)

def sendHelp():
    sendhelp = settings["autoResponMessage"]
    client.sendMessage(to, sendhelp)
def menuSett():
    if settings['setKey'] == True:
       settings['keyCommand']
    else:
        key = ''
    menuSett =  "☑ sᴇᴛᴘᴇsᴀɴ: ☞ᴛᴇxᴛ ☜" + "\n" + \
                "☑ " + key + "sᴇᴛʀᴇsᴘᴏɴ1: ☞ᴛᴇxᴛ ☜" + "\n" + \
                "☑ " + key + "sᴇᴛʀᴇsᴘᴏɴ2: ☞ᴛᴇxᴛ ☜" + "\n" + \
                "☑ " + key + "sᴇᴛʀᴇsᴘᴏɴ3: ☞ᴛᴇxᴛ ☜" + "\n" + \
                "☑ " + key + "sᴇᴛᴀᴜᴛᴏᴊᴏɪɴ: ☞ᴛᴇxᴛ ☜" + "\n" + \
                "☑ " + key + "sᴇᴛᴀᴜᴛᴏʟᴇᴀᴠᴇ: ☞ᴛᴇxᴛ ☜" + "\n" + \
                "☑ " + key + "sᴇᴛᴄᴏᴍᴍᴇɴᴛ: ☞ᴛᴇxᴛ ☜" + "\n" + \
                "☑ " + key + "sᴇᴛᴡᴇʟᴄᴏᴍᴇ: ☞ᴛᴇxᴛ ☜" + "\n" + \
                "☑ " + key + "sᴇᴛʟᴇᴀᴠᴇ: ☞ᴛᴇxᴛ ☜" + "\n" + \
                "☑ " + key + "ᴄᴇᴋ sɪᴅᴇʀ"
    return menuSett
  
def menuSelf():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuSelf =  "☑ ᴍᴇ" + "\n" + \
                "☑ " + key + "ᴍᴇ" + "\n" + \
                "☑ " + key + "ᴏᴘᴇɴ" + "\n" + \
                "☑ " + key + "ᴄʟᴏsᴇ" + "\n" + \
                "☑ " + key + "ᴜʀʟ" + "\n" + \
                "☑ " + key + "ᴋɪᴄᴋ: ☞@☜" + "\n" + \
                "☑ " + key + "ʀᴇɴᴀᴍᴇ" + "\n" + \
                "☑ " + key + "ᴄʜᴀɴɢᴇʙɪᴏ: ☞ᴛᴇxᴛ☜" + "\n" + \
                "☑ " + key + "ᴘᴇᴏᴘʟᴇ ᴍᴇ" + "\n" + \
                "☑ " + key + "ᴍʏᴜʀʟ" + "\n" + \
                "☑ " + key + "ᴀʟʟ ᴍɪᴅ"
    return menuSelf
  
def menuGrup():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuGrup =  "☑ ʀᴇsᴘᴏɴsᴇɴᴀᴍᴇ ☞@☜" + "\n" + \
                "☑ " + key + "ɢᴇᴛᴍɪᴅ ☞@☜" + "\n" + \
                "☑ " + key + "ɢᴇᴛᴄᴏɴᴛᴀᴄᴛ ☞@☜" + "\n" + \
                "☑ " + key + "ɢᴇᴛɴᴀᴍᴇ ☞@☜" + "\n" + \
                "☑ " + key + "ɢᴇᴛʙɪᴏ ☞@☜" + "\n" + \
                "☑ " + key + "ɢᴇᴛᴘɪᴄᴛᴜʀᴇ ☞@☜" + "\n" + \
                "☑ " + key + "ɢᴇᴛᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ ☞@☜" + "\n" + \
                "☑ " + key + "ɢᴇᴛᴄᴏᴠᴇʀ ☞@☜" + "\n" + \
                "☑ " + key + "ᴄʟᴏɴᴇᴘʀᴏғɪʟᴇ ☞@☜" + "\n" + \
                "☑ " + key + "ᴀᴅᴅғᴀᴠᴏʀɪᴛᴇ ☞@☜" + "\n" + \
                "☑ " + key + "ʀᴇɴᴀᴍᴇ ☞@☜" + "\n" + \
                "☑ " + key + "ғʀɪᴇɴᴅɪɴғᴏ ☞ɴᴜᴍʙᴇʀ☜" + "\n" + \
                "☑ " + key + "ɢɪɴғᴏ"
    return menuGrup

def menuSpcl():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuSpcl =  " ☑  changepict" + "\n" + \
                " ☑ " + key + "changecover" + "\n" + \
                " ☑ " + key + "changevp" + "\n" + \
                " ☑ " + key + "changegrouppicture" + "\n" + \
                " ☑ " + key + "changedual" + "\n" + \
                " ☑ " + key + "grouplist" + "\n" + \
                " ☑ " + key + "memberlist" + "\n" + \
                " ☑ " + key + "user list" + "\n" + \
                " ☑ " + key + "admin list" + "\n" + \
                " ☑ " + key + "bypass" + "\n" + \
                " ☑ " + key + "changekey"
    return menuSpcl
  
def menuMdia():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuMdia =  " ☑  ʏᴏᴜᴛᴜʙᴇ ☞ᴛᴇxᴛ ☜" + "\n" + \
                " ☑ " + key + "ғᴏᴏᴅ ☞ᴛᴇxᴛ ☜" + "\n" + \
                " ☑ " + key + "sᴇᴀʀᴄʜᴀᴘᴘ ☞ᴛᴇxᴛ ☜" + "\n" + \
                " ☑ " + key + "sᴏɴɢ: ☞ʟɪɴᴋ ᴏᴄ sᴍᴜʟᴇ ☜" + "\n" + \
                " ☑ " + key + "sɪɴɢ ☞ɪᴅ sᴍᴜʟᴇ ☜" + "\n" + \
                " ☑ " + key + "ɪᴅ sᴍᴜʟᴇ ☞ɪᴅ sᴍᴜʟᴇ ☜" + "\n" + \
                " ☑ " + key + "ǫᴜʀᴀɴʟɪsᴛ" + "\n" + \
                " ☑ " + key + "ɴᴀᴅᴀǫᴜʀᴀɴᴍᴘ3 ☞ ɴᴏ ☜" + "\n" + \
                " ☑ " + key + "sᴏᴜɴᴅᴄʟᴏᴜᴅ ☞ɴᴀᴍᴀ ᴘᴇɴʏᴀɴʏɪ ☜" + "\n" + \
                " ☑ " + key + "sᴏᴜɴᴅᴄʟᴏᴜᴅ ☞ᴊᴜᴅᴜʟ ☜☞number☜" + "\n" + \
                " ☑ " + key + "ᴢᴏᴅɪᴀᴋ ☞ʙɪɴᴛᴀɴɢ ᴍᴜ☜" + "\n" + \
                " ☑ " + key + "sᴀᴍᴇʜᴀᴅᴀᴋᴜ ☞ɴᴀᴍᴀ ᴀɴɪᴍᴇ☜" + "\n" + \
                " ☑ " + key + "ᴍᴛᴏʜ ☞ᴍᴀsᴇʜɪ ᴛᴏ ʜɪᴊʀɪᴀᴊ☜ ☞ᴅᴀᴛᴇ☜ " + "\n" + \
                " ☑ " + key + "ᴋᴀʟᴇɴᴅᴇʀ"
    return menuMdia

#=====================================================================================
async def clientBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                client.findAndAddContactsByMid(op.param1)
                cover = client.getProfileCoverURL(op.param1)
                data = {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#003333"
        },
        "header": {
          "backgroundColor": "#003333"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "☑ нคℓℓ๏ധ ☑\n{}".format(client.getContact(op.param1).displayName),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#aaaaaa",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#00FFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": settings["autoAddMessage"],
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#00FFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "☑ MyCreator: ☑\n☑ ZHR FAMILY BOTS ☑",
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#aaaaaa",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#00FFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "☑ ᴊɪᴋᴀ ʙᴇʀᴍɪɴᴀᴛ ᴅᴇɴɢᴀɴ ʙᴏᴛ\n☑ ʙᴏʟᴇʜ ᴄᴇᴋ ʟɪsᴛ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ\n☑ 👇👇👇👇",
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"            
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#FF0000",
                  "height": "xs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ☑ ZHR FAMILY BOTS ☑",
            "size": "xs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param1).pictureStatus),
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#003333"
        },
        "header": {
          "backgroundColor": "#003333"
        }
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☑ ℘гσʄıɭε mu ☑",
            "size": "xs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": cover,
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#003333"
        },
        "header": {
          "backgroundColor": "#003333"
        }
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☑ ℘гσʄıɭε ℘εŋɢนŋɖศŋɢ ☑",
            "size": "xs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                client.postFlex(op.param1, data)
                data = {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#003333"
        },
        "header": {
          "backgroundColor": "#003333"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "☑ ʙᴏᴛ ᴄʟ ᴘʀᴏᴛᴇᴄᴛ ☑",
            "color": "#ff0000",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "xs",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#00FFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ 5 вσтs",
                    "color": "#00ff00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          
          {
            "text": "☑ 20K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url":"https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ 7 вσтs",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 150K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url":"https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ 10 вσтs",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url":"https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ 15 вσтs",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☑ ØP€Ň ØŘĐ€Ř ☑",
            "size": "xs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~maul-703"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#003333"
        },
        "header": {
          "backgroundColor": "#003333"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "☑ sᴇʟғ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ",
            "color": "#00FF00",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "xs",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#00FFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ 5 ᴀsɪsᴛ",
                    "color": "#00ff00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 20k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ 10 ᴀsɪsᴛ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 180k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ 15 ᴀsɪsᴛ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ 20 ᴀsɪsᴛ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 300k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☑ ØP€Ň ØŘĐ€R ☑",
            "size": "xs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~maul-703"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "body": {
        "type": "cover",
        "backgroundColor": "#FF0099"
      },
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#003333"
        },
        "header": {
          "backgroundColor": "#003333"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "☑ sᴇʟғ ʙᴏᴛ price ☑",
            "color": "#00FF00",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#00FFFF"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ sᴇʟғʙᴏᴛ ɴᴏ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 60k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ sᴇʟғʙᴏᴛ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 5k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ sᴇʟғʙᴏᴛ 5 ᴀsɪsᴛ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 120k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ sᴇʟғʙᴏᴛ 7 ᴀsɪsᴛ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 150k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☑ ØP€Ň ØŘĐ€R ☑",
            "size": "xs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~maul-703"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#003333"
        },
        "header": {
          "backgroundColor": "#003333"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "☑ ᴘᴇᴍᴀsᴀɴɢᴀɴ ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ",
            "color": "#00FF00",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "xs",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#00FF00"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ ʀᴏᴏᴍ / ɢᴄ sᴍᴜʟᴇ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 120k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ ʀᴏᴏᴍ ᴇᴠᴇɴᴛ sᴍᴜʟᴇ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 180k Sampai Selesai",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ ʀᴏᴏᴍ ᴄʜᴀᴛᴛɪɴɢ",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ 180k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xs",
                    "type": "icon",
                    "url": "https://avatars3.githubusercontent.com/u/48912948?s=400&v=4"
                  },
                  {
                    "text": "☑ DLL",
                    "color": "#00FF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "☑ pm aje mas bro ☑",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☑ ØP€Ň ØŘĐ€Ř ☑",
            "size": "xs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~maul-703"
            },
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}

                client.postFlex(op.param1, data)

        if op.type == 13:
            if settings["autoJoin"] and clientMid in op.param3:
                group = client.getGroup(op.param1)
                group.notificationDisabled = False
                client.acceptGroupInvitation(op.param1)
                client.updateGroup(group)
                ginfo = client.getGroup(op.param1)
                data = {
   "contents": [{
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "🚥⟬ғᴏᴛᴏ ᴘᴇɴɢᴜɴᴅᴀɴɢ⟭🚥",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [                      
{
"type": "separator",
"color": "#33ffff"
},{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [ 
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(client.getContact(op.param2).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         #natase
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/4N1BjnV/20190427-175005.png", #watshaphttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/6282135759022",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://call/contacts"
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🚥C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞Z̸͟͞🚥",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~maul-703",
          },
           "align": "center"
          }
        ]
      }
    }, #Batas1
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "🚥⟬ᴘʀᴏғɪʟᴇ ɢʀᴏᴜᴘ⟭🚥",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
{
"type": "separator",
"color": "#33ffff"
}, #Fotoprofile
{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(client.getGroup(op.param1).pictureStatus),
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(group.name),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
       "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"   
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🚥C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞Z̸͟͞🚥",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~maul-703",
          },
           "align": "center"
          }
        ]
      }
 }, #Batas1
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text":"🚥⟬ᴛʜᴀɴᴋs ғᴏʀ ɪɴᴠɪᴛᴇ⟭🚥",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
{
"type": "separator",
"color": "#33ffff"
}, #Fotoprofile
{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [         
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(client.getContact(op.param2).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
       "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },{
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",
           }, 
            "flex": 1            
          },{
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },{
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },{
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },{
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🚥C̸͟͞R̸͟͞E̸͟͞A̸͟͞T̸͟͞O̸͟͞R̸͟͞ B̸͟͞O̸͟͞T̸͟͞Z̸͟͞🚥",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~maul-703",
          },
           "align": "center"
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                client.postFlex(op.param1, data)


        if op.type == 13:
            if settings["autoLeave"] and clientMid in op.param3:
                group = client.getGroup(op.param1)
                group.notificationDisabled = False
                client.acceptGroupInvitation(op.param1)
                client.updateGroup(group)
                client.sendMessage(op.param1, settings["autoLeaveMessage"])
                client.leaveGroup(op.param1)
        
#=====================BAHAN WELCOME DAN LEAVE============================
        if op.type == 15:
            if settings["welcome"] == True:
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2).picturePath
                cover = client.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                warna1 = ("#00ffff","#9933ff","#0033CC","#00ff33","#ffffff","#ff0033","#003333")
                warnanya1 = random.choice(warna1)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                data = {
                                "type": "flex",
                                "altText": "ZHR BOTS",
                                "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#003399"
    }
  },
  "type": "bubble",
  "size": "micro",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "text":"☑ Bye bye sob\n\n☑ see you next time\n\n☑ {}".format(client.getContact(op.param2).displayName),
            "size": "xxs",
            "color": "#00FF33",
            "wrap": True,
            "type": "text",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#00ff00"
          },
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
            "type": "image",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "4:5"
          }       
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "flex": 2,
          "contents": [{
              "type": "button",
              "style": "secondary",
              "color": "#ff0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                  "uri": "http://line.me/ti/p/~maul-703"
              }
          }]
      }]
  }
}
}
                client.postTemplate(op.param1, data)

        if op.type == 17:
            if settings["welcome"] == True:
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2).picturePath
                cover = client.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                warna1 = ("#00ffff","#9933ff","#0033CC","#00ff33","#cc00ff","#ff0033","#003333")
                warnanya1 = random.choice(warna1)
                data = {
                                       "type": "flex",
                                       "altText": "welcome",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif", #https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ᴡᴇʟᴄᴏᴍᴇ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~slanker123456",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "80px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚺{} ".format(client.getContact(op.param2).displayName),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": settings["welcome"],
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "125px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif", #https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ᴡᴇʟᴄᴏᴍᴇ", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/6282135759022",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
"size": "full",
"action": {
"type": "uri",
"uri": "https://youtube.com",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🏡ɢʀᴏᴜᴘ",
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "90px",
"height": "16px",
"width": "52px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚺{}".format(client.getContact(op.param2).displayName),
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🏠{}".format(ginfo.name),
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "125px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                client.postTemplate(op.param1, data)

#==========================BAGIAN PROTECT ANTIJS=========================================
        if op.type == 19:
            if op.param1 in protectantijs:
                if clientMid in op.param3:
                    if op.param2 in Bots:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        settings["blackList"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        client.inviteIntoGroup(op.param1,[Zmid])

#=========================BAGIAN SIDER=================================================
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)

        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = client.getContact(op.param2).displayName
                    ginfo = client.getGroup(op.param1)
                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                    group = client.getGroup(op.param1)
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    group.notificationDisabled = False
                    client.updateGroup(group)
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = client.getContact(op.param2)
                        warna1 = ("#00ffff","#9933ff","#0033CC","#00ff33","#cc00ff","#ff0033","#003333")
                        warnanya1 = random.choice(warna1)
                        data = {
                                       "type": "flex",
                                       "altText": "zhr bots cctv",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#0000A0",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://gifimage.net/wp-content/uploads/2018/06/ukuran-gif-dp-bbm-5.gif", 
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://content.skyscnr.com/m/7d3992c451e6cf6c/original/color.gif?imbypass=true",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",  #"https://em.wattpad.com/4c7e5d80bb78b4c9abde154708b4efdb4e71c0c6/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f6b63787836516f3833615a7a43413d3d2d3639323032383336312e313538306535356565336436353532663138343830393632343530302e676966?s=fit&w=720&h=720", #https://thumbs.gfycat.com/WickedMeekGazelle-size_restricted.gif",
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "21px",
"offsetStart": "21px",
"height": "157px",
"width": "117px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(client.getGroup(op.param1).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "27px",
"offsetStart": "27px",
"height": "145px",
"width": "105px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "27px",
"offsetStart": "27px",
"height": "145px",
"width": "105px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "text",
"text": "SIDER", 
"align": "center",
"color": "#aaaaaa",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "29px",
"backgroundColor": "#808080",
"offsetStart": "30px",
"height": "13px",
"width": "34px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~maul-703",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "42px",
"offsetStart": "24px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ffff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "120px",
"backgroundColor": "#00ff00",
"offsetStart": "70px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": settings["sider"],
"weight": "bold",
"color": "#aaaaaa",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "138px",
"backgroundColor": "#0000CC",
"offsetStart": "47px",
"height": "16px",
"width": "84px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚹{} ".format(client.getContact(op.param2).displayName),
"weight": "bold",
"color": "#ffffff",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "155px",
#"backgroundColor": "#ac00c8",
"offsetStart": "29px",
"height": "16px",
"width": "105px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                        client.postTemplate(op.param1, data),
#=======================================================================================================

        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                cmd = command(text)
                ryyn = "u1114bedb28e7280bb83ec5adba6e68bb"
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
#====================BAGIAN MUTE & UNMUTE===================================================================================================================
                        if cmd == "off":
                              if msg._from in admin:
                                if to not in offbot:
                                  sendTextTemplate(to, "❂➣ Mode Mute Active Di Group ini")
                                  offbot.append(to)
                                  print(to)
                                else:
                                  sendTextTemplate(to, "❂➣ Sukses Menonaktifkan Mute di Room ini")

                        elif cmd == "on":
                              if msg._from in admin:
                                if to in offbot:
                                  offbot.remove(to)
                                  sendTextTemplate(to, "❂➣ Mode Mute Aktif")
                                  print(to)
                                else:
                                  sendTextTemplate(to, "❂➣ Sukses Mengaktifkan Mute Di Room ini")

                        elif cmd == "reset cok":
                              if msg._from in admin:
                                restart = "ʙᴏᴛ sᴜᴋsᴇs ᴅɪ ʀᴇsᴇᴛ ᴜʟᴀɴɢ ʙᴏs"
                                contact = client.getContact(sender)
                                sendTextTemplate(to, restart)
                                restartBot()

                        elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - clientStart
                                runtime = timeChange(runtime)
                                run = "❂?🇩➣ ʙᴏᴛ ᴛᴇʟᴀʜ ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ\n⏰{}".format(str(runtime))
                                sendTextTemplate(to, run)

                        elif cmd == "speed":
                            	get_profile_time_start = time.time()
                            	get_profile = client.getProfile()
                            	get_profile_time = time.time() - get_profile_time_start
                            	speed = " {} ᴅᴇᴛɪᴋ".format(str(get_profile_time))
                            	sendTextTemplate(to, speed)

                        elif cmd == "gid":
                              if msg._from in admin:
                                gid = client.getGroupIdsJoined()
                                h = ""
                                for i in gid:
                                    h += "❂➣ %s:\n%s\n\n" % (client.getGroup(i).name,i)
                                sendTextTemplate(to,"                 ĐΔ₣ŦΔŘ IĐ GŘØỮPŞ\n\n"+h)

                        elif cmd == "namagroup":
                              if msg._from in admin:
                                gid = client.getGroup(to)
                                sendTextTemplate(to, "🔹 ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ 🔹\n❂➣ {}".format(gid.displayName))

                        elif cmd == "fotogroup":
                              if msg._from in admin:
                                gid = client.getGroup(to)
                                sendTextTemplate(to,"http://dl.profile.line-cdn.net/{}".format(gid.pictureStatus))

                        elif cmd == "reject":
                              if msg._from in admin:
                                ginvited = client.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        client.rejectGroupInvitation(gid)
                                    sendTextTemplate(to, "❂➣ ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ {} ᴜɴᴅᴀɴɢᴀɴ ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                                else:
                                    sendTextTemplate(to, "❂➣ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜɴᴅᴀɴɢᴀɴ ʏᴀɴɢ ᴛᴇʀᴛᴜɴᴅᴀ")

                        elif cmd.startswith("setkey: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                settings["keyCommand"] = str(key).lower()
                                sendTextTemplate(to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴜʙᴀʜ sᴇᴛ ᴋᴇʏ ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴊᴀᴅɪ : 「{}」".format(str(key).lower()))

                        elif cmd == "help":
                              if msg._from in admin:
                                with open("help.json","r") as f:
                                    data = json.load(f)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                            if len(ret_) >= 5:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["link"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "{}".format(str(fn["name"])),
                                                        "uri": "{}".format(str(fn["linkliff"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//5
                                    for aa in range(k+1):
                                        data = {
                                                "type": "template",
                                                "altText": "Help Message",
                                                "template": {
                                                    "type": "image_carousel",
                                                    "columns": ret_[aa*5 : (aa+1)*5]
                                                }
                                            }
                                        client.postTemplate(to, data)

                        elif cmd == "status":
                              if msg._from in admin:
                                helpStatus = menuStat()
                                people1 = "🇮🇩 sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ 🇮🇩"
                                people = "ᴜsᴇʀ{}".format(client.getProfile().displayName)
                                sendTextTemplate7(to, helpStatus, people, people1)

                        elif cmd == "settings":
                              if msg._from in admin:
                                helpSettings = menuSett()
                                people1 = "🇮🇩 sᴇᴛᴛɪɴɢ ᴍᴇssᴀɢᴇ ??"
                                people = "ᴜsᴇʀ{}".format(client.getProfile().displayName)
                                sendTextTemplate7(to, helpSettings, people, people1)

                        elif cmd == "self":
                              if msg._from in admin:
                                helpSelf = menuSelf()
                                people1 = "🇮🇩 sᴇʟғ ᴍᴇssᴀɢᴇ 🇮🇩"
                                people = "ᴜsᴇʀ{}".format(client.getProfile().displayName)
                                sendTextTemplate7(to, helpSelf, people, people1)

                        elif cmd == "group":
                              if msg._from in admin:
                                helpGroup = menuGrup()
                                people1 = "🇮🇩 ɢʀᴏᴜᴘ ᴍᴇssᴀɢᴇ 🇮🇩"
                                people = "ᴜsᴇʀ{}".format(client.getProfile().displayName)
                                sendTextTemplate7(to, helpGroup, people, people1)

                        elif cmd == "special":
                              if msg._from in admin:
                                helpSpecial = menuSpcl()
                                people1 = "🇮🇩 sᴘᴇᴄɪᴀʟ ᴍᴇssᴀɢᴇ 🇮🇩"
                                people = "ᴜsᴇʀ{}".format(client.getProfile().displayName)
                                sendTextTemplate7(to, helpSpecial, people, people1)

                        elif cmd == "media":
                              if msg._from in admin:
                                helpMedia = menuMdia()
                                people1 = "🇮🇩 ᴍᴇᴅɪᴀ ᴍᴇssᴀɢᴇ 🇮🇩"
                                people = "ᴜsᴇʀ{}".format(client.getProfile().displayName)
                                sendTextTemplate7(to, helpMedia, people, people1)

                        elif cmd == "remove":
                              if msg._from in admin:
                                client.removeAllMessages(op.param2)
                                sendTextTemplate(to, "sᴜᴄᴄᴇsғᴜʟʟʏ ᴄʟᴇᴀʀ ᴍᴇssᴀɢᴇs")

                        elif cmd == "set":
                              if msg._from in admin:
                                people = "🇮🇩 ŞŦΔŦỮŞ Μ€ŞŞΔG€ 🇮🇩"
                                ret_ = "🌠"
                                if settings["unsend"] == True: ret_ += "\n❂➢ ᴜɴsᴇɴᴅ : ✅"
                                else: ret_ += "\n❂➢ ᴜɴsᴇɴᴅ : ❌"
                                if settings["checkContact"] == True: ret_ += "\n❂➢ ᴄᴏɴᴛᴀᴄᴛ : ✅"
                                else: ret_ += "\n❂➢ ᴄᴏɴᴛᴀᴄᴛ : ❌"
                                if settings["cloneContact"] == True: ret_ += "\n❂➢ ᴄʟᴏɴᴇᴄᴏɴᴛᴀᴄᴛ : ✅"
                                else: ret_ += "\n❂➢ ᴄʟᴏɴᴇᴄᴏɴᴛᴀᴄᴛ : ❌"                                    
                                if settings["checkPost"] == True: ret_ += "\n❂➢ ᴘᴏsᴛ : ✅"
                                else: ret_ += "\n❂➢ ᴘᴏsᴛ : ❌"
                                if settings["checkSticker"] == True: ret_ += "\n❂➢ ᴄʜᴇᴄᴋsᴛɪᴄᴋᴇʀ : ✅"
                                else: ret_ += "\n❂➢ ᴄʜᴇᴄᴋsᴛɪᴄᴋᴇʀ : ❌"
                                if settings["setKey"] == True: ret_ += "\n❂➢ Set Key : ✅"
                                else: ret_ += "\n❂➢ Set Key : ❌"
                                if settings["autoAdd"] == True: ret_ += "\n❂➢ ᴀᴜᴛᴏᴀᴅᴅ : ✅"
                                else: ret_ += "\n❂➢ ᴀᴜᴛᴏᴀᴅᴅ : ❌"
                                if settings["mimic"]["status"] == True: ret_ += "\n❂➢ ᴍɪᴍɪᴄ : ✅"
                                else: ret_ += "\n❂➢ ᴍɪᴍɪᴄ : ❌"
                                if to in welcome: ret_ +="\n❂➢ ᴡᴇʟᴄᴏᴍᴇ : ✅"
                                else: ret_ +="\n❂➢ ᴡᴇʟᴄᴏᴍᴇ : ❌" 
                                if settings["delFriend"] == True: ret_ += "\n❂➢ ᴅᴇʟᴇᴛᴇғʀɪᴇɴᴅ : ✅"
                                else: ret_ += "\n❂➢ ᴅᴇʟᴇᴛᴇғʀɪᴇɴᴅ : ❌"
                                if settings["autoRespon"] == True: ret_ += "\n❂➢ ᴀᴜᴛᴏʀᴇsᴘᴏɴ1 : ✅"
                                else: ret_ += "\n❂➢ ʀᴇsᴘᴏɴ1 : ❌"
                                if settings["autoRes"] == True: ret_ += "\n❂➢ ᴀᴜᴛᴏʀᴇsᴘᴏɴ2 : ✅"
                                else: ret_ += "\n❂➢ ʀᴇsᴘᴏɴ2 : ❌"
                                if settings["autoRespek"] == True: ret_ += "\n❂➢ ᴀᴜᴛᴏʀᴇsᴘᴏɴ3 : ✅"
                                else: ret_ += "\n❂➢ ʀᴇsᴘᴏɴ3 : ❌"
                                if settings["autoReply"] == True: ret_ += "\n❂➢ ᴀᴜᴛᴏʀᴇᴘʟʏ : ✅"
                                else: ret_ += "\n❂➢ ᴀᴜᴛᴏʀᴇᴘʟʏ : ❌"
                                if to in settings["sticker"] == True: ret_ += "\n❂➢ sᴛɪᴄᴋᴇʀ : ✅"
                                else: ret_ += "\n❂➢ sᴛɪᴄᴋᴇʀ : ❌"
                                if to in settings["sniff"] == True: ret_ += "\n❂➢ Sniff Mode : ✅"
                                else: ret_ += "\n❂➢ Sniff Mode : ❌"
                                if settings["autoJoin"] == True: ret_ += "\n❂➢ ᴀᴜᴛᴏᴊᴏɪɴ : ✅"
                                else: ret_ += "\n❂➢ ᴀᴜᴛᴏᴊᴏɪɴ : ❌"
                                if settings["autoLeave"] == True: ret_ += "\n❂➢ ᴀᴜᴛᴏʟᴇᴀᴠᴇ : ✅"
                                else: ret_ += "\n❂➢ ᴀᴜᴛᴏʟᴇᴀᴠᴇ : ❌"
                                if settings["autoJoinTicket"] == True: ret_ += "\n❂➢ ᴀᴜᴛᴏᴊᴏɪɴᴛɪᴄᴋᴇᴛ : ✅"
                                else: ret_ += "\n❂➢ ᴀᴜᴛᴏᴊᴏɪɴᴛɪᴄᴋᴇᴛ : ❌"
                                if settings["autoRead"] == True: ret_ += "\n❂➢ ᴀᴜᴛᴏʀᴇᴀᴅ : ✅"
                                else: ret_ += "\n❂➢ ᴀᴜᴛᴏʀᴇᴀᴅ : ❌"
                                if to in protectantijs: ret_ +="\n❂➢ ᴀɴᴛɪᴊs : ✅"
                                else: ret_ +="\n❂➢ ᴀɴᴛɪᴊs : ❌"
                                people1 = "вy: ZHR FAMILY BOTS"
                                sendTextTemplate9(to, ret_+"🌠", people, people1)


                        elif cmd == "open":
                              if msg._from in admin:
                                if msg.toType == 2:
                                   X = client.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   client.updateGroup(X)
                                   sendTextTemplate(to, "❂➣ Url Opened")

                        elif cmd == "close":
                              if msg._from in admin:
                                  if msg.toType == 2:
                                     X = client.getGroup(msg.to)
                                     X.preventedJoinByTicket = True
                                     client.updateGroup(X)
                                     sendTextTemplate(to, "❂➣ Url Closed")

                        elif cmd == "url":
                              if msg._from in admin:
                                  if msg.toType == 2:
                                     x = client.getGroup(msg.to)
                                     if x.preventedJoinByTicket == True:
                                        x.preventedJoinByTicket = False
                                        client.updateGroup(x)
                                     gurl = client.reissueGroupTicket(msg.to)
                                     sendTextTemplate(to, "❂➣ Nama : "+str(x.name)+ "\n❂➣ Url grup : http://line.me/R/ti/g/"+gurl)                                                                                                                                              


#=BAGIAN DAFTAR GROUP STICKER DAN TEMAN SERTA ANGGOTA GROUP===========================
                        elif cmd == "grouplist":
                              if msg._from in admin:
                                groups = client.getGroupIdsJoined()
                                ret_ = ""
                                no = 0
                                for gid in groups:
                                    group = client.getGroup(gid)
                                    no += 1
                                    ret_ += "\n🎉 {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                people = "🌟🌠TOAL {} YOUR GROUPS 🌠🌟".format(str(len(groups)))
                                people1 = "🌟🇮🇩 LIST YOUR GROUPS 🇮🇩🌟"
                                sendTextTemplate7(to, str(ret_), people, people1)

                        elif cmd == "memberlist":
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    num = 0
                                    ret_ = ""
                                    for contact in group.members:
                                        num += 1
                                        ret_ += "\n🎎 {}. {}".format(num, contact.displayName)
                                    people = "✨🇮🇩 TOTAL {} MEMBERS 🇮🇩✨".format(len(group.members))
                                    people1 = "🏆🇮🇩 LIST MEMBERS 🇮🇩🏆"
                                    sendTextTemplate7(to, str(ret_), people, people1)

                        elif cmd == "user list":
                              if msg._from in admin:
                                if owner == []:
                                   sendTextTemplate(to, "User Is Empty")
                                else:
                                    sendTextTemplate(to, "➢ Tunggu Boss ku")
                                    user = ""
                                    user = "❂🇮🇩➢ User List"
                                    for mid in owner:
                                        user += "\n\n➢ "+client.getContact(mid).displayName
                                    user += "\n\n❂🇮🇩➢ Finish"
                                    sendTextTemplate(to, user)

                        elif cmd == "admin list":
                              if msg._from in admin:
                                if admin == []:
                                   sendTextTemplate(to, "Admin Is Empty")
                                else:
                                    sendTextTemplate(to, "➢ Tunggu Boss ku")
                                    user = ""
                                    user = "❂🇮🇩➢ Admin List"
                                    for mid in admin:
                                        user += "\n\n➢ "+client.getContact(mid).displayName
                                    user += "\n\n❂🇮🇩➢ Finish"
                                    sendTextTemplate(to, user)

                        elif cmd == "list sticker":
                              if msg._from in admin:
                                 no = 0
                                 ret_ = "❂🇮🇩➢ List Your Sticker \n\n"
                                 for sticker in stickers:
                                     no += 1
                                     ret_ += str(no) + ". " + sticker.title() + "\n"
                                 ret_ += "\n\n❂🇮🇩➢ Total {} Stickers".format(str(len(stickers)))
                                 sendTextTemplate(to, ret_)

                        elif cmd == "list sticker template":
                              if msg._from in admin:
                                 no = 0
                                 ret_ = "❂🇮🇩➢ Daftar Sticker Template\n\n"
                                 for sticker in stickerstemplate:
                                     no += 1
                                     ret_ += str(no) + ". " + sticker.title() + "\n"
                                 ret_ += "\n\n❂🇮🇩➢ Total {} Stickers Template".format(str(len(stickers)))
                                 sendTextTemplate(to, ret_)

                        elif cmd == "listmp3":
                              if msg._from in admin:
                                no = 0
                                ret_ = "🎶Daftar Lagu🎶\n\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str(no) + ". " + audio.title() + "\n"
                                ret_ += "\n❂🇮🇩➢ Total {} Lagu".format(str(len(audios)))
                                sendTextTemplate(to, ret_)

                        elif cmd == "friendlist":
                              if msg._from in admin:
                                contacts = client.getAllContactIds()
                                num = 0
                                result = ""
                                for listContact in contacts:
                                    contact = client.getContact(listContact)
                                    num += 1
                                    result += "\n🍬🇮🇩 {}. {}".format(num, contact.displayName)
                                people = "\n🎂🇮🇩 TOTAL {} FRIENDS 🇮🇩🎂".format(len(contacts))
                                people1 = "👔🇮🇩 LIST YOUR FRIENDS 🇮🇩👔"
                                sendTextTemplate7(to, str(result), people, people1)


#======================BAGIAN UPDATING STICKER BIASA==============================
                        elif cmd.startswith("addsticker "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["addSticker"]["status"] = True
                                    settings["addSticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = {}
                                    f = codecs.open('sticker.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "❂🇮🇩➢ Send your stickers!")
                                else:
                                    sendTextTemplate(to, "❂🇮🇩➢ Stickers name already in List!")                     

                        elif cmd.startswith("delsticker "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil menghapus sticker:\n❂🇮🇩➢ {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(to, "❂🇮??➢ Sticker itu tidak ada dalam list")

#=========================BAGIAN UPADATING STICKER TEMPLATE================================
                        elif cmd.startswith("addstickertemplate "):
                              if msg._from in admin:
                                ssn = client.getContact(sender).mid
                                ssnd.append(ssn)
                                if sender in ssnd:
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name not in stickers:
                                      settings["addStickertemplate"]["statuss"] = True
                                      settings["addStickertemplate"]["namee"] = str(name.lower())
                                      stickerstemplate[str(name.lower())] = {}
                                      f = codecs.open('stickertemplate.json','w','utf-8')
                                      json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      sendTextTemplate(to, "❂🇮🇩➢ Send your stickers!")
                                  else:
                                      sendTextTemplate(to, "❂🇮🇩➢ Stickers name already in List!")

                        elif cmd.startswith("deletstickertemplate "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickerstemplate:
                                    del stickerstemplate[str(name.lower())]
                                    f = codecs.open("stickertemplate.json","w","utf-8")
                                    json.dump(stickerstemplate, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil menghapus sticker\n❂🇮🇩➢ {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(to, "❂🇮🇩➢ Sticker itu tidak ada didalam list")

#=====================BAGIAN UPDATENG MP3==============================================
                        elif cmd.startswith("addmp3 "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["statuss"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "❂🇮🇩➢ Silahkan kirim mp3 nya") 
                                else:
                                    sendTextTemplate(to, "❂🇮🇩➢ Mp3 itu sudah didalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    client.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil menghapus mp3:\n❂🇮🇩➢ {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(to, "❂🇮🇩➢ Mp3 itu tidak ada dalam list") 

#=============== BAGIAN UPDATE KEY =====================================================================================
                        elif cmd.startswith("changekey"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                settings["tatan"] = "{}".format(txt)
                                sendTextTemplate(to, "❂🇮🇩➢ Succesfully Changekey:\n❂🇮🇩➢ {}".format(settings["tatan"]))

                        elif text.lower() == "mykey":
                              if msg._from in admin:
                                sendTextTemplate(to, "❂🇮🇩➢ Keycommand saat ini :\n❂🇮🇩➢ {}".format(str(settings["keyCommand"])))

                        elif text.lower() == "setkey on":
                              if msg._from in admin:
                                if settings["setKey"] == True:
                                    sendTextTemplate(to, "❂🇮🇩➢ Setkey Telah aktif Bosku")
                                else:
                                    settings["setKey"] = True
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil mengaktifkan setkey")

                        elif text.lower() == "setkey off":
                              if msg._from in admin:
                                if settings["setKey"] == False:
                                    sendTextTemplate(to, "❂🇮🇩➢ Setkey telah nonaktif")
                                else:
                                    settings["setKey"] = False
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil menonaktifkan setkey")
                        if text is None: return

#==============BAGIAN UPDATE GROUP==========================================================================================
                        elif cmd.startswith("dor "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.kickoutFromGroup(to, [ls])

                        elif cmd.startswith("rename: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 999:
                                    profile = client.getProfile()
                                    profile.displayName = name
                                    client.updateProfile(profile)
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil mengubah nama menjadi :\n❂🇮🇩➢ {}".format(name))
                              else:
                                  txt = ("❂🇮🇩➢ Silahkan Di Ciba Lagi")
                                  pop = random.choice(txt)
                                  sendTextTemplate(to, pop)

                        elif cmd.startswith("changebio: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                bio = text.replace(sep[0] + " ","")
                                if len(bio) <= 500:
                                    profile = client.getProfile()
                                    profile.statusMessage = bio
                                    client.updateProfile(profile)
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil mengubah bio menjadi :\n❂🇮🇩➢ {}".format(bio))

                        elif cmd == "virus me":
                                client.sendMention(to, "@!", [sender])
                                client.sendFakeReplyContact(msg_id, to, sender)

                        elif cmd == "myurl":
                              if msg._from in admin:
                                client.reissueUserTicket()
                                arr = client.profile.displayName + "\n❂🇮🇩➢ Ticket URL :\n http://line.me/ti/p/" + client.getUserTicket().id
                                sendTextTemplate(to, arr)

                        elif text.lower() == "my mid":
                              if msg._from in admin:
                               sendTextTemplate(to, msg._from)
                               
                        elif text.lower() == "mid":
                               client.sendMessage(to, msg._from)
                               
                        elif cmd == "myname":
                              if msg._from in admin:
                                contact = client.getContact(sender)
                                sendTextTemplate(to, "💠Your Name :\n💠 {}".format(contact.displayName))

                        elif cmd == "mybio":
                              if msg._from in admin:
                                contact = client.getContact(sender)
                                sendTextTemplate(to, "💠Your Bio :\n💠 {}".format(contact.statusMessage))

                        elif cmd == "mypicture":
                              if msg._from in admin:
                                contact = client.getContact(sender)
                                client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                        elif cmd == "myvideoprofile":
                              if msg._from in admin:
                                contact = client.getContact(sender)
                                if contact.videoProfile == None:
                                    return sendTextTemplate(to, "Anda tidak memiliki video profile")
                                client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                        elif cmd == "mu":
                              if msg._from in admin:
                                cover = client.getProfileCoverURL(sender)
                                client.sendImageWithURL(to, str(cover))

                        elif cmd == "mycover url":
                              if msg._from in admin:
                                cover = client.getProfileCoverURL(sender)
                                sendTextTemplate(to, str(cover))

                        elif cmd == "myteam":
                            if msg._from in admin:
                                for i in Bots:
                                    contact = client.getContact(i)
                                    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+contact.pictureStatus, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': contact.statusMessage, 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': contact.displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+i,'MSG_SENDER_NAME':  contact.displayName,}
                                    client.sendMessage(msg.to, contact.displayName, contentMetadata, 19)      


                        elif cmd == "byeme":
                              if msg._from in admin:
                                G = client.getGroup(to)
                                data = {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "🇮🇩 ŋศɱศ ɢгσน℘ 🇮🇩\n{}".format(G.name),
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "sᴏʀʀʏ ᴋᴀᴋ sᴀʏᴀ ɪᴢɪɴ ᴘᴀᴍɪᴛ\nᴍᴏʜᴏɴ ᴍᴀᴀᴘ ᴋᴀʟᴀᴜ sᴇʟᴀᴍᴀ\nsᴀʏᴀ ʙᴇʀɢᴀʙᴜɴɢ ᴅɪɢʀᴏᴜᴘ ᴋᴀᴋᴀᴋ\nsᴀʏᴀ ʙᴀɴʏᴀᴋ ᴋᴇsᴀʟᴀʜᴀɴ\nᴅᴀʀɪ ᴛᴜᴛᴜʀ ᴋᴀᴛᴀᴋᴜ ʏᴀɴɢ\nᴘᴇʀɴᴀʜ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇʀsɪɴɢɢᴜɴɢ\n🙏 ᴛᴇʀɪᴍᴀᴋᴀsɪʜ 🙏 ",
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "🇮🇩 sαℓαм ∂αri sαyα 🇮🇩\n{}".format(client.getContact(sender).displayName),
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"            
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#0000CC",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "Cʜᴀᴛ ᴛᴏ ᴄƦᴇᴀᴛᴏƦ",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ZH,BOTS",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFF00",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#0000CC",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "Cʜᴀᴛ ᴛᴏ ᴄƦᴇᴀᴛᴏƦ",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "℘гσʄıɭε ɢгσน℘",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFF00",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(client.getGroup(to).pictureStatus),
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#0000CC",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "Cʜᴀᴛ ᴛᴏ ᴄƦᴇᴀᴛᴏƦ",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "℘гσʄıɭε ℘εŋɢนŋɖศŋɢ",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFF00",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)
                                client.leaveGroup(to)


#====================UPDATING IS FRIEND AND GROUPS =================================
                        elif cmd == "respon":
                              if sender in admin:
                                group = client.getGroup(to)
                                midMembers = [contact.mid for contact in group.members]
                                for data in midMembers:
                                    sendTextTemplate(to, "{}".format(client.getContact(data).displayName), contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(data).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(data).pictureStatus)})

                        elif cmd.startswith("getmid "):
                              if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                mi = client.getContact(key1)
                                sendTextTemplate(to, "💠 Nama : "+str(mi.displayName)+"\n💠 MID : " +key1)

                        elif cmd.startswith("getcontact "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                client.sendContact(to, txt);

                        elif cmd.startswith("getname "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        sendTextTemplate(to, "💠 Nama :\n "+str(mi.displayName), [ls])

                        elif cmd.startswith("getbio "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        sendTextTemplate(to, "Status Message {}".format(contact.statusMessage), [ls])

                        elif cmd.startswith("getpicture "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                        elif cmd.startswith("getvideoprofile "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        if contact.videoProfile == None:
                                            return client.sendMention(to, "@!tidak memiliki video profile", [ls])
                                        client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                        elif cmd.startswith("getcover "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cover = client.getProfileCoverURL(ls)
                                        client.sendImageWithURL(to, str(cover))

                        elif cmd.startswith("cloneprofile "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.cloneContactProfile(ls)
                                        client.sendContact(to, sender)
                                        sendTextTemplate(to, "Berhasil clone profile")

                        elif cmd == "invite to group":
                              if msg._from in admin:
                                if settings["groupInvite"] == True:
                                    sendTextTemplate(to, "Kirim Kontaknya Boss")
                                else:
                                    settings["groupInvite"] = True
                                    sendTextTemplate(to, "Kirim Kontaknya Boss")

                        elif cmd.startswith("friendinfo "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                contacts = client.getAllContactIds()
                                try:
                                    listContact = contacts[int(query)-1]
                                    contact = client.getContact(listContact)
                                    cover = client.getProfileCoverURL(listContact)
                                    result = "❂🇮🇩➢ Details Profile 🎉"
                                    result += "\n❂🇮🇩➢ Display Name : @!"
                                    result += "\n❂🇮🇩➢ Mid : {}".format(contact.mid)
                                    result += "\n❂🇮🇩➢ Status Message : {}".format(contact.statusMessage)
                                    result += "\n❂🇮🇩➢ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                    result += "\n❂🇮🇩➢ Cover : {}".format(str(cover))
                                    result += "\n❂🇮🇩➢ Finish 🎊"
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                    client.sendMention(to, result, [contact.mid])
                                except Exception as error:
                                    logError(error)

                        elif cmd.startswith("delfriendmid "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                client.deleteContact(txt)
                                sendTextTemplate(to, "Done Boskuh",txt)

                        elif cmd.startswith("delfriend "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.deleteContact(ls)
                                        sendTextTemplate(to, "Udah Boss Ku")

                        elif cmd.startswith("addfavorite "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.addFavorite(ls)
                                        client.sendReplyMention(msg_id, to, "Succesfully add @! to Favorite Friend", [ls])

                        elif cmd.startswith("rename "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.renameContact(ls,sep[1])
                                        client.sendReplyMention(msg_id, to, "Succesfully change @! display name to {}".format(sep[1]), [ls])

                        elif cmd == "blocklist":
                              if msg._from in admin:
                                blockeds = client.getBlockedContactIds()
                                num = 0
                                result = "❂🇮🇩➢ List Blocked 🎉"
                                for listBlocked in blockeds:
                                    contact = client.getContact(listBlocked)
                                    num += 1
                                    result += "\n\n❂🇮🇩➢ {}. {}".format(num, contact.displayName)
                                result += "\n\n❂🇮🇩➢ Total {} Blocked".format(len(blockeds))
                                sendTextTemplate(to, result)

                        elif cmd.startswith("changegroupname: "):
                              if msg._from in admin:
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    groupname = text.replace(sep[0] + " ","")
                                    if len(groupname) <= 100:
                                        group = client.getGroup(to)
                                        group.name = groupname
                                        client.updateGroup(group)
                                        sendTextTemplate(to, "Berhasil mengubah nama group menjadi :\n{}".format(groupname))

                        elif cmd == "grouppicture":
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    data = {
                                            "type": "flex",
                                            "altText": "ZHR,BOTS",
                                            "contents": {
  "type": "bubble",
  "styles": {
    "body": {
      "backgroundColor": "#0000A0"
    },
    "footer": {
      "backgroundColor": "#808080"
    },
    "header": {
      "backgroundColor": "#808080"
    }
  },  
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#ff0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                  "uri": "https://line.me/ti/p/~maul-703"
              }
          }]
      }]
  },
  "hero": {
    "aspectMode": "cover",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(client.getGroup(to).pictureStatus),
    "size": "full",
    "align": "center",
  },
  "header": {
    "type": "box",   
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "☑ ʄσtσ ℘гσʄıɭε ɢгσน℘ ☑",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center"
      }
    ]
  }
}
}
                                    client.postTemplate(to, data)

                        elif cmd == "all mid":
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    num = 0
                                    ret_ = "".format(group.name)
                                    for contact in group.members:
                                        num += 1
                                        ret_ += "\n🎲🇮🇩 {}.{}\n╠❂➢{}".format(num, contact.displayName, contact.mid)
                                    people = "\n🔔 TOTAL {} MID 🔔".format(len(group.members))
                                    people1 = "🇮🇩 MID ANGGOTA GROUP 🇮🇩"
                                    sendTextTemplate7(to, str(ret_), people, people1)

                        elif cmd == "pendinglist":
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = ""
                                    no = 0
                                    if group.invitee is None or group.invitee == []:
                                        return sendTextTemplate(to, "Tidak ada pendingan")
                                    else:
                                        for pending in group.invitee:
                                            no += 1
                                            ret_ += "\n👹🇮🇩➢ {}. {}".format(str(no), str(pending.displayName))
                                        people= "\n👻🇮🇩TOTAL {} PENDINGAN🇮🇩👻".format(str(len(group.invitee)))
                                        people1 = "👾🇮🇩 DAFTAR PENDINGAN 🇮🇩👾"
                                        sendTextTemplate7(to, str(ret_), people, people1)

                        elif cmd.startswith("leavegc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    client.leaveGroup(group.id)
                                    sendTextTemplate(to, "Succesfully leave to Group:\n{}".format(group.name))
                                except Exception as error:
                                    logError(error)

                        elif cmd.startswith("sendcrashtogc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    client.sendContact(group.id, "u73629292,'")
                                    sendTextTemplate(to, "Succesfully send Crash to Group:\n {}".format(group.name))
                                except Exception as error:
                                    logError(error)

                        elif cmd.startswith("invitetogc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    client.inviteIntoGroup(group.id, [sender])
                                    client.sendMention(to, "Succesfully invite @! to Group {}".format(group.name), [sender])
                                except Exception as error:
                                    logError(error)

                        elif cmd.startswith("mutebotingc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    if group not in offbot:
                                      sendTextTemplate(to, "\nBerhasil Mure Bot Di Group {}".format(group.name))
                                      offbot.append(group.id)
                                      print(group.id)
                                    else:
                                      sendTextTemplate(to, "Failed Mute Bot In Group\n{}".format(group.name))
                                except Exception as error:
                                    logError(error)

                        elif cmd.startswith("unmutebotingc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                listGroup = groups[int(query)-1]
                                group = client.getGroup(listGroup)
                                if group.id in offbot:
                                    offbot.remove(group.id)
                                    sendTextTemplate(to, "Berhasil Unmute Bot Di Group\n{}".format(group.name))
                                    print(group.id)
                                else:
                                    sendTextTemplate(to, "Failed Unmute Bot In Group\n{}".format(group.name))

                        elif cmd.startswith("chattofr"):
                              if msg._from in admin:
                                dan = text.split("-")
                                frs = client.getAllContactIds()
                                try:
                                    listFriend = frs[int(dan[1])-1]
                                    friend = client.getContact(listFriend)
                                    sendTextTemplate(to, friend.mid, dan[2])
                                except:
                                    pass

                        elif cmd.startswith("sendgifttogc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                    client.sendGift(group.id, random.choice(gf), "theme")
                                    txt = "~Gift~"
                                    client.sendMentionWithFooter(to, txt, "Succesfully send gift to Group {} :)".format(group.name), [sender])
                                except:
                                    pass

                        elif cmd == "cekme":
                              client.sendMessage(to, "waiting...")
                              if sender in admin:
                                contact = client.getContact(sender)
                                cover = client.getProfileCoverURL(sender)
                                result = "╔══[ 🔊Check Profile🔊 ]"
                                result += "\n╠❂➢ Name :".format(str(contact.displayName))
                                result += "\n╠❂➢ Mid : {}".format(contact.mid)
                                result += "\n╠❂➢ Status Profile"
                                result += "\n╠❂➢ Whitelist : False"
                                result += "\n╠❂➢ Blacklist : True"
                                result += "\n╚══[ 💠🇮🇩 FINISH 🇮🇩💠 ]"
                                sendTextTemplate(to, result)
                              elif sender in settings["blackList"]:
                                contact = client.getContact(sender)
                                cover = client.getProfileCoverURL(sender)
                                result = "╔══[ 🔊Check Profile🔊 ]"
                                result += "\n╠❂➢ Name :".format(str(contact.displayName))
                                result += "\n╠❂➢ Mid : {}".format(contact.mid)
                                result += "\n╠❂➢ Status Profile"
                                result += "\n╠❂➢ Whitelist : False"
                                result += "\n╠❂➢ Blacklist : True"
                                result += "\n╚══[ 💠🇮🇩 FINISH 🇮🇩💠 ]"
                                sendTextTemplate(to, result)
                              else:
                                contact = client.getContact(sender)
                                cover = client.getProfileCoverURL(sender)
                                result = "╔══[ 🔊Check Profile🔊 ]"
                                result += "\n╠❂➢ Name :".format(str(contact.displayName))
                                result += "\n╠❂➢ Mid : {}".format(contact.mid)
                                result += "\n╠❂➢ Status Profile"
                                result += "\n╠❂➢ Whitelist : False"
                                result += "\n╠❂➢ Blacklist : True"
                                result += "\n├≽ Blacklist : False"
                                result += "\n╚══[ 💠🇮🇩 FINISH 🇮🇩💠 ]"
                                sendTextTemplate(to, result)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = client.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(client.getGroup(to).pictureStatus),
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#808080"
        },
        "header": {
          "backgroundColor": "#808080"
        }
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xxs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☑ ℘гσʄıɭε ɢгσน℘ ☑",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(G.creator.pictureStatus),
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#808080"
        },
        "header": {
          "backgroundColor": "#808080"
        }
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{

              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xxs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☑ ℘гσʄıɭε ɕгεศtσг ɢгσน℘ ☑",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center"            
          }
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#808080"
        },
        "header": {
          "backgroundColor": "#808080"
        }
      },
      "type": "bubble",
      "size": "micro",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(G.name),
                    "size": "xxs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#00ff00"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "☑ MID GROUP ☑\n{}".format(G.id)+ "\n\n☑ WAKTU DIBUAT ☑\n{}".format(str(timeCreated)),
                    "size": "xxs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#00ff00"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "\n☑ Jumlah Member ☑ {}".format(str(len(G.members)))+ "\n☑ Jumlah Pending ☑ {}".format(gPending)+ "\n☑ Group Qr ☑ {}".format(gQr)+ "\n☑ Group Ticket ☑ {}".format(gTicket),
                    "size": "xxs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#ffffff",
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xxs",
                  "action": {
                      "type": "uri",
                      "label": "☑ CƦᴇᴀᴛᴏƦ ☑",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☑ รtศtนร ℘гσʄıɭε ɢгσน℘ ☑",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center"            
          }
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#0000A0"
        },
        "footer": {
          "backgroundColor": "#808080"
        },
        "header": {
          "backgroundColor": "#808080"
        }
      },
      "type": "bubble",
      "size": "micro",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(G.creator.displayName),
                    "size": "xxs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#00ff00"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "☑ MID CREATOR GROUP ☑\n{}".format(G.creator.mid)+ "\n\n☑ STATUS PROFILE CREATOR GROUP ☑",
                    "size": "xxs",
                    "weight": "bold",
                    "color": "#ffffff",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#00ff00"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(G.creator.statusMessage),
                    "size": "xxs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xxs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#ff0000",
                  "height": "xxs",
                  "action": {
                      "type": "uri",
                      "label": "☄1�7 CƦᴇᴀᴛᴏƦ ☄1�7",
                      "uri": "https://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "☄1�7 รtศtนร ɕгεศtσг ɢгσน℘ ☄1�7",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)

                            except Exception as e:
                                sendTextTemplate(msg.to, str(e))

                        elif cmd.startswith("groupvideocall "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                num = int(txt)
                                sendTextTemplate(to, "Berhasil Invite Ke Dalam VideoCall Group")
                                for anu in range(0,num):
                                    group = client.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    client.inviteIntoGroupVideoCall(to, contactIds=members)

                        elif cmd in ('nikung','mpus','zahra','tag'):
                              if msg._from in admin:
                                group = client.getGroup(msg.to);nama = [contact.mid for contact in group.members];nama.remove(client.getProfile().mid)
                                client.datamention(msg.to,'🚥 mention 🚥',nama)

#==================BAGIAN UPDATING PROFILE===========================================
                        elif cmd == "changepict":
                              if msg._from in admin:
                                settings["changePictureProfile"] = True
                                sendTextTemplate(to, "❂🇮🇩➢ Kirim Fotonya Bos Ku")

                        elif cmd == "changecover":
                              if sender in admin:
                                settings["changeCover"] = True
                                sendTextTemplate(to, "❂🇮🇩➢ Kirim Fotonya Bos Ku")

                        elif cmd == "changevp":
                              if msg._from in admin:
                                settings["changeVpProfile"] = True
                                sendTextTemplate(to, "❂🇮🇩➢ Kirim Fotonya Bos Ku")

                        elif cmd == "changegrouppicture":
                              if msg._from in admin:
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    sendTextTemplate(to, "❂🇮🇩➢ Kirim Fotonya Bos Ku")

                        elif cmd == "changedual":
                              if msg._from in admin:
                                settings["changeDual"] = True
                                sendTextTemplate(to, "❂🇮🇩➢ Kirim VideoNya Boss Ku")

#===================BAGIAN SETTINGAN==============================================
                        elif cmd.startswith("setpesan: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoAddMessage"] = txt
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil mengubah pesan\n❂🇮🇩➢ Auto add menjadi :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                    sendTextTemplate(to, "❂🇮🇩➢ Gagal mengubah pesan auto add")

                        elif cmd.startswith("setrespon1: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoResponMessage"] = txt
                                    sendTextTemplate(to, "❂🇮🇩➢ Success Update\n❂🇮🇩➢ Auto Respon1 Menjadi :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                   sendTextTemplate(to, "❂🇮🇩➢ Auto Respon1 Gagal Di Rubah")

                        elif cmd.startswith("setrespon2: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoResMessage"] = txt
                                    sendTextTemplate(to, "❂🇮🇩➢ Success Update\n❂🇮🇩➢ Auto Respon2 Menjadi :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                   sendTextTemplate(to, "❂🇮🇩➢ Auto Respon2 Gagal Di Rubah")

                        elif cmd.startswith("setrespon3: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoRespekMessage"] = txt
                                    sendTextTemplate(to, "❂🇮🇩➢ Success Update\n❂🇮🇩➢ Auto Respon3 Menjadi :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                   sendTextTemplate(to, "❂🇮🇩➢ Auto Respon3 Gagal Di Rubah")


                        elif cmd.startswith("setautojoin: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoJoinMessage"] = txt
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil mengubah pesan\n❂🇮🇩➢ auto join menjadi :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                    sendTextTemplate(to, "❂🇮🇩➢ Gagal mengubah pesan auto join")

                        elif cmd.startswith("setautoleave: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoLeaveMessage"] = txt
                                    sendTextTemplate(to, "❂🇮🇩➢ Berhasil mengubah pesan\n❂🇮🇩➢ auto leave menjadi :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                    sendTextTemplate(to, "❂🇮🇩➢ Gagal mengubah pesan auto leave")

                        elif cmd.startswith("setcomment: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["commentPost"] = txt
                                    sendTextTemplate(to, "❂🇮🇩➢ Succes Mengubah Pesan\n❂🇮🇩➢ CommentTimeLine :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                    sendTextTemplate(to, "❂🇮🇩➢ Failed")

                        elif cmd.startswith("setwelcome: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["welcome"] = txt
                                    sendTextTemplate(to, "❂🇮🇩➢ Success Update\n❄1�7?🇩➄1�7 Welcome Menjadi :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                   sendTextTemplate(to, "❂🇮🇩➢ Welcome Gagal Di Rubah")

                        elif cmd.startswith("setleave: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["leave"] = txt
                                    sendTextTemplate(to, "❂🇮🇩➢ Success Update\n❂🇮🇩➢ Leave Menjadi :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                   sendTextTemplate(to, "❂🇮🇩➢ Leave Gagal Di Rubah")

                        elif cmd.startswith("setsider: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["sider"] = txt
                                    sendTextTemplate(to, "❂🇄1�7??➄1�7 Success Update\n❂🇮🇩➢ Sider Menjadi :\n❂🇮🇩➢ {}".format(txt))
                                except:
                                   sendTextTemplate(to, "❂🇮🇩➢ Sider Gagal Di Rubah")

                        elif cmd.startswith("addsettings to "):
                              if sender in admin:
                                txt = removeCmd("addsettings to", text)
                                settings["{}".format(txt)] = []
                                f=codecs.open('setting.json','w','utf-8')
                                json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                client.sendReplyMessage(msg_id, to, "Succesfully add {} to settings".format(txt))

                        elif cmd.startswith("addsettings "):
                              if sender in admin:
                              	txt = removeCmd("addsettings", text)
                              	settings["{}".format(txt)] = False
                              	f=codecs.open('setting.json','w','utf-8')
                              	json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                              	client.sendReplyMessage(msg_id, to, "Succesfully add {} to settings".format(txt))

                        elif cmd.startswith("delsettings "):
                              if sender in admin:
                              	txt = removeCmd("delsettings", text)
                              	del settings["{}".format(txt)]
                              	client.sendReplyMessage(msg_id, to, "Succesfully del {} in settings".format(txt))

#====================BAGIAN PENGECEKAN=================================================
                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Pesan Message mu :\n\n ❂🇮🇩➢" + str(settings["autoAddMessage"]))

                        elif text.lower() == "cek respon1":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Respon1 Message mu :\n\n ❂🇮🇩➢" + str(settings["autoResponMessage"]))

                        elif text.lower() == "cek respon2":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Respon2 Message mu :\n\n ❂🇮🇩➢" + str(settings["autoResMessage"]))

                        elif text.lower() == "cek respon3":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Respon3 Message mu :\n\n ❂🇮🇩➢" + str(settings["autoRespekMessage"]))

                        elif text.lower() == "cek autojoin":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Autojoin Message mu :\n\n ❂🇮🇩➢" + str(settings["autoJoinMessage"]))

                        elif text.lower() == "cek autoleave":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Autoleave Message mu :\n\n ❂🇮🇩➢" + str(settings["autoLeaveMessage"]))

                        elif text.lower() == "cek coment timeline":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Comen TL Message mu :\n\n ❂🇮🇩➢" + str(settings["commentPost"]))

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Welcome Message mu :\n\n ❂🇮🇩➢" + str(settings["welcome"]))

                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Leave Message mu :\n\n ❂🇮🇩➢" + str(settings["leave"]))

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate(to, "❂🇮🇩➢ Sider Message mu :\n\n ❂🇮🇩➢" + str(settings["sider"]))

#=======================BAGIAN REMOT CONTROL===============================================
                        if cmd == "unsend on":
                            if msg._from in admin:
                                settings["unsend"] = True
                                sendTextTemplate(to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                settings["unsend"] = False
                                sendTextTemplate(to, "Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "autojoin on":
                            if msg._from in admin:
                                if settings["autoJoin"] == True:
                                    sendTextTemplate(to, "Auto join telah aktif")
                                else:
                                    settings["autoJoin"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto join")

                        elif cmd == "autojoin off":
                            if msg._from in admin:
                                if settings["autoJoin"] == False:
                                    sendTextTemplate(to, "Auto join telah nonaktif")
                                else:
                                    settings["autoJoin"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto join")                                

                        elif cmd == "autoblock on":
                            if msg._from in admin:
                                if settings["autoAdd"] == True:
                                    sendTextTemplate(to, "Autoblock allready on")
                                else:
                                    settings["AutoBlock"] = True
                                    sendTextTemplate(to, "Autoblock allready on")

                        elif cmd == "autoblock off":
                            if msg._from in admin:
                                if settings["autoAdd"] == False:
                                    sendTextTemplate(to, "Autoblock allready off")
                                else:
                                    settings["AutoBlock"] = False
                                    sendTextTemplate(to, "Autoblock allready off")

                        elif cmd == "autoleave on":
                            if msg._from in admin:
                                if settings["autoLeave"] == True:
                                    sendTextTemplate(to, "Auto Leave telah aktif")
                                else:
                                    settings["autoJoin"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto Leave")

                        elif cmd == "autoleave off":
                            if msg._from in admin:
                                if settings["autoLeave"] == False:
                                    sendTextTemplate(to, "Auto Leave telah nonaktif")
                                else:
                                    settings["autoLeave"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto Leave")

                        elif cmd == "autojointicket on":
                            if msg._from in admin:
                                if settings["autoJoinTicket"] == True:
                                    sendTextTemplate(to, "Auto join ticket telah aktif")
                                else:
                                    settings["autoJoinTicket"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto join ticket")

                        elif cmd == "autojointicket off":
                            if msg._from in admin:
                                if settings["autoJoinTicket"] == False:
                                    sendTextTemplate(to, "Auto join ticket telah nonaktif")
                                else:
                                    settings["autoJoinTicket"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto join ticket")

                        elif cmd == "autoread on":
                            if msg._from in admin:
                                if settings["autoRead"] == True:
                                    sendTextTemplate(to, "Auto read telah aktif")
                                else:
                                    settings["autoRead"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto read")

                        elif cmd == "autoread off":
                            if msg._from in admin:
                                if settings["autoRead"] == False:
                                    sendTextTemplate(to, "Auto read telah nonaktif")
                                else:
                                    settings["autoRead"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto read")

                        elif cmd == "autoadd on":
                            if msg._from in admin:
                                if settings["autoAdd"] == True:
                                    sendTextTemplate(to, "Auto Add telah aktif")
                                else:
                                    settings["autoAdd"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto Add")

                        elif cmd == "autoadd off":
                            if msg._from in admin:
                                if settings["autoAdd"] == False:
                                    sendTextTemplate(to, "Auto add telah nonaktif")
                                else:
                                    settings["autoAdd"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto Add")

                        elif cmd == "respon1 on":
                            if msg._from in admin:
                                if settings["autoRespon"] == True:
                                    sendTextTemplate(to, "Auto respon telah aktif")
                                else:
                                    settings["autoRespon"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto respon")

                        elif cmd == "respon1 off":
                            if msg._from in admin:
                                if settings["autoRespon"] == False:
                                    sendTextTemplate(to, "Auto respon telah nonaktif")
                                else:
                                    settings["autoRespon"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto respon")

                        elif cmd == "respon on":
                            if msg._from in admin:
                                if settings["autoRes"] == True:
                                    sendTextTemplate(to, "Auto respon2 telah aktif")
                                    data = {"type": "text","text": "{}".format(am),"sentBy": {"label": "Zhr.𝐛𝐨𝐭𝐥𝐢𝐧𝐞", "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u6e4534dd63e82642f29205d2c993c642"}}
                                    sendTemplate(to,data)
                                else:
                                    settings["autoRes"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto respon")

                        elif cmd == "respon off":
                            if msg._from in admin:
                                if settings["autoRes"] == False:
                                    sendTextTemplate(to, "Auto respon2 telah nonaktif")
                                else:
                                    settings["autoRes"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto respon2")

                        elif cmd == "respon3 on":
                            if msg._from in admin:
                                if settings["autoRespek"] == True:
                                    sendTextTemplate(to, "Auto respon3 Mode PM telah aktif")
                                else:
                                    settings["autoRespek"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto respon3\nMode PM")

                        elif cmd == "respon3 off":
                            if msg._from in admin:
                                if settings["autoRespek"] == False:
                                    sendTextTemplate(to, "Auto respon3 Mode PM telah nonaktif")
                                else:
                                    settings["autoRespek"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto respon3\nMode PM")

                        elif cmd == "autoreply on":
                            if msg._from in admin:
                                if settings["autoReply"] == True:
                                    sendTextTemplate(to, "Auto Reply telah aktif")
                                else:
                                    settings["autoReply"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto reply")

                        elif cmd == "autoreply off":
                            if msg._from in admin:
                                if settings["autoReply"] == False:
                                    sendTextTemplate(to, "Auto Reply telah nonaktif")
                                else:
                                    settings["autoReply"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto Reply")

                        elif cmd == "contact on":
                            if msg._from in admin:
                                if settings["checkContact"] == True:
                                    sendTextTemplate(to, "Check details contact telah aktif")
                                else:
                                    settings["checkContact"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan check details contact")

                        elif cmd == "contact off":
                            if msg._from in admin:                          
                                if settings["checkContact"] == False:
                                    sendTextTemplate(to, "Check details contact telah nonaktif")
                                else:
                                    settings["checkContact"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan Check details contact")

                        elif cmd == "post on":
                            if msg._from in admin:                          
                                if settings["checkPost"] == True:
                                    sendTextTemplate(to, "Check details post telah aktif")
                                else:
                                    settings["checkPost"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan check details post")

                        elif cmd == "post off":
                            if msg._from in admin:                          
                                if settings["checkPost"] == False:
                                    sendTextTemplate(to, "Check details post telah nonaktif")
                                else:
                                    settings["checkPost"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan check details post")

                        elif cmd == "checksticker on":
                            if msg._from in admin:
                                if settings["checkSticker"] == True:
                                    sendTextTemplate(to, "Check details sticker telah aktif")
                                else:
                                    settings["checkSticker"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan check details sticker")

                        elif cmd == "checksticker off":
                            if msg._from in admin:                          
                                if settings["checkSticker"] == False:
                                    sendTextTemplate(to, "Check details sticker telah nonaktif")
                                else:
                                    settings["checkSticker"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan check details sticker")

                        elif cmd == "sticker on":
                            if msg._from in admin:                          
                                if to in settings["sticker"]:
                                    sendTextTemplate(to, "Sticker telah aktif")
                                else:
                                    if to not in settings["sticker"]:
                                        settings["sticker"].append(to)
                                    sendTextTemplate(to, "Berhasil mengaktifkan sticker")

                        elif cmd == "sticker off":
                            if msg._from in admin:                          
                                if to not in settings["sticker"]:
                                    sendTextTemplate(to, "Sticker telah nonaktif")
                                else:
                                    if to in settings["sticker"]:
                                        settings["sticker"].remove(to)
                                    sendTextTemplate(to, "Berhasil menonaktifkan sticker")

                        elif cmd == "deletefriend on":
                            if msg._from in admin:                          
                                if settings["delFriend"] == True:
                                    sendTextTemplate(to, "Send Contact !!!!")
                                else:
                                    settings["delFriend"] = True
                                    sendTextTemplate(to, "Send Contact :)")

                        elif cmd == "deletefriend off":
                            if msg._from in admin:                          
                                if settings["delFriend"] == False:
                                    sendTextTemplate(to, "Udah Ga aktif !!!")
                                else:
                                    settings["delFriend"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan delete friend")

                        elif cmd == "autokick on":
                            if msg._from in owner or admin:                          
                                if protectGroup[to]["autoKick"] == True:
                                    sendTextTemplate(to, "Auto Kick telah aktif")
                                else:
                                    protectGroup[to]["autoKick"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan Auto Kick")

                        elif cmd == "autokick off":
                            if msg._from in owner or admin:                          
                                if protectGroup[to]["autoKick"] == False:
                                    sendTextTemplate(to, "Auto Kick telah nonaktif")
                                else:
                                    protectGroup[to]["autoKick"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto Kick")

                        elif cmd == "welcome on":
                            if msg._from in admin:
                                if settings["welcome"] == True:
                                    sendTextTemplate(to, "Auto join telah aktif")
                                else:
                                    settings["welcome"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto join")

                        elif cmd == "welcome off":
                            if msg._from in admin:
                                if settings["welcome"] == False:
                                    sendTextTemplate(to, "Auto join telah nonaktif")
                                else:
                                    settings["welcome"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto join")

                        elif cmd == "sider on":
                            if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate2(to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                            if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate2(to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendTextTemplate2(to, "Sudak tidak aktif")

                        elif cmd == "lurking on":
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to in read['readPoint']:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    sendTextTemplate(to, "Lurking telah diaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    sendTextTemplate(to, "Set reading point : \n{}".format(readTime))

                        elif cmd == "lurking off":
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to not in read['readPoint']:
                                    sendTextTemplate(to,"Lurking telah dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    sendTextTemplate(to, "Delete reading point : \n{}".format(readTime))

                        elif "lurking" in msg.text.lower():
                            if msg._from in admin:
                                if to in read['readPoint']:
                                    if read["readMember"][to] == []:
                                        return client.sendMessage(to, "Tidak Ada Sider")
                                    else:
                                        no = 0
                                        result = "╔══[ Reader ]"
                                        for dataRead in read["readMember"][to]:
                                            no += 1
                                            result += "\n├≽ {}. @!".format(str(no))
                                        result += "\n╚══[ Total {} Sider ]".format(str(len(read["readMember"][to])))
                                        sendTextTemplate(to, result, read["readMember"][to])
                                        read['readMember'][to] = []

                        elif cmd == "clonecontact":
                            if msg._from in admin:
                                settings["cloneContact"] = True
                                sendTextTemplate(to, "Kirim Contactnya Boss Ku")

                        elif cmd == "clone contact off":
                            if msg._from in admin:
                                if settings["cloneContact"] == False:
                                    sendTextTemplate(to, "Clone Contact Has been Aborted")
                                else:
                                    settings["cloneContact"] = False
                                    sendTextTemplate(to, "Succesfully Aborted \n\nClone Contact Profile")

                        elif cmd == "allcvp on":
                            if msg._from in admin:
                                if settings["allchangedual"] == True:
                                    sendTextTemplate(to, "ALLCVP Active")
                                else:
                                    settings["allchangedual"] = True
                                    sendTextTemplate(to, "ALLCVP succses Active \n\nChange Video & Picture")

                        elif cmd == "allcvp off":
                            if msg._from in admin:
                                if settings["allchangedual"] == False:
                                    sendTextTemplate(to, "CVP Has Been Aborted")
                                else:
                                    settings["allchangedual"] = False
                                    sendTextTemplate(to, "Succesfully Aborted \n\nChange Video & Picture")

                        elif cmd == "cvp on":
                            if msg._from in admin:
                                if settings["changeDual"] == True:
                                    sendTextTemplate(to, "CVP Active")
                                else:
                                    settings["changeDual"] = False
                                    sendTextTemplate(to, "CVP Succes Active \n\nChange Video & Picture")

                        elif cmd == "cvp off":
                            if msg._from in admin:
                                if settings["changeDual"] == False:
                                    sendTextTemplate(to, "CVP Has Been Aborted")
                                else:
                                    settings["changeDual"] = False
                                    sendTextTemplate(to, "Succesfully Aborted \n\nChange Video & Picture")

                        elif cmd == "mimic on":
                            if msg._from in admin:
                                if settings["mimic"]["status"] == True:
                                    sendTextTemplate(to, "Mimic telah aktif")
                                else:
                                    settings["mimic"]["status"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan mimic")

                        elif cmd == "mimic off":
                            if msg._from in admin:
                                if settings["mimic"]["status"] == False:
                                    sendTextTemplate(to, "mimic telah nonaktif")
                                else:
                                    settings["mimic"]["status"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan mimic") 

                        elif 'Antijs ' in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace('Antijs ','')
                                if spl == 'on':
                                    if msg.to in protectantijs:
                                         msgs = "❂🇮🇩➢ Protectantijs di aktifkan"
                                    else:
                                         protectantijs.append(msg.to)
                                         ginfo = client.getGroup(msg.to)
                                         msgs = ""
                                    sendTextTemplate(to, "❂🇮🇩➢ Protectantijs Telah Active")
                                elif spl == 'off':
                                      if msg.to in protectantijs:
                                           protectantijs.remove(msg.to)
                                           ginfo = client.getGroup(msg.to)
                                           msgs = "❂🇮🇩➢ Protectantijs non aktif"
                                      else:
                                           msgs = ""
                                      sendTextTemplate(to, "❂🇮🇩➢ Protectantijs Telah Nonactive")

#=======================BAGIAN STAY RESPON ANTI-JS===========================================
                        elif cmd == "gjoin":
                            if msg._from in admin:
                                G = client.getGroup(msg.to)
                                ginfo = client.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                client.updateGroup(G)
                                invsend = 0
                                Ticket = client.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "gout":
                            if msg._from in admin:
                                G = client.getGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "stay":
                            if msg._from in admin:
                                try:
                                    ginfo = client.getGroup(to)
                                    client.inviteIntoGroup(to, [Zmid])
                                    sendTextTemplate(to,"❂➢ Grup :\n❂➢ "+str(ginfo.name)+"\n❂➢ Aman Dari JS")
                                except:
                                    pass
#=======================MEDIA BAGIAN YOUTUBE================================================

                        elif cmd.startswith("youtube "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                            "type": "bubble",
                                            "styles": {
                                                "header": {
                                                    "backgroundColor": "#808080"
                                                },
                                                "body": {
                                                   "backgroundColor": "#0000A0",
                                                   "separator": True,
                                                   "separatorColor": "#0000CC"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#808080",
                                                    "separator": True,
                                                   "separatorColor": "#0000CC"
                                               }
                                            },
                                            "header": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [  
                                                   {
                                                        "type": "text",
                                                        "text": "🚥 ZHR FAMILY BOTS 🚥",
                                                        "weight": "bold",
                                                        "color": "#FF0000",
                                                        "size": "xl",
                                                        "align": "center"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                "size": "full",
                                                "aspectRatio": "2:3",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://nv/profilePopup/mid=u67ae64c90c91af8d20d8edbef8281dd5"
                                                }
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "image",
                                                        "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                        "aspectMode": "cover",
                                                        "gravity": "bottom",
                                                        "size": "sm",
                                                        "aspectRatio": "1:1",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                        }
                                                    }]
                                                }, {
                                                    "type": "separator",
                                                    "color": "#00FF00"
                                                }, {
                                                    "type": "box",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "🚥 Judul vidio 🚥",
                                                        "color": "#FF0000",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#00ff00"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#aaaaaa",
                                                        "size": "sm",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 2,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 2,
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "🚥 YOUTUBE 🚥",
                                                            "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                    }, {
                                                        "flex": 3,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#ff0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "🚥 Mp3 🚥",
                                                            "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Ytdl%20{}".format(str(music['id']['videoId']))
                                                        }
                                                    }]
                                                }, {
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#FF0000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "🚥 Mp4 🚥",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        client.postTemplate(to, data)

                        elif cmd.startswith("food "):
                            if msg._from in admin:
                                query = removeCmd("food", text)
                                cond = query.split(" ")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []                                	
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "I'm hungry",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        client.postTemplate(to, data)

                        elif cmd.startswith("searchapp "):
                            if msg._from in admin:
                                query = removeCmd("searchapp", text)
                                cond = query.split(" ")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        client.postTemplate(to, data)

                        elif cmd.startswith("idsmule "):
                                sep = text.split(" ")
                                nama = text.replace(sep[0] + " ","")    
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("https://www.smule.com/{}".format(urllib.parse.quote(nama)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    try:
                                        for anu in soup.findAll('script', attrs={'type':'text/javascript'})[1]:
                                            a = anu.replace('DataStore.Pages.Profile =','')
                                            b = a.replace(';','')
                                            get = json.loads(b)
                                            pict = get['user']['pic_url']
                                            ret_ = "🎶➢Account ID: "+str(get['user']['account_id'])
                                            ret_ += "\n🎶➢ ᴜsᴇʀ ɴᴀᴍᴇ: "+str(get['user']['handle'])
                                            ret_ += "\n🎶➢ ƒσℓℓσωєrs: "+str(get['user']['followers'])
                                            ret_ += "\n🎶➢ ƒσℓℓσω: "+str(get['user']['followees'])
                                            ret_ += "\n🎶➢ ρєrƒσrмαทcєs: "+str(get['user']['num_performances'])
                                            ret_ += "\n🎶➢ ᴠɪᴘ sᴛᴀᴛᴜs: "+str(get['user']['is_vip'])
                                            ret_ += "\n🎶➢ Description:\n❂🇮🇩➢ "+str(get['user']['blurb'])
                                        data = {
                                                "type": "flex",
                                                "altText": "SMULE ID",
                                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "🚥 STATUS SMULE 🚥 :", 
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#FF0000"
          },
          {
            "type": "separator",
            "color": "#aaaaaa"
          },
          {
            "type": "text",
            "text": ret_,
            "size": "sm",
            "weight": "bold",
            "color": "#00FF00",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#0000A0"
    },
    "footer": {
      "backgroundColor": "#808080"
    },
    "header": {
      "backgroundColor": "#808080"
    }
  },  
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#ff0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "🚥 creator 🚥",
                  "uri": "https://line.me/ti/p/~maul-703"
              }
          }]
      }]
  },
  "hero": {
    "aspectMode": "cover",
    "aspectRatio": "2:3",
    "type": "image",
    "url": pict,
    "size": "full",
    "align": "center",
  },
  "header": {
    "type": "box",   
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "🚥 ZHR FAMILY BOTS 🚥",
        "size": "sm",
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center"
      }
    ]
  }
}
}
                                        client.postTemplate(to, data)
                                    except:
                                        client.sendMessage(msg.to, "User tidak ditemukan!")


                        elif cmd.startswith("nadaquranmp3 "):
                            try:
                                sep = msg.text.split(" ")
                                surah = int(text.replace(sep[0] + " ",""))
                                if 0 < surah < 115:
                                    if surah not in [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 17, 18, 20, 21, 23, 26, 37]:
                                        if len(str(surah)) == 1:
                                            audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(surah) + "-muslimcentral.com.mp3"
                                            client.sendAudioWithURL(to, audionya)
                                        elif len(str(surah)) == 2:
                                            audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(surah) + "-muslimcentral.com.mp3"
                                            client.sendAudioWithURL(to, audionya)
                                        else:
                                            audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(surah) + "-muslimcentral.com.mp3"
                                            client.sendAudioWithURL(to, audionya)
                                    else:
                                        client.sendMessage(msg.to, "Surah terlalu panjang")
                                else:
                                    client.sendMessage(msg.to, "Quran hanya 114 surah")
                            except Exception as error:
                                client.sendMessage(msg.to, "error\n"+str(error))

                        elif cmd == "quranlist":
                          if msg._from in admin:
                              ret_ = "\n    1. Al-Faatiha"
                              ret_ += "\n    2. Al-Baqara"
                              ret_ += "\n    3. Aal-i-Imraan"
                              ret_ += "\n    4. An-Nisaa"
                              ret_ += "\n    5. Al-Maaida"
                              ret_ += "\n    6. Al-An'aam"
                              ret_ += "\n    7. Al-A'raaf"
                              ret_ += "\n    8. Al-Anfaal"
                              ret_ += "\n    9. At-Tawba"
                              ret_ += "\n  10. Yunus"
                              ret_ += "\n  11. Hud"
                              ret_ += "\n  12. Yusuf"
                              ret_ += "\n  13. Ar-Ra'd"
                              ret_ += "\n  14. Ibrahim"
                              ret_ += "\n  15. Al-Hijr"
                              ret_ += "\n  16. An-Nahl"
                              ret_ += "\n  17. Al-Israa"
                              ret_ += "\n  18. Al-Kahf"
                              ret_ += "\n  19. Maryam"
                              ret_ += "\n  20. Taa-Haa"
                              ret_ += "\n  21. Al-Anbiyaa"
                              ret_ += "\n  22. Al-Hajj"
                              ret_ += "\n  23. Al-Muminoon"
                              ret_ += "\n  24. An-Noor"
                              ret_ += "\n  25. Al-Furqaan"
                              ret_ += "\n  26. Ash-Shu'araa"
                              ret_ += "\n  27. An-Naml"
                              ret_ += "\n  28. Al-Qasas"
                              ret_ += "\n  29. Al-Ankaboot"
                              ret_ += "\n  30. Ar-Room"
                              ret_ += "\n  31. Luqman"
                              ret_ += "\n  32. As-Sajda"
                              ret_ += "\n  33. Al-Ahzaab"
                              ret_ += "\n  34. Saba"
                              ret_ += "\n  35. Faatir"
                              ret_ += "\n  36. Yaseen"
                              ret_ += "\n  37. As-Saaffaat"
                              ret_ += "\n  38. Saad"
                              ret_ += "\n  39. Az-Zumar"
                              ret_ += "\n  40. Ghafir"
                              ret_ += "\n  41. Fussilat"
                              ret_ += "\n  42. Ash-Shura"
                              ret_ += "\n  43. Az-Zukhruf"
                              ret_ += "\n  44. Ad-Dukhaan"
                              ret_ += "\n  45. Al-Jaathiya"
                              ret_ += "\n  46. Al-Ahqaf"
                              ret_ += "\n  47. Muhammad"
                              ret_ += "\n  48. Al-Fath"
                              ret_ += "\n  49. Al-Hujuraat"
                              ret_ += "\n  50. Qaaf"
                              ret_ += "\n  51. Adh-Dhaariyat"
                              ret_ += "\n  52. At-Tur"
                              ret_ += "\n  53. An-Najm"
                              ret_ += "\n  54. Al-Qamar"
                              ret_ += "\n  55. Ar-Rahmaan"
                              ret_ += "\n  56. Al-Waaqia"
                              ret_ += "\n  57. Al-Hadid"
                              ret_ += "\n  58. Al-Mujaadila"
                              ret_ += "\n  59. Al-Hashr"
                              ret_ += "\n  60. Al-Mumtahana"
                              ret_ += "\n  61. As-Saff"
                              ret_ += "\n  62. Al-Jumu'a"
                              ret_ += "\n  63. Al-Munaafiqoon"
                              ret_ += "\n  64. At-Taghaabun"
                              ret_ += "\n  65. At-Talaaq"
                              ret_ += "\n  66. At-Tahrim"
                              ret_ += "\n  67. Al-Mulk"
                              ret_ += "\n  68. Al-Qalam"
                              ret_ += "\n  69. Al-Haaqqa"
                              ret_ += "\n  70. Al-Ma'aarij"
                              ret_ += "\n  71. Nooh"
                              ret_ += "\n  72. Al-Jinn"
                              ret_ += "\n  73. Al-Muzzammil"
                              ret_ += "\n  74. Al-Muddaththir"
                              ret_ += "\n  75. Al-Qiyaama"
                              ret_ += "\n  76. Al-Insaan"
                              ret_ += "\n  77. Al-Mursalaat"
                              ret_ += "\n  78. An-Naba"
                              ret_ += "\n  79. An-Naazi'aat"
                              ret_ += "\n  80. Abasa"
                              ret_ += "\n  81. At-Takwir"
                              ret_ += "\n  82. Al-Infitaar"
                              ret_ += "\n  83. Al-Mutaffifin"
                              ret_ += "\n  84. Al-Inshiqaaq"
                              ret_ += "\n  85. Al-Burooj"
                              ret_ += "\n  86. At-Taariq"
                              ret_ += "\n  87. Al-A'laa"
                              ret_ += "\n  88. Al-Ghaashiya"
                              ret_ += "\n  89. Al-Fajr"
                              ret_ += "\n  90. Al-Balad"
                              ret_ += "\n  91. Ash-Shams"
                              ret_ += "\n  92. Al-Lail"
                              ret_ += "\n  93. Ad-Dhuhaa"
                              ret_ += "\n  94. Ash-Sharh"
                              ret_ += "\n  95. At-Tin"
                              ret_ += "\n  96. Al-Alaq"
                              ret_ += "\n  97. Al-Qadr"
                              ret_ += "\n  98. Al-Bayyina"
                              ret_ += "\n  99. Az-Zalzala"
                              ret_ += "\n100. Al-Aadiyaat"
                              ret_ += "\n101. Al-Qaari'a"
                              ret_ += "\n102. At-Takaathur"
                              ret_ += "\n103. Al-Asr"
                              ret_ += "\n104. Al-Humaza"
                              ret_ += "\n105. Al-Fil"
                              ret_ += "\n106. Quraish"
                              ret_ += "\n107. Al-Maa'un"
                              ret_ += "\n108. Al-Kawthar"
                              ret_ += "\n109. Al-Kaafiroon"
                              ret_ += "\n110. An-Nasr"
                              ret_ += "\n111. Al-Masad"
                              ret_ += "\n112. Al-Ikhlaas"
                              ret_ += "\n113. Al-Falaq"
                              ret_ += "\n114. An-Naas"
                              people1= "📕 LIST AL'QURAN 📕"
                              people= "Silahkan Ketik :\nNadaquranmp3 (no)\n━━━━━━━━━━━━━\nBy:\n👔җ̷̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫э̷̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫в̷̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫э̷̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫я̷̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫ℓ̷̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫ђ̷̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫ý̷̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫и̷̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫̫👔".format(str(settings["keyCommand"]))
                              sendTextTemplate7(msg.to, str(ret_), people, people1)

#===================BAGIAN TOKEN =====================================================
                        if cmd == "ᴛᴏᴋᴇɴ ᴅᴇsᴋᴛᴏᴘᴍᴀᴄ":
                                ryn = DESKTOPMAC()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "ᴛᴏᴋᴇɴ ᴅᴇsᴋᴛᴏᴘᴡɪɴ":
                                ryn = DESKTOPWIN()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "ᴛᴏᴋᴇɴ ɪᴏsɪᴘᴀᴅ":
                                ryn = IOSIPAD()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "ᴛᴏᴋᴇɴ ᴄʜʀᴏᴍᴇᴏs":
                                ryn = CHROMEOS()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "ᴛᴏᴋᴇɴ ᴡɪɴ10":
                                ryn = WIN10()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "ᴛᴏᴋᴇɴ ᴀɴᴅʀᴏɪᴅ":
                                ryn = ANDROID()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()

                        if cmd == "mytoken":
                          lists = {"result": [{"name": "ᴛᴏᴋᴇɴ ᴅᴇsᴋᴛᴏᴘᴡɪɴ",},{"name": "ᴛᴏᴋᴇɴ ᴄʜʀᴏᴍᴇᴏs",},{"name": "ᴛᴏᴋᴇɴ ɪᴏsɪᴘᴀᴅ",},{"name": "ᴛᴏᴋᴇɴ ᴅᴇsᴋᴛᴏᴘᴍᴀᴄ",},{"name": "ᴛᴏᴋᴇɴ ᴡɪɴ10",},{"name": "ᴛᴏᴋᴇɴ ᴀɴᴅʀᴏɪᴅ",}]}
                          if lists["result"] != []:
                                  ret_ = []
                                  for fn in lists["result"]:
                                          if len(ret_) >= 20:
                                              pass
                                          else:
                                             ret_.append({
                                            "type": "bubble",
                                            "styles": {
                                                "header": {
                                                    "backgroundColor": "#000000"
                                                },
                                                "body": {
                                                   "backgroundColor": "#000000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#000000",
                                                    "separator": True,
                                                   "separatorColor": "#000000"
                                               }
                                            },
                                            "header": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [  
                                                   {
                                                        "type": "text",
                                                        "text": "ZH,BOTS",
                                                        "weight": "bold",
                                                        "color": "#FFFF00",
                                                        "size": "xl",
                                                        "align": "center"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "https://i.ibb.co/2Z376F8/IMG-20190129-131452.jpg",
                                                "size": "full",
                                                "aspectRatio": "20:13",
                                                "aspectMode": "cover",
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "🇮🇩 ɳαɱα тσҡεɳ 🇮🇩",
                                                        "color": "#FF3300",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                    }, {
                                                        "type": "text",
                                                        "text": "{}".format(fn["name"]),	
                                                        "color": "#00FF00",
                                                        "size": "xl",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 2,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 2,
                                                        "style": "primary",
                                                        "color": "#FFFF00",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "ᴄʀᴇᴀᴛᴏʀ",
                                                            "uri": "https://line.me/ti/p/~maul-703"
                                                        }
                                                    }, {
                                                        "flex": 3,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "FFFF00",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "ᴛᴀᴋᴇ ʏᴏᴜʀ ʟɪɴᴋ",
                                                            "uri": "line://app/1603968955-ORWb9RdY/?type=text&text={}".format(urllib.parse.quote("{}".format(fn["name"])))
                                                        }
                                                    }]
                                                }]
                                            }
                                        }
                                    )
                                  k = len(ret_)//10
                                  for aa in range(k+1):
                                      data = {
                                          "type": "flex",
                                          "altText": "Token",
                                          "contents": {
                                              "type": "carousel",
                                              "contents": ret_[aa*10 : (aa+1)*10]
                                          }
                                      }
                                      client.postTemplate(to, data)

#==========================TAMPILAN ME & ME2====================================
                        elif cmd == "menu":
                          if msg._from in admin:
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/56G5mR3/images-2.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "xs",
                 "action": {
                   "type": "uri",
                   "label": "Musik Joox",
                   "uri": "line://app/1623679774-z6dOvOV9"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/kczj6Z3/20190211-032421.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "xs",
                 "action": {
                   "type": "uri",
                   "label": "Sound Clouds",
                   "uri": "line://app/1623679774-lGOq9q3G"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/YhG678n/unnamed-1.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "xs",
                 "action": {
                   "type": "uri",
                   "label": "Smulle ID",
                   "uri": "line://app/1623679774-qmmXPXJ5"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/ZY7NZBs/3608024724-e7714bcedd-z.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "xs",
                 "action": {
                   "type": "uri",
                   "label": "Google",
                   "uri": "line://app/1623679774-3vDKkKaP"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/b27wkKk/1486988-9996a116-d7f4-488a-8bd6-98d20162ee86.png",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Google Play Store",
                   "uri": "line://app/1623679774-qmmXPXJ5"
                 }
               }
            ]
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/Kqg7Qmy/header.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Game Online",
                   "uri": "line://app/1609524990-ODaJ0Va0"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/BKRYPsm/unnamed.png",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Main Game",
                   "uri": "line://app/1623679774-j4rZkZ51"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/ysYBxrv/images-3.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Photo Editor",
                   "uri": "line://app/1623679774-1pKn8ngr"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/d4TcJjL/textpro-me.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Text Neon Editor",
                   "uri": "line://app/1609524990-pdlOGglG"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/KGqL2SK/tv-704887.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "TV Online",
                   "uri": "line://app/1623679774-WVajRjDn"
                 }
               }
            ]
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/1qzvnLR/images-1.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Notepad",
                   "uri": "line://app/1623679774-pXJyQy1D"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/st7DcZT/youtube-logo-black-background.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Get Channel",
                   "uri": "line://app/1623679774-9GWpqpGw"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/61SWtyx/images-4.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Facebook",
                   "uri": "line://app/1609524990-mpvZ5xv5"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/JmK8WqQ/twitter.png",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Twitter",
                   "uri": "https://mobile.twitter.com"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/mhh8f8T/images-5.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FFFFFF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Instagram",
                   "uri": "https://www.instagram.com/"
                 }
               }
            ]
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)


                        elif cmd == "me":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)                   
                                cover = client.getProfileCoverURL(sender)
                                data = {
   "contents": [{
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "🚥⟬PROFIL MU⟭🚥",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
{
"type": "separator",
"color": "#33ffff"
},{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [         
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(status.displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/4N1BjnV/20190427-175005.png", #watshaphttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/6282135759022",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~greetolala999",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://call/contacts"
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🚥ZHR FAMILY BOTS🚥",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~maul-703",
          },
           "align": "center"
          }
        ]
      }
    }, #Batas1
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "🚥⟬COVER MU⟭🚥",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
{
"type": "separator",
"color": "#33ffff"
}, #Fotoprofile
{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": cover,
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "{}".format(status.displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [ 
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
       "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"   
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🚥ZHR FAMILY BOTS🚥",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~maul-703",
          },
           "align": "center"
          }
        ]
      }
 }, #Batas1
    {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
            },
           {
            "contents": [
              {
            "text": "🚥⟬PROFIL TEAM⟭🚥",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
{
"type": "separator",
"color": "#33ffff"
}, #Fotoprofile
{
"contents": [{"type": "separator","color": "#33ffff"},{
"type": "image",
"url": "https://i.ibb.co/sJW6Dg5/20200129-044522.jpg",
"size": "full",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~maul-703",
            },
            "flex": 0
}
],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
{"type": "separator",
"color": "#33ffff"
}
],
"type": "box",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
         },
         {
        "contents": [
        { 
        "type": "separator",
         "color": "#33ffff"
         },
         {
            "contents": [
              {
"text": "zhr protection",
           "size": "xxs",
           "align": "center",
           "color": "#ccff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {
       "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/fxWzxcR/20190428-232352.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/settings"
            },
            "flex": 1
            },
            {
            "type": "image",
            "url": "https://i.ibb.co/cb7WqMS/20190428-232825.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profile"   
          },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/7YVnNPF/20190625-190410.png", #https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://joox.com"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🚥ZHR FAMILY BOTS🚥",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#aaaaaa",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~maul-703",
          },
           "align": "center"
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)

                        elif cmd == "me3":
                              if msg._from in admin:
                                contact = client.getContact()
                                client.sendImageWithURL(to, str(cover))
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)                               	
                                data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/L17HWJ0/IMG-20200120-190800.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴾᴿᴼ𝖋ᶦᴸ ᴹu",
                "size": "xs",
                "color": "#FFFFFF",
                "align": "center",
                "wrap": false,
                "weight": "regular",
                "offsetTop": "2px"
              },
              {
                "type": "separator",
                "color": "#00FFFF",
                "margin": "sm"
              }
            ],
            "position": "absolute",
            "width": "130px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "cornerRadius": "5px",
            "offsetTop": "10px",
            "height": "400px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
                "position": "absolute",
                "size": "full",
                "aspectMode": "cover"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "𝔫𝔞𝔪𝔢: {}".format(status.displayName),
                    "weight": "regular",
                    "align": "center",
                    "wrap": false,
                    "size": "sm",
                    "color": "#FFFFFF"
                  }
                ],
                "position": "absolute",
                "width": "130px",
                "borderWidth": "1px",
                "backgroundColor": "#000000",
                "height": "20px",
                "offsetTop": "116px"
              }
            ],
            "position": "absolute",
            "width": "130px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "height": "138px",
            "offsetTop": "32px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝖘𝖊ι𝖋𝖇𝖔𝖙𝖘 ༒ཇཀཌℓค༒ཇ",
                "size": "xs",
                "color": "#ff0000",
                "align": "center",
                "wrap": false,
                "weight": "regular",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "130px",
            "height": "23px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "offsetTop": "169px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/vv5gkR7/line.png",
                    "position": "absolute",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "position": "absolute",
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/ZY7NZBs/3608024724-e7714bcedd-z.jpg",
                    "position": "absolute",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "position": "absolute",
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "24px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/b27wkKk/1486988-9996a116-d7f4-488a-8bd6-98d20162ee86.png",
                    "aspectMode": "cover",
                    "size": "full",
                    "position": "absolute"
                  }
                ],
                "width": "22px",
                "height": "22px",
                "borderWidth": "1px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "position": "absolute",
                "offsetStart": "49px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/JmK8WqQ/twitter.png",
                    "position": "absolute",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "position": "absolute",
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "74px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/mhh8f8T/images-5.jpg",
                    "aspectMode": "cover",
                    "size": "full",
                    "position": "absolute"
                  }
                ],
                "position": "absolute",
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "98px"
              }
            ],
            "position": "absolute",
            "width": "122px",
            "height": "25px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "cornerRadius": "3px",
            "offsetTop": "195px",
            "offsetStart": "19px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "⟭⃫⃟Ꮓ卄ℜ 𝖋𝖆𝔪ᎥℒY 𝖇𝖔𝖙𝖘⟭⃫⃟",
                "color": "#FFFFFF",
                "size": "xs",
                "weight": "regular",
                "align": "center",
                "wrap": false
              }
            ],
            "backgroundColor": "#0000B8",
            "borderWidth": "4px",
            "borderColor": "#0000B8"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/L17HWJ0/IMG-20200120-190800.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "♣ cover ᴹu ♣",
                "weight": "regular",
                "align": "center",
                "wrap": false,
                "size": "xs",
                "color": "#FFFFFF",
                "offsetTop": "2px"
              },
              {
                "type": "separator",
                "margin": "sm",
                "color": "#00FFFF"
              }
            ],
            "width": "130px",
            "borderWidth": "1px",
            "position": "absolute",
            "borderColor": "#00FFFF",
            "cornerRadius": "5px",
            "offsetTop": "10px",
            "height": "400px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": cover,
                "size": "full",
                "aspectMode": "cover",
                "position": "absolute"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "𝔫𝔞𝔪𝔢: {}".format(status.displayName),
                    "align": "center",
                    "weight": "regular",
                    "wrap": false,
                    "color": "#FFFFFF",
                    "size": "xs"
                  }
                ],
                "offsetTop": "116px",
                "backgroundColor": "#000000",
                "width": "130px",
                "position": "absolute",
                "height": "20px"
              }
            ],
            "position": "absolute",
            "width": "130px",
            "height": "138px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "offsetTop": "32px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝖘𝖊ι𝖋𝖇𝖔𝖙𝖘 ༒ཇཀཌℓค༒ཇ",
                "size": "xs",
                "color": "#ff0000",
                "offsetTop": "2px",
                "weight": "regular",
                "align": "center",
                "wrap": false
              }
            ],
            "offsetTop": "169px",
            "width": "130px",
            "height": "23px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "position": "absolute",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#000000"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/vv5gkR7/line.png",
                    "position": "absolute",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "position": "absolute",
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/ZY7NZBs/3608024724-e7714bcedd-z.jpg",
                    "size": "full",
                    "aspectMode": "cover",
                    "position": "absolute"
                  }
                ],
                "position": "absolute",
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "24px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/b27wkKk/1486988-9996a116-d7f4-488a-8bd6-98d20162ee86.png",
                    "size": "full",
                    "aspectMode": "cover",
                    "position": "absolute"
                  }
                ],
                "position": "absolute",
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "49px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/JmK8WqQ/twitter.png",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "74px",
                "position": "absolute"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/mhh8f8T/images-5.jpg",
                    "position": "absolute",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "98px",
                "position": "absolute"
              }
            ],
            "offsetTop": "195px",
            "offsetStart": "19px",
            "position": "absolute",
            "width": "122px",
            "height": "25px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "cornerRadius": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "⟭⃫⃟Ꮓ卄ℜ 𝖋𝖆??ᎥℒY 𝖇𝖔𝖙𝖘⟭⃫⃟",
                "size": "xs",
                "color": "#ffffff",
                "weight": "regular",
                "align": "center",
                "wrap": false
              }
            ],
            "backgroundColor": "#0000B8",
            "borderWidth": "4px",
            "borderColor": "#0000B8"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/L17HWJ0/IMG-20200120-190800.jpg",
            "position": "absolute",
            "gravity": "top",
            "margin": "xxl",
            "size": "full",
            "aspectRatio": "2:3",
            "aspectMode": "cover",
            "offsetTop": "0px",
            "offsetStart": "0px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "♣ ᴾᴿᴼ𝖋ᶦᴸ ᵀᴱᴬᴹ ♣",
                "weight": "regular",
                "align": "center",
                "wrap": false,
                "size": "xs",
                "color": "#FFFFFF",
                "offsetTop": "2px"
              },
              {
                "type": "separator",
                "color": "#00FFFF",
                "margin": "sm"
              }
            ],
            "position": "absolute",
            "width": "130px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "cornerRadius": "5px",
            "offsetTop": "10px",
            "height": "400px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                    "size": "full",
                    "aspectMode": "cover",
                    "position": "relative"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "𝔫𝔞𝔪𝔢: Ꮓ卄ℜ 𝖇𝖔𝖙𝖘",
                        "weight": "regular",
                        "align": "center",
                        "wrap": false,
                        "size": "sm",
                        "color": "#FFFFFF"
                      }
                    ],
                    "width": "130px",
                    "height": "20px",
                    "backgroundColor": "#000000",
                    "position": "absolute",
                    "offsetTop": "116px"
                  }
                ]
              }
            ],
            "position": "absolute",
            "width": "130px",
            "height": "138px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "offsetTop": "32px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝖘𝖊ι𝖋𝖇𝖔𝖙𝖘 ༒ཇཀཌℓค༒ཇ",
                "size": "xs",
                "color": "#ff0000",
                "weight": "regular",
                "align": "center",
                "wrap": false,
                "offsetTop": "2px"
              }
            ],
            "offsetTop": "169px",
            "offsetStart": "15px",
            "position": "absolute",
            "width": "130px",
            "height": "23px",
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "hello, world"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/vv5gkR7/line.png",
                    "position": "absolute",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "position": "absolute",
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "1px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/ZY7NZBs/3608024724-e7714bcedd-z.jpg",
                    "position": "absolute",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "position": "absolute",
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "25px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/b27wkKk/1486988-9996a116-d7f4-488a-8bd6-98d20162ee86.png",
                    "aspectMode": "cover",
                    "size": "full",
                    "position": "absolute"
                  }
                ],
                "width": "22px",
                "height": "22px",
                "cornerRadius": "30px",
                "offsetTop": "1px",
                "offsetStart": "49px",
                "position": "absolute"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/JmK8WqQ/twitter.png",
                    "aspectMode": "cover",
                    "size": "full",
                    "position": "absolute"
                  }
                ],
                "offsetTop": "1px",
                "cornerRadius": "30px",
                "width": "22px",
                "height": "22px",
                "position": "absolute",
                "offsetStart": "74px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/mhh8f8T/images-5.jpg",
                    "position": "absolute",
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ],
                "offsetStart": "98px",
                "offsetTop": "1px",
                "cornerRadius": "30px",
                "height": "22px",
                "width": "22px",
                "position": "absolute"
              }
            ],
            "offsetTop": "195px",
            "offsetStart": "19px",
            "cornerRadius": "3px",
            "borderColor": "#00ffff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "122px",
            "height": "25px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "⟭⃫⃟Ꮓ卄ℜ 𝖋𝖆𝔪ᎥℒY 𝖇𝖔𝖙𝖘⟭⃫⃟",
                "size": "xs",
                "color": "#ffffff",
                "weight": "regular",
                "align": "center",
                "wrap": false
              }
            ],
            "backgroundColor": "#0000B8",
            "offsetTop": "240px",
            "offsetStart": "0px",
            "width": "300px",
            "position": "absolute",
            "borderWidth": "4px",
            "borderColor": "#0000B8"
          }
        ]
      }
    }
  ]
}
                                client.postFlex(op.param1, data)


#=========================BAGIAN ABOUT====================================
                        elif cmd == "about":
                                groups = client.getGroupIdsJoined()
                                contacts = client.getAllContactIds()
                                blockeds = client.getBlockedContactIds()
                                crt = "u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6"
                                supp = "u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6","u2dab61a80a46a7dd521555a50b3699a6"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                runtime = timeNoww - clientStart
                                runtime = timeChange(runtime)
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n│ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "ZHR FAMILY BOTS",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000033"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    },
    "header": {
      "backgroundColor": "#000033"
    }
  },
  "type": "bubble",
  "size": "kilo",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),
            "type": "image",
            "size": "full",
            "aspectRatio": "2:3",
            "aspectMode": "cover"
          },
          {
            "type": "separator",
            "color": "#33ffff"
          },
          {
            "text": "\n❂ SELFBOT ❂\n+\n❂ ANTI-JS ❂",
            "size": "md",
            "align": "center",
            "color": "#ccff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#33ffff"
      },
      {
        "contents": [
          {
            "text": "🚥selfbot ᴠᴇʀsɪᴏɴ : v5.0🚥",
            "size": "md",
            "align": "center",
            "color": "#00FF33",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://i.ibb.co/sJW6Dg5/20200129-044522.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "❂➣ɴᴀᴍᴀ: {}".format(client.getProfile().displayName),
                "size": "md",
                "margin": "none",
                "color": "#ccff00",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#33ffff"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/sJW6Dg5/20200129-044522.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "❂➣ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ : {}".format(str(runtime)),
                "size": "md",
                "margin": "none",
                "color": "#ccff00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/sJW6Dg5/20200129-044522.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "❂➣ᴊᴜᴍʟᴀʜ ɢʀᴏᴜᴘ : {}".format(str(len(groups))),
                "size": "md",
                "margin": "none",
                "color": "#ccff00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/sJW6Dg5/20200129-044522.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "❂➣ᴊᴜᴍʟᴀʜ ᴛᴇᴍᴀɴ : {}".format(str(len(contacts))),
                "size": "md",
                "margin": "none",
                "color": "#ccff00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/sJW6Dg5/20200129-044522.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "❂➣ᴊᴜᴍʟᴀʜ ʙʟᴏᴋ : {}".format(str(len(blockeds))),
                "size": "md",
                "margin": "none",
                "color": "#ccff00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/sJW6Dg5/20200129-044522.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "❂➣zahra_maul",
                "size": "md",
                "margin": "none",
                "color": "#ccff00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/sJW6Dg5/20200129-044522.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "❂➣Mყ Sน℘℘σгt \n❂ zhr ʙ❍ᴛs\n❂ Dn Family ʙ❍ᴛs\n❂ ʙ❍ᴛs lemah",
                "size": "md",
                "margin": "none",
                "color": "#ccff00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#00FF33",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "🚥chat to ᴄʀᴇᴀᴛᴏʀ🚥",
                  "uri": "https://line.me/ti/p/~maul-703"
              }
          }]
      }]
  },
  "header": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "🚥ZHR FAMILY BOTS🚥",
                "size": "md",
                "weight": "bold",
                "color": "#00FF33",
                "type": "text",
                "align": "center"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                client.postTemplate(to, data)

#=========================ORDERAN==================================================================
                        if cmd == "xxxxxxxxxxqqq":                                   
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/TmTFmMz/20190205-082453.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🍓 Şᴇʟғ ʙ❍ᴛŞ 🍓",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#00FF00",
            "align": "center"            
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "👔sʙ ᴛᴇᴍᴘʟᴀᴛᴇ & sʙ ᴀɴᴛɪ - ᴊs👔",
                    "color": "#BF00FF",
                    "wrap": True,
                    "weight": "bold",
                    "size": "md",
                    "type": "text",
                    "align": "center"            
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍎 sʙ ᴏɴʟʏ =  ☞ 50ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍎 sʙ ᴛᴇᴍᴘʟᴀᴛᴇ =  ☞ 65ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍎 sʙ ᴀɴᴛɪ-ᴊs =  ☞ 65ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "CATATAN: \n━━━━━━━━━━\nʙᴏᴛ ғᴜʟʟ ᴛᴇᴍᴘʟᴀᴛᴇ ᴅᴀɴ ғɪᴛᴜʀ ᴍᴇɴᴀʀɪᴋ ᴡᴀʀɴᴀ ʙɪsᴀ ᴅɪ ʀᴇǫ.",
                    "color": "#FFFFFF",
                    "size": "sm",
                    "wrap": True,
                    "type": "text"
                  },
                  {
                    "url": "https://i.ibb.co/S5xgmk6/20190206-205139.jpg",
                    "type": "image",
                    "size": "full"
                  }
                ],
                "type": "box",
                "spacing": "md",
                "layout": "horizontal"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "horizontal"
          },
          {
            "text": "ɓყ : ZH,BOTS",
            "size": "xs",
            "align": "end",
            "color": "#00FFFF",
            "wrap": True,
            "type": "text",
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "\n🍄 ℘Ʀᴏᴛᴇᴄᴛ ᴀɴᴛ-ᴊŞ 🍄",
                    "color": "#00FF00",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "align": "center",          
                    "size": "xl"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "ZH,BOTS",
                    "color": "#BF00FF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "align": "center",          
                    "size": "md"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍄 6 ʙᴏᴛs  =  ☞ 120ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍄 8 ʙᴏᴛs  =  ☞ 150ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },

          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍄 11 ʙᴏᴛs  =  ☞ 200ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍄 15 ʙᴏᴛs  =  ☞ 230ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "KEUNTUNGAN : \n━━━━━━━━━━\nғʀᴇᴇ sᴇʟғʙᴏᴛ ᴛᴇᴍᴘʟᴀᴛᴇ.",
                    "color": "#FFFFFF",
                    "size": "sm",
                    "wrap": True,
                    "type": "text"
                  },
                  {
                    "url": "https://i.ibb.co/9bxRrZd/20190206-230645.jpg",
                    "type": "image",
                    "size": "full"
                  }
                ],
                "type": "box",
                "spacing": "md",
                "layout": "horizontal"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "horizontal"
          },
          {
            "text": "ɓყ : xεɓε૨ℓɦყɳ",
            "size": "xs",
            "align": "end",
            "color": "#00FFFF",
            "wrap": True,
            "type": "text",
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "\n🍆 ℘Ʀᴏᴛᴇᴄᴛ ƦᴏᴏM 🍆",
                    "color": "#00FF00",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "align": "center",          
                    "size": "xl"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "👔şᴍᴜʟʟᴇ, ᴇᴠᴇɴᴛ & ᴄʜᴀᴛ👔",
                    "color": "#BF00FF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "align": "center",          
                    "size": "md"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍆 ʀᴏᴏᴍ sᴍᴜʟʟᴇ = ☞ 120ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍆 ʀᴏᴏᴍ ᴇᴠᴇɴᴛ = ☞ 150ʀʙ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "KEUNTUNGAN : \n━━━━━━━━━━\nʙɪsᴀ ᴛᴀᴍʙᴀʜɪɴ ᴀᴅᴍɪɴ ᴅᴀɴ sᴛᴀғғ, ᴏᴡɴᴇʀ ᴅᴀɴ ғᴏᴜɴᴅᴇʀ ғʀᴇᴇ sʙ ᴛᴇᴍᴘʟᴀᴛᴇ.",
                    "color": "#FFFFFF",
                    "size": "sm",
                    "wrap": True,
                    "type": "text"
                  },
                  {
                    "url": "https://i.ibb.co/yYWhMCC/20190206-234040.jpg",
                    "type": "image",
                    "size": "full"
                  }
                ],
                "type": "box",
                "spacing": "md",
                "layout": "horizontal"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "horizontal"
          },
          {
            "text": "ɓყ : мαul",
            "size": "xs",
            "align": "end",
            "color": "#00FFFF",
            "wrap": True,
            "type": "text",
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#4682B4",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "Cʜᴀᴛ ᴛᴏ ᴄƦᴇᴀᴛᴏƦS",
                      "uri": "http://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "мαul",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}

                                    client.postFlex(to, data)

#=================BAGIAN PROMO==================================
                        elif cmd == "promo":
                            if msg._from in owner:
                                saya = client.getGroupIdsJoined()
                                for groups in saya:      
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/TmTFmMz/20190205-082453.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~maul-703",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🍓 Şᴇʟғ ʙ❍ᴛŞ 🍓",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#00FF00",
            "align": "center"            
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "👔sʙ ᴛᴇᴍᴘʟᴀᴛᴇ & sʙ ᴀɴᴛɪ - ᴊs👔",
                    "color": "#BF00FF",
                    "wrap": True,
                    "weight": "bold",
                    "size": "md",
                    "type": "text",
                    "align": "center"            
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍎 sʙ ᴏɴʟʏ =  ☞ 50ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍎 sʙ ᴛᴇᴍᴘʟᴀᴛᴇ =  ☞ 65ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍎 sʙ ᴀɴᴛɪ-ᴊs =  ☞ 65ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "CATATAN: \n━━━━━━━━━━\nʙᴏᴛ ғᴜʟʟ ᴛᴇᴍᴘʟᴀᴛᴇ ᴅᴀɴ ғɪᴛᴜʀ ᴍᴇɴᴀʀɪᴋ ᴡᴀʀɴᴀ ʙɪsᴀ ᴅɪ ʀᴇǫ.",
                    "color": "#FFFFFF",
                    "size": "sm",
                    "wrap": True,
                    "type": "text"
                  },
                  {
                    "url": "https://i.ibb.co/S5xgmk6/20190206-205139.jpg",
                    "type": "image",
                    "size": "full"
                  }
                ],
                "type": "box",
                "spacing": "md",
                "layout": "horizontal"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "horizontal"
          },
          {
            "text": "ɓყ : ZH,BOTS",
            "size": "xs",
            "align": "end",
            "color": "#00FFFF",
            "wrap": True,
            "type": "text",
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "\n🍄 ℘Ʀᴏᴛᴇᴄᴛ ᴀɴᴛ-ᴊŞ 🍄",
                    "color": "#00FF00",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "align": "center",          
                    "size": "xl"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "ZH,BOTS",
                    "color": "#BF00FF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "align": "center",          
                    "size": "md"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍄 6 ʙᴏᴛs  =  ☞ 120ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍄 8 ʙᴏᴛs  =  ☞ 150ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },

          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍄 11 ʙᴏᴛs  =  ☞ 200ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍄 15 ʙᴏᴛs  =  ☞ 230ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "KEUNTUNGAN : \n━━━━━━━━━━\nғʀᴇᴇ sᴇʟғʙᴏᴛ ᴛᴇᴍᴘʟᴀᴛᴇ.",
                    "color": "#FFFFFF",
                    "size": "sm",
                    "wrap": True,
                    "type": "text"
                  },
                  {
                    "url": "https://i.ibb.co/9bxRrZd/20190206-230645.jpg",
                    "type": "image",
                    "size": "full"
                  }
                ],
                "type": "box",
                "spacing": "md",
                "layout": "horizontal"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "horizontal"
          },
          {
            "text": "ɓყ :мαul",
            "size": "xs",
            "align": "end",
            "color": "#00FFFF",
            "wrap": True,
            "type": "text",
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "\n🍆 ℘Ʀᴏᴛᴇᴄᴛ ƦᴏᴏM 🍆",
                    "color": "#00FF00",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "align": "center",          
                    "size": "xl"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "👔şᴍᴜʟʟᴇ, ᴇᴠᴇɴᴛ & ᴄʜᴀᴛ👔",
                    "color": "#BF00FF",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "align": "center",          
                    "size": "md"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍆 ʀᴏᴏᴍ sᴍᴜʟʟᴇ = ☞ 120ʀʙ/ʙʟɴ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "🍆 ʀᴏᴏᴍ ᴇᴠᴇɴᴛ = ☞ 150ʀʙ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": "KEUNTUNGAN : \n━━━━━━━━━━\nʙɪsᴀ ᴛᴀᴍʙᴀʜɪɴ ᴀᴅᴍɪɴ ᴅᴀɴ sᴛᴀғғ, ᴏᴡɴᴇʀ ᴅᴀɴ ғᴏᴜɴᴅᴇʀ ғʀᴇᴇ sʙ ᴛᴇᴍᴘʟᴀᴛᴇ.",
                    "color": "#FFFFFF",
                    "size": "sm",
                    "wrap": True,
                    "type": "text"
                  },
                  {
                    "url": "https://i.ibb.co/yYWhMCC/20190206-234040.jpg",
                    "type": "image",
                    "size": "full"
                  }
                ],
                "type": "box",
                "spacing": "md",
                "layout": "horizontal"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "horizontal"
          },
          {
            "text": "ɓყ :ZH,BOTS",
            "size": "xs",
            "align": "end",
            "color": "#00FFFF",
            "wrap": True,
            "type": "text",
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#000000",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "Cʜᴀᴛ ᴛᴏ ᴄƦᴇᴀᴛᴏƦS",
                      "uri": "http://line.me/ti/p/~maul-703"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ZH,BOTS",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#000000",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                    client.postFlex(groups, data)

#=====================BAGIAN BROADCAST==================================================
                        if cmd.startswith("bc "):
                	        if msg._from in admin:
                	            sep = text.split(" ")
                	            bc = text.replace(sep[0] + " ","")
                	            saya = client.getGroupIdsJoined()
                	            for rom in saya:
                	                try:client.sendMessage(rom," "+bc);client.sendContact(rom,"ua469ac2f8440ce1f5697d16bcf01f660")
                	                except:pass
                	            client.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(saya))))

                        elif cmd.startswith("broadcast2: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = client.getGroupIdsJoined()
                               for group in saya:
                                   data = {
                                           "type": "flex",
                                           "altText": "BROADCASH Viruѕ тeaм",
                                           "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": pesan,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF3300"
    },
    "header": {
      "backgroundColor": "#FF3300"
    }
  },  
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#000000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴏʀᴅᴇʀᴀɴ",
                  "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=order"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#000000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "https://line.me/ti/p/~maul-703"
              }
          }]
      }]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "🎉ʙʀᴏᴀᴅᴄᴀsʜ🎉",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"            
      }
    ]
  }
}
}
                                   client.postTemplate(group, data)

#============================BAGIAN SMULE===========================================
                        elif msg.text.lower().startswith("song: "):
                            separate = text.split(" ")
                            channel = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0"
                                r = web.get("http://api.fckveza.com/downloadsmule={}".format(urllib.parse.quote(channel)))
                                data = r.text
                                data = json.loads(data)
                                for design in data["result"]:
                                    image = design["image"]
                                    url = design["url"]
                                data = {
                                        "type": "flex",
                                        "altText": "Smule Viruѕ тeaм",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF3300"
    },
    "header": {
      "backgroundColor": "#FF3300"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": image,
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "\n🎶MP3🎶\nSMULE",
            "size": "xl",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "align": "center"            
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "❂🇮🇩➢ sᴏɴɢs sᴍᴜʟʟᴇʀ\n❂🇮🇩➢ ᴋᴇᴛɪᴋ sᴏɴɢ:☞ ʟɪɴᴋ sᴍᴜʟᴇ ☜" ,
                "size": "xs",
                "margin": "none",
                "color": "#00FF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#6A5ACD",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "https://line.me/ti/p/~maul-703"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#4682B4",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴅᴏᴡɴʟᴏᴅ ᴍᴘ3",
                  "uri": url
              }
          }]
      }]
  },
  "header": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Viruѕ тeaм",
                "size": "xl",
                "weight": "bold",
                "align": "center",            
                "color": "#FFD700",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                client.postTemplate(to, data)
                                client.sendAudioWithURL(msg.to, url)

                        elif cmd.startswith("mp3 "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.fckveza.com/jooxmusic={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = ""
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n➢ {}. {}".format(str(num), str(music["judul"]))
                                    ret_ += "".format(str(len(music)))
                                    people = "ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟ ᴍᴜsɪᴋ\nsɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ\nᴍᴜsɪᴋ:「ᴊᴜᴅᴜʟ ʟᴀɢᴜ ᴋᴇsᴜᴋᴀᴀɴ」"
                                    people1 = "🇮🇩 ᴅᴀғᴛᴀʀ ᴍᴘ3 ᴘɪʟɪʜᴀɴ 🇮🇩"
                                    sendTextTemplate7(to, str(ret_), people, people1)
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.fckveza.com/musicid={}".format(str(music["songid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data != []:
                                            ret_ = "❂🇮🇩➢ Vocal : {}".format(str(data["result"][0]["artis"]))
                                            ret_ += "\n❂🇮🇩➢ Judul : {}".format(str(data["result"][0]["judul"]))
                                            ret_ += "\n❂🇮🇩➢ Album : {}".format(str(data["result"][0]["single"]))
                                            image = str(data["result"][0]["imgUrl"])
                                            links = str(data["result"][0]["mp3Url"])
                                            client.sendAudioWithURL(to, str(data["result"][0]["mp3Url"]))





                        elif cmd.startswith("musik "):
                           if msg._from in admin: 
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "\n❂🇮🇩➢ ᴠᴏᴋᴀʟ : "+str(d)
                                hasil += "\n❂🇮??➢ ᴊᴜᴅᴜʟ : "+str(c)
                                data = {
                                        "type": "flex",
                                        "altText": "Musik Viruѕ тeaм",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF3300"
    },
    "header": {
      "backgroundColor": "#FF3300"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": g,
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "\n🎶MP3🎶",
            "size": "xl",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "align": "center"            
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": hasil,
                "size": "xs",
                "margin": "none",
                "color": "#00FF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#000000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "https://line.me/ti/p/~maul-703"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#4682B4",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴅᴏᴡɴʟᴏᴅ ᴍᴘ3",
                  "uri": e
              }
          }]
      }]
  },
  "header": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Viruѕ тeaм",
                "size": "xl",
                "weight": "bold",
                "align": "center",            
                "color": "#000000",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                client.postTemplate(to, data)
                                client.sendAudioWithURL(to,e)
                            except Exception as error:
                                client.sendMessage(to, "📣 eror bos" + str(error))
                                logError(error)



                        elif cmd.startswith("sing "):
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] +" ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api.fckveza.com/record={}".format(urllib.parse.quote(links)))
                                time.sleep(2)
                                data = {
                                        "type": "flex",
                                        "altText": "smule Xeberlhyn",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF3300"
    },
    "header": {
      "backgroundColor": "#FF3300"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://i.ibb.co/gyzYpJ5/images-3.jpg",
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": " \n\n🎶 SMULE 🎶 ",
            "size": "sm",
            "color": "#FFFF00",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "align": "center"            
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "❂➣ ID Smule : "+smule+"\n❂➣ Link:\n"+links,
                "size": "xs",
                "margin": "none",
                "color": "#00FF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "header": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Viruѕ тeaм",
                "size": "xl",
                "weight": "bold",
                "align": "center",            
                "color": "#000000",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#000000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "https://line.me/ti/p/~maul-703"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#4682B4",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴛᴏ sɪɴɢ",
                  "uri": links
              }
          }]
      }]
  }
}
}
                                client.postTemplate(to, data)
                            except Exception as e:
                                pass


#=============================STICKER==========================================================================
                        if "itel" in msg.text.lower():
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://4.bp.blogspot.com/-nJ4iMqsxTQc/WwJ97etgoiI/AAAAAAAIoGM/_mG-H0OhIPMLPdJ85ApFDB9Nzxqr_74IwCLcBGAs/s1600/AW1084508_09.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "http://line.me/ti/p/~maul-703"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "asalamualaikum" in msg.text.lower():
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "imageUrl": "https://thumbs.gfycat.com/FirstPeriodicChimpanzee-size_restricted.gif",
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "http://line.me/ti/p/~maul-703"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "kabur" in msg.text.lower():
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "http://line.me/ti/p/~maul-703"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)


                        if "......" in msg.text.lower():
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "http://line.me/ti/p/~maul-703"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "........" in msg.text.lower():
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "http://line.me/ti/p/~maul-703"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "sue" in msg.text.lower():
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "http://line.me/ti/p/~maul-703"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)

                        if "sem" in msg.text.lower():
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                to = msg.to
                                data = {
                                            "type": "template",
                                            "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                            "template": {
                                               "type": "image_carousel",
                                               "columns": [
                                                {
                                                    "size": "full", 
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "http://line.me/ti/p/~maul-703"
                             }                                                
                   }
                  ]
                                            }
                                        }
                                client.postTemplate(to, data)
            except Exception as error:
                logError(error)

#=========================BAGIAN LIKE AND COMENT TIMELINE=====================================
        if op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != client.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "╔══[ Details Post ]"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = client.getContact(sender)
                                        auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n╠❂🇮🇩➢ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n╠❂🇮🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n╠❂🇮🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n╠❂🇮🇩➢ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n╠❂🇮🇩➢ Tulisan :\n╠❂🇮🇩➢ {}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n╚══[ Finish ]"
                                    sendTextTemplate(to, str(ret_))
                                except:
                                    sendTextTemplate(to, "        ❂.Done Like.By: Zhr protection")
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = client.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                adws = client.createComment(purl[0], purl[1], settings["commentPost"])
                                sendTextTemplate(to, "        ❂.Done Like.By: Zhr protection")
            except Exception as error:
                logError(error)

        if op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != client.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
#===============================MEDIA=============================================================
                            if text.lower() == 'kalender':
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                                sendTextTemplate(msg.to, readTime)

                            elif terminal.startswith("soundcloud "):
                                def sdc():
                                    kitsunesplit = rynSplitText(msg.text.lower()).split(" ")
                                    r = requests.get('https://soundcloud.com/search?q={}'.format(rynSplitText(msg.text.lower())))
                                    soup = BeautifulSoup(r.text,'html5lib')
                                    data = soup.find_all(class_='soundTitle__titleContainer')
                                    data = soup.select('li > h2 > a')
                                    if len(kitsunesplit) == 1:
                                        a = '          🎺 NOTE PILIHAN LAGU 🎺\n____________________________________';no=0
                                        for b in data:
                                            no+=1
                                            a+= '\n{}. {}'.format(no,b.text)
                                        sendTextTemplate5(to,a)
                                    if len(kitsunesplit) == 2:
                                        a = data[int(kitsunesplit[1])-1];b = list(a)[0]
                                        kk = random.randint(0,999)
                                        sendTextTemplate5(to,'Judul: {}\nStatus: Waiting... For Upload'.format(a.text))
                                        hh=subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output {}.mp3 {}'.format(kk,'https://soundcloud.com{}'.format(a.get('href'))))
                                        try:client.sendAudio(to,'{}.mp3'.format(kk))
                                        except Exception as e:sendTextTemplate(to,' 「 ERROR 」\nJudul: {}\nStatus: {}\nImportant: Try again'.format(a.text,e))
                                        os.remove('{}.mp3'.format(kk))
                                ryn = Thread(target=sdc)
                                ryn.daemon = True
                                ryn.start()
                                ryn.join()

#===============================BAGIAN SPAM================================================================
                            elif terminal.startswith("spaminvmid"):
                                dan = text.split("|")
                                nam = dan[1]
                                jlh = int(dan[2])
                                tar = dan[3]
                                grr = client.groups
                                client.findAndAddContactsByMid(tar)
                                if jlh <= 101:
                                    for var in range(0,jlh):
                                        gcr = client.createGroup(nam, [tar])
                                        Thread(target=client.inviteIntoGroup,args=(gcr.id, [tar]),).start()
                                        time.sleep(2)
                                        client.leaveGroup(gcr.id)
                                    client.sendMention(to, "Succesfully Spam Invite @! to Group {}".format(gcr.name), [tar])

                            elif terminal.startswith("spaminvite"):
                                key = eval(msg.contentMetadata["MENTION"])
                                tar = key["MENTIONEES"][0]["M"]
                                dan = text.split("|")
                                nam = dan[1]
                                jlh = int(dan[2])
                                grr = client.groups
                                client.findAndAddContactsByMid(tar)
                                if jlh <= 101:
                                    for var in range(0,jlh):
                                        gcr = client.createGroup(nam, [tar])
                                        client.inviteIntoGroup(gcr.id, [tar])
                                        time.sleep(2)
                                        client.leaveGroup(gcr.id)
                                    client.sendMention(to, "Succesfully Spam Invite @! to Group {}".format(gcr.name), [tar])
                                
                            elif terminal.startswith("chatowner: "):
                                contact = client.getContact(sender)
                                sep = text.split(" ")
                                ryan = text.replace(sep[0] + " ","")
                                for own in owner:
                                    result = "@!"
                                    result += "\nSender : {}".format(contact.displayName)
                                    result += "\nPesan : {}".format(ryan)
                                    result += "\nMid : {}".format(contact.mid)
                                    client.sendReplyMessage(msg_id, to, "Succesfully send chat to Owner")
                                    client.sendMention(own, result, [sender])
                                    client.sendContact(own, sender)

                            elif terminal.startswith("invtogc"):
                                key = eval(msg.contentMetadata["MENTION"])
                                tar = key["MENTIONEES"][0]["M"]
                                dan = text.split("|")
                                grr = client.getGroupIdsJoined()
                                client.findAndAddContactsByMid(tar)
                                try:
                                    listGroup = grr[int(dan)-1]
                                    gri = client.getGroup(listGroup)
                                    client.inviteIntoGroup(gri.id, [tar])
                                    client.sendMessage(to, "Succesfully invite {} to group {}".format(tar.displayName, gri.name))
                                except Exception as e:
                                    client.sendMessage(to, str(e))

                            elif terminal.startswith('spamtag '):
                                sep = text.split(" ")
                                num = int(sep[1])                           
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            client.sendMention(to, "@!", [ls])

                            elif terminal.startswith('spamcall '):
                                sep = text.split(" ")
                                num = int(sep[1])
                                try:                           
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            for var in range(0,num):
                                                group = client.getGroup(to)
                                                members = [ls]
                                                kunkun = client.getContact("u3a1a2458a60d209a3d4802e789b7d540").displayName
                                                client.acquireGroupCallRoute(to)
                                                client.inviteIntoGroupCall(to, contactIds=members)
                                            client.sendMention(to, "Succesfully Spamcall to @!", [ls])
                                except Exception as error:
                                    client.sendMessage(to, str(error))

          
                            elif terminal.startswith("spamchat"):
                              if sender in owner:
                                text = text.split("-")
                                jmlh = int(text[2])
                                balon = jmlh * (text[3]+"\n")
                                if text[1] == "on":
                                    if jmlh <= 999:
                                        for x in range(jmlh):
                                            client.sendMessage(to, text[3])
                                    else:
                                        client.sendMention(to, "Sorry the amount is too much :) @!", [sender])
                                elif text[1] == "off":
                                  if jmlh <= 999:
                                    client.sendMessage(to, balon)
                                  else:
                                    client.sendMention(to, "Sorry the amount is too much :) @!", [sender])

                            elif terminal.startswith('spamgift '):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                    txt = "~Gift~"
                                    client.sendMentionWithFooter(to, txt, "Succesfully Spam gift to your pc", [sender])
                                    for var in range(0,num):
                                       contact = client.getContact(sender)
                                       client.sendGift(contact.mid, random.choice(gf), "theme")                

                            elif terminal.startswith('spam'):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    client.sendMessage(to, "Succesfully Spam Call to Group")
                                    for var in range(0,num):
                                       group = client.getGroup(to)
                                       members = [mem.mid for mem in group.members]
                                       client.acquireGroupCallRoute(to)
                                       client.inviteIntoGroupCall(to, contactIds=members)


#=======================BAGIAN MEDIA MIMIC ❂🇮🇩➢
                            elif terminal == "mimiclist":
                              if msg._from in owner:
                                if settings["mimic"]["target"] == {}:
                                    client.sendMessage(to, "Tidak Ada Target")
                                else:
                                    no = 0
                                    result = "╔══[ Mimic List ]"
                                    target = []
                                    for mid in settings["mimic"]["target"]:
                                        target.append(mid)
                                        no += 1
                                        result += "\n├≽ {}. @!".format(no)
                                    result += "\n╚══[ Total {} Mimic ]".format(str(len(target)))
                                    client.sendMention(to, result, target)
                            elif terminal.startswith("mimicadd "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            if ls in settings["mimic"]["target"]:
                                                client.sendMessage(to, "Target sudah ada dalam list")
                                            else:
                                                settings["mimic"]["target"][ls] = True
                                                client.sendMessage(to, "Berhasil menambahkan target")
                                        except:
                                            client.sendMessage(to, "Gagal menambahkan target")
                            elif terminal.startswith("mimicdel "):
                              if msg._from in owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            if ls not in settings["mimic"]["target"]:
                                                client.sendMessage(to, "Target sudah tida didalam list")
                                            else:
                                                del settings["mimic"]["target"][ls]
                                                client.sendMessage(to, "Berhasil menghapus target")
                                        except:
                                            client.sendMessage(to, "Gagal menghapus target")

#==================MEDIA PRAYTIME KOTA MASING² ❂🇮🇩➢
                            elif terminal.startswith("praytime "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0]+ " ","")
                                url = requests.get("https://time.siswadi.com/pray/{}".format(txt))
                                data = url.json()
                                ret_ = "╭───「 Praytime at {} 」".format(txt)
                                ret_ += "\n├≽ Date : {}".format(data["time"]["date"])
                                ret_ += "\n├≽ Subuh : {}".format(data["data"]["Fajr"])
                                ret_ += "\n├≽ Dzuhur : {}".format(data["data"]["Dhuhr"])
                                ret_ += "\n├≽ Ashar : {}".format(data["data"]["Asr"])
                                ret_ += "\n├≽ Magrib : {}".format(data["data"]["Maghrib"])
                                ret_ += "\n├≽ Isha : {}".format(data["data"]["Isha"])
                                ret_ += "\n├≽ 1/3 Malam : {}".format(data["data"]["SepertigaMalam"])
                                ret_ += "\n├≽ Tengah Malam : {}".format(data["data"]["TengahMalam"])
                                ret_ += "\n├≽ 2/3 Malam : {}".format(data["data"]["DuapertigaMalam"])
                                ret_ += "\n├≽ 「 Always Remember to Your God :) 」"
                                ret_ += "\n╰───「 {} 」".format(txt)
                                client.sendMessageWithFooter(to, str(ret_))
                                address = ''.format(data["location"]["address"])
                                latitude = float(data["location"]["latitude"])
                                longitude = float(data["location"]["longitude"])
                                client.sendLocation(to, address,latitude,longitude)

#=======================MEDIA TELEVISION ❂🇮🇩➢
                            elif terminal.startswith("acaratv "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/acaratv.php?id={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba&type=separate".format(txt))
                                data = url.json()
                                no = 0
                                result = "╔══[ ~ Acara TV ~ ]"
                                for anu in data:
                                    no += 1
                                    result += "\n├≽ {}. {} >>> {} ".format(str(no),str(anu["acara"]),str(anu["jam"]))
                                result += "\n╚══[ ~ Acara TV ~ ]"
                                client.sendMessageWithFooter(to, result)

#====================MEDIA BINTANGMU ❂🇮🇩➢
                            elif terminal.startswith("zodiak "):
                              if msg._from in owner:
                                sep = msg.text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                                data1 = data["description"]
                                data2 = data["color"]
                                translator = Translator()
                                hasil = translator.translate(data1, dest='id')
                                hasil1 = translator.translate(data2, dest='id')
                                A = hasil.text
                                B = hasil1.text
                                ret_ = "🍀 Ramalan zodiak {} hari ini 🍀\n".format(str(query))
                                ret_ += str(A)
                                ret_ += "\n======================\n🍀 Tanggal : " +str(data["current_date"])
                                ret_ += "\n?? Rasi bintang : "+query
                                ret_ += " ("+str(data["date_range"]+")")
                                ret_ += "\n🍀 Pasangan Zodiak : " +str(data["compatibility"])
                                ret_ += "\n🍀 Angka keberuntungan : " +str(data["lucky_number"])
                                ret_ += "\n🍀 Waktu keberuntungan : " +str(data["lucky_time"])
                                ret_ += "\n🍀 Warna kesukaan : " +str(B)
                                client.sendMessage(to, str(ret_))

#=======================MEDIA ANIME ❂🇮🇩➢
                            elif terminal.startswith("samehadaku "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/samehadaku.php?id={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba".format(txt))
                                data = url.json()
                                no = 0
                                result = "╔══[ ~ Samehadaku ~ ]"
                                for anu in data:
                                    no += 1
                                    result += "\n├≽ {}. {}".format(str(no),str(anu["title"]))
                                    result += "\n├≽ {}".format(str(anu["url"]))
                                    result += "\n├≽ {}".format(str(anu["date"]))
                                result += "\n╚══[ {} Anime ]".format(str(len(data)))
                                client.sendMessageWithFooter(to, result)

#===================MEDIA AL'QURAN ❂🇮🇩➢                           
                            elif terminal.startswith("mtoh "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.aladhan.com/v1/gToH?date={}".format(txt))
                                data = url.json()
                                result = "~ Hijriah ~ = {}".format(str(data["data"]["hijri"]["date"]))
                                result += "\n~ Masehi ~ = {}".format(str(data["data"]["gregorian"]["date"]))
                                client.sendMessageWithFooter(to, result)

                            elif terminal.startswith("asmaulhusna"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.aladhan.com/asmaAlHusna/{}".format(txt))
                                data = url.json()
                                result = "~ Asma Allah ke {} = ~ {} ~".format(txt,data["data"][0]["name"])
                                result += "\n~Artinya =~ {} ~".format(data["data"][0]["en"]["meaning"])
                                client.sendMessageWithFooter(to, result)

                            elif terminal.startswith("al-qur'an"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                web = requests.get("http://api.alquran.cloud/surah/{}".format(txt))
                                data = web.json()
                                result = "~[~{}~]~".format(data["data"]["englishName"])
                                quran = data["data"]
                                result += "\n~ Surah ke {} ~".format(quran["number"])
                                result += "\n~ Nama Surah ~ {} ~".format(quran["name"])
                                result += "\n~ {} Ayat ~".format(quran["numberOfAyahs"])
                                result += "\n~ {} ~".format(quran["name"])
                                result += "\n~ Ayat Sajadah = {} ~".format(quran["ayahs"][0]["sajda"])
                                result += "\n==================\n"
                                no = 0
                                for ayat in data["data"]["ayahs"]:
                                    no += 1
                                    result += "\n{}. {}".format(no,ayat['text'])
                                k = len(result)//10000
                                for aa in range(k+1):
                                    sendTextTemplate(to,'{}'.format(result[aa*10000 : (aa+1)*10000]))

                            elif terminal.startswith("murrotal"):
                                try:
                                    sep = text.split(" ")
                                    txt = int(text.replace(sep[0] + " ",""))
                                    if 0 < txt < 115:
                                        if txt not in [2,3,4,5,6,7,9,10,11,12,16,17,18,20,21,23,26,37]:
                                            if len(str(txt)) == 1:
                                                audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(txt) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                            elif len(str(txt)) == 2:
                                                audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(txt) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                            else:
                                                audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(txt) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                        else:
                                            client.sendMessage(to, "The Surah is too long")
                                    else:
                                        client.sendMessage(to, "Holy Qur'an Only have 114 surah :)")
                                except Exception as error:
                                    client.sendMessage(to, "error\n"+str(error))
                                    logError(error)

                            elif terminal == "ayat sajadah":
                                url = requests.get("http://api.alquran.cloud/sajda/quran-uthmani")
                                data = url.json()
                                result = "~[Ayat Sajadah]~"
                                for ayat in data["data"]["ayahs"]:
                                    ayatnya = ayat["text"]
                                    result += "\n{}".format(ayatnya)
                                    result += "\n Surah {}".format(ayat["surah"]["englishName"])
                                result += "\n ~~~~~~ Juz {} ~~~~~~".format(ayat["juz"])
                                sendTextTemplate(to, result)

#===================MEDIA MEME ❂🇮🇩➢
                            elif terminal.startswith("listmeme"):
                              if msg._from in owner:
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "🍀 Daftar Meme Image 🍀\n"
                                    for aa in data["data"]["memes"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                    hasil += " "
                                    client.sendMessage(to,hasil)
                                    client.sendMention(to, "\nJika ingin menggunakan, \nSilahkan ketik:\n\n🍀 Listmeme | urutan\n🍀 Meme text1 | text2 | urutan", [sender])
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        gambar = data["data"]["memes"][num - 1]
                                        hasil = "{}".format(str(gambar["name"]))
                                        client.sendMention(to, "🍀 Meme Image 🍀\nTunggu \nFoto sedang diproses...", [sender])
                                        client.sendMessage(to, hasil)
                                        client.sendImageWithURL(to, gambar["url"])
                                    except Exception as e:
                                        client.sendMessage(to," "+str(e))

                            elif terminal.startswith("meme "):  
                                if msg._from in owner:
                                    code = msg.text.split(" ")
                                    txt = msg.text.replace(code[0] + "/" + " ","")
                                    txt2 = msg.text.replace(txt[0] + "/" + " ","")
                                    naena = "https://api.imgflip.com/"+txt2+".jpg"
                                    try:
                                         start = time.time()
                                         client.sendMessage(to,"🍀Meme Image🍀\nType : Meme Image\nTime taken : %s seconds" % (start))
                                         client.sendImageWithURL(to, naena)
                                    except Exception as error:
                                         sendTextTemplate(to, str(error))

#=================MEDIA WEBSITE ❂🇮🇩➢
                            elif terminal.startswith("ssweb "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://api.site-shot.com//?url={}&width=1280&height=2080&5ba006ea23010.jpg".format(txt)
                                Thread(target=client.sendImageWithURL,args=(to, url,)).start()

#=================== MEDIA TIMELINE ❂🇮🇩➢
                            elif terminal.startswith("linedownload "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                client.sendImageWithURL(to, txt)
                                client.sendVideoWithURL(to, txt)

                            elif terminal.startswith("linepost "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://farzain.com/api/special/line.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                client.sendImageWithURL(to, data["result"])
                                client.sendVideoWithURL(to, data["result"])

#===================MEDIA TIKTOK ❂🇮🇩➢
                            elif terminal.startswith("tiktok"):
                            	def tiktoks():
                            		try:
		                                url = requests.get("https://rest.farzain.com/api/tiktok.php?country=jp&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba&type=json")
		                                data = url.json()
		                                client.sendVideoWithURL(to, data["first_video"])
                            		except:
		                            	client.sendMessage(to, data["result"])
                            	ryn = Thread(target=tiktoks)
                            	ryn.daemon = True
                            	ryn.start()

#============= MEDIA RAMALAN ❂🇮🇩➢
                            elif terminal.startswith("artinama "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://api.eater.site/api/name/?apikey=beta&name={}".format(txt))
                                data = url.json()
                                client.sendMessageWithFooter(to, str(data["result"][0]["name"]))

                            elif terminal.startswith("artimimpi "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://farzain.com/api/mimpi.php?q={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba".format(txt))
                                data = url.json()
                                client.sendMessageWithFooter(to, str(data["result"]))

#================MEDIA YOUTUBE1 ❂🇮🇩➢
                            elif terminal.startswith("ytmp3"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                def yt():
                                    youtubeMp3(to, txt)
                                treding = Thread(target=yt)
                                treding.daemon = True
                                treding.start()

                            elif terminal.startswith("ytmp4"):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                treding = Thread(target=youtubeMp4,args=(to,txt,))
                                treding.daemon = True
                                treding.start()

                            elif cmd.startswith("youtubesearch "):
	                            sep = text.split(" ")
	                            search = text.replace(sep[0] + " ","")
	                            params = {"search_query": search}
	                            with _session as web:
	                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
	                                r = web.get("https://www.youtube.com/results", params = params)
	                                soup = BeautifulSoup(r.content, "html5lib")
	                                ret_ =  "╭───「 Youtube Result 」"
	                                datas = []
	                                for data in soup.select(".yt-lockup-title > a[title]"):
	                                    if "&lists" not in data["href"]:
	                                        datas.append(data)
	                                for data in datas:
	                                    ret_ += "\n-≽[ {} ]".format(str(data["title"]))
	                                    ret_ += "\n-≽https://www.youtube.com{}".format(str(data["href"]))
	                                ret_ += "\n╰───「 {} 」".format(len(datas))
	                                client.sendMessage(to, str(ret_))

                            elif terminal.startswith("youtubemp4 "):
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url="https://www.youtube.com/results?search_query="
                                    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers = mozhdr)
                                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                    x = (yt_links[1])
                                    yt_href =  x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        me = best.url
                                        hasil = ""
                                        title = "Judul [ " + vid.title + " ]"
                                        author = '\n\n•-≽ Author : ' + str(vid.author)
                                        durasi = '\n•-≽ Duration : ' + str(vid.duration)
                                        suka = '\n•-≽ Likes : ' + str(vid.likes)
                                        rating = '\n•-≽ Rating : ' + str(vid.rating)
                                        deskripsi = '\n•-≽ Deskripsi : ' + str(vid.description)
                                    client.sendVideoWithURL(msg.to, me)
                                    client.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                                except Exception as e:
                                    client.sendMessage(msg.to,str(e))

                            elif terminal.startswith("youtubemp3 "):
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url="https://www.youtube.com/results?search_query="
                                    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers = mozhdr)
                                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                    x = (yt_links[1])
                                    yt_href =  x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    bestaudio = vid.getbestaudio()
                                    bestaudio.bitrate
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        shi = bestaudio.url
                                        me = best.url
                                        vin = s.url
                                        hasil = ""
                                        title = "Judul [ " + vid.title + " ]"
                                        author = '\n\n❂⊱• Author : ' + str(vid.author)
                                        durasi = '\n❂⊱• Duration : ' + str(vid.duration)
                                        suka = '\n❂⊱• Likes : ' + str(vid.likes)
                                        rating = '\n❂⊱• Rating : ' + str(vid.rating)
                                        deskripsi = '\n❂⊱• Deskripsi : ' + str(vid.description)
                                    client.sendImageWithURL(to, me)
                                    client.sendAudioWithURL(to, shi)
                                    client.sendMessage(to,title+ author+ durasi+ suka+ rating+ deskripsi)
                                except Exception as e:
                                    client.sendMessage(to,str(e))

                            elif terminal.startswith('ssweb'):
                                sep = msg.text.split(" ")
                                nazri = msg.text.replace(sep[0] + " ","")
                                Thread(target=client.sendImageWithURL(to, 'http://api.screenshotmachine.com/?key=3ae749&dimension=1920x1080&format=jpg&url='+nazri)).start()

                            elif terminal.startswith("drakor"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://api.eater.pw/drakor/{}".format(txt))
                                dat = url.json()
                                drk = "「{}」".format(txt)
                                num = 0
                                for dr in dat["result"]:
                                    num += 1
                                    drk += "\n{}.「Judul」 : {}".format(str(num),str(dr["judul"]))
                                    drk += "\n   「Link」  : {}".format(str(dr["link"]))
                                drk += "\nTotal 「{}」 Drakor".format(str(len(dat["result"])))
                                client.sendReplyMessage(msg_id, to, drk)

#===========MEDIA YOUTUBE2 ❂🇮🇩➢

                            elif terminal.startswith("ytdl "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/yt_download.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                def sendVid():
                                    client.sendAudioWithURL(to, data["urls"][1]["id"])
                                td = Thread(target=sendVid)
                                td.daemon = True
                                td.start()

                            elif terminal.startswith("ytdownload "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/yt_download.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                data = data["urls"][1]["id"]
                                if "\/" in data:
                                	data = data.replace("\/","/")
                                else:
                                	pass
                                zzz = google_url_shorten(data)
                                client.sendMessageMusic(to, title='Youtube', url='line://app/1603138059-k9Egggar?type=video&ocu=https://{}&piu=https://ngebotantipusing.com/hmmk.jpg'.format(zzz))

                            elif terminal.startswith("searchyoutube "):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                cond = txt.split("|")
                                search = cond[0]
                                url = requests.get("http://api.w3hills.com/youtube/search?keyword={}&api_key=86A7FCF3-6CAF-DEB9-E214-B74BDB835B5B".format(search))
                                data = url.json()
                                if len(cond) == 1:
                                    no = 0
                                    result = "╔══[ Youtube Search ]"
                                    for anu in data["videos"]:
                                        no += 1
                                        result += "\n├≽ {}. {}".format(str(no),str(anu["title"]))
                                        result += "\n├≽ {}".format(str(anu["webpage"]))
                                    result += "\n╚══[ Total {} Result ]".format(str(len(data["videos"])))
                                    client.sendMessage(to, result)
                                elif len(cond) == 2:
                                    num = int(str(cond[1]))
                                    if num <= len(data):
                                        search = data["videos"][num - 1]
                                        ret_ = "╔══[ Youtube Info ]"
                                        ret_ += "\n├≽ Channel : {}".format(str(search["publish"]["owner"]))
                                        ret_ += "\n├≽ Title : {}".format(str(search["title"]))
                                        ret_ += "\n├≽ Release : {}".format(str(search["publish"]["date"]))
                                        ret_ += "\n├≽ Viewers : {}".format(str(search["stats"]["views"]))
                                        ret_ += "\n├≽ Likes : {}".format(str(search["stats"]["likes"]))
                                        ret_ += "\n├≽ Dislikes : {}".format(str(search["stats"]["dislikes"]))
                                        ret_ += "\n├≽ Rating : {}".format(str(search["stats"]["rating"]))
                                        ret_ += "\n├≽ Description : {}".format(str(search["description"]))
                                        ret_ += "\n╚══[ {} ]".format(str(search["webpage"]))
                                        client.sendImageWithURL(to, str(search["thumbnail"]))
                                        client.sendMessage(to, str(ret_))

                            elif terminal.startswith("searchimage "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/gambarg.php?id={}&apikey=VBbUElsjMS84rXUO7wRlIwjFm".format(txt))
                                data = url.json()
                                client.sendImageWithURL(to, data["url"])

                            elif terminal.startswith("searchlyric "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                cond = txt.split("|")
                                query = cond[0]
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0"
                                    url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
                                    data = BeautifulSoup(url.content, "html.parser")
                                    result = []
                                    for trackList in data.findAll("ul", {"class":"tracks list"}):
                                        for urlList in trackList.findAll("a"):
                                            title = urlList.text
                                            url = urlList["href"]
                                            result.append({"title": title, "url": url})
                                    if len(cond) == 1:
                                        ret_ = "╔══[ Musixmatch Result ]"
                                        num = 0
                                        for title in result:
                                            num += 1
                                            ret_ += "\n├≽ {}. {}".format(str(num), str(title["title"]))
                                        ret_ += "\n╚══[ Total {} Lyric ]".format(str(len(result)))
                                        ret_ += "\n\nUntuk melihat lyric, silahkan gunakan command {}SearchLyric {}|「number」".format(str(setKey), str(query))
                                        client.sendMessage(to, ret_)
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(result):
                                            data = result[num - 1]
                                            with requests.session() as web:
                                                web.headers["user-agent"] = "Mozilla/5.0"
                                                url = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(data["url"])))
                                                data = BeautifulSoup(url.content, "html5lib")
                                                for lyricContent in data.findAll("p", {"class":"mxm-lyrics__content "}):
                                                    lyric = lyricContent.text
                                                    client.sendMessage(to, lyric)


#===================== BAHAN PERINTAH / PENDUKUNG BOT ===============================================
                            if "/ti/g/" in msg.text.lower():
                                if settings["autoJoinTicket"] == True:
                                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                    links = link_re.findall(text)
                                    n_links = []
                                    for l in links:
                                        if l not in n_links:
                                            n_links.append(l)
                                    for ticket_id in n_links:
                                        group = client.findGroupByTicket(ticket_id)
                                        client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        client.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))

                        elif msg.contentType == 2:
                            if settings["changeDual"] == True:
                                def cvp():
                                    client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/cvp.mp4")
                                    client.sendMessage(to, "Send Pict :)")
                                td = Thread(target=cvp)
                                td.daemon = True
                                td.start()

                        elif msg.contentType == 1:
                            if settings["changeDual"] == True:
                                def change():
                                    pict = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changeDual"] = False
                                    client.updateVideoAndPictureProfile(pict, "LineAPI/tmp/cvp.mp4")
                                    client.sendMessage(to, "Succesfully change video & picture profile")
                                    client.deleteFile(pict)
                                    client.deleteFile("LineAPI/tmp/cvp.mp4")
                                td = Thread(target=change)
                                td.daemon = True
                                td.start()

                            if to in settings["decode"]:
                                generateLink(to, msg_id)

                            if to in settings["watercolor"] == True:
                                uploadFile(msg_id)
                                client.sendImageWithURL(to, 'http://ari-api.herokuapp.com/watercolor?type=2&rancol=on&url={}'.format(urlEncode("https://fahminogameno.life/uploadimage/images/ryngenerate.jpg")))

                            if to in settings["drawink"]:
                            	uploadFile(msg_id)
                            	client.sendImageWithURL(to, 'http://ari-api.herokuapp.com/ink?url='.format(urlEncode("https://fahminogameno.life/uploadimage/images/ryngenerate.png")))

#=========================BAHAN PENDUKUNG IMAGE / FOTO =================================================================
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if settings["addImage"]["status"] == True:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-add.bin".format(str(settings["addImage"]["name"])))
                                    images[settings["addImage"]["name"]] = {"IMAGE":str(path)}
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(msg.to, "Succesfully add Image With Keyword {}".format(str(settings["addImage"]["name"])))
                                    settings["addImage"]["status"] = False                
                                    settings["addImage"]["name"] = ""

                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if settings["changePictureProfile"] == True:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changePictureProfile"] = False
                                    client.updateProfilePicture(path)
                                    client.sendMessage(to, "Berhasil mengubah foto profile")
                                    client.deleteFile(path)

                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if to in settings["changeGroupPicture"]:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cgp.bin".format(time.time()))
                                    settings["changeGroupPicture"].remove(to)
                                    client.updateGroupPicture(to, path)
                                    client.sendMessage(to, "Berhasil mengubah foto group")
                                    client.deleteFile(path)

                            if msg.toType == 2:
                                if settings["changeCover"] == True:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cv.bin".format(time.time()))
                                    settings["changeCover"] = False
                                    client.updateProfileCover(path)
                                    client.sendMessage(to, "Berhasil mengubah cover profile")
                                    client.deleteFile(path)

                        elif msg.contentType == 2:
                            if settings["changeVpProfile"] == True:
                                path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cvp.mp4".format(time.time()))
                                settings["changeVpProfile"] = False
                                changeVideoAndPictureProfile(path)
                                client.sendMessage(to, "Berhasil mengubah video profile")
                                client.deleteFile(path)

#=====================BAHAN PENDUKUNG DETEKSI STICKER=================================================
                        elif msg.contentType == 7:
                            if settings["checkSticker"] == True:
                                stk_id = msg.contentMetadata['STKID']
                                stk_ver = msg.contentMetadata['STKVER']
                                pkg_id = msg.contentMetadata['STKPKGID']
                                ret_ = "╔══[ Sticker Info ]"
                                ret_ += "\n├≽ STICKER ID : {}".format(stk_id)
                                ret_ += "\n├≽ STICKER PACKAGES ID : {}".format(pkg_id)
                                ret_ += "\n├≽ STICKER VERSION : {}".format(stk_ver)
                                ret_ += "\n├≽ STICKER URL : line://shop/detail/{}".format(pkg_id)
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))

#==================BAHAN PENDETEKSI STICKER MODE TEMPLATE=================================================
                            if to in settings["sticker"]:
                                if 'STKOPT' in msg.contentMetadata:
                                    stk_id = msg.contentMetadata['STKID']
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(stk_id)
                                else:
                                    stk_id = msg.contentMetadata['STKID']
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                                data = {
                                    "type": "template",
                                    "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                    "template": {
                                        "type": "image_carousel",
                                        "columns": [
                                            {
                                                "imageUrl": "{}".format(stc),
                                                "size": "full", 
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "http://instagram.com/xeberlhyn12345"
                                                }
                                            }
                                        ]
                                    }
                                }
                                client.postTemplate(to, data)

#===================BAHAN PENDUKUNG STICKER BIASA========================================================
                            if msg.toType == 2:    
                              if msg._from in admin:
                                if settings["addSticker"]["status"] == True:
                                    stickers[settings["addSticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKVER":msg.contentMetadata['STKVER'], "STKPKGID":msg.contentMetadata["STKPKGID"]}
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessageWithFooter(to, "Succesfully add sticker with keyword >> {} ".format(str(settings["addSticker"]["name"])))
                                    settings["addSticker"]["status"] = False                
                                    settings["addSticker"]["name"] = ""

#======================AN PENDUKUNG STICKER TEMPLATE==============================================
                            if msg.toType == 2:
                              if msg._from in admin:
                                if settings["addStickertemplate"]["statuss"] == True:
                                    stickerstemplate[settings["addStickertemplate"]["namee"]] = {"STKID":msg.contentMetadata["STKID"],"STKVER":msg.contentMetadata['STKVER'], "STKPKGID":msg.contentMetadata["STKPKGID"]}
                                    f = codecs.open("stickertemplate.json","w","utf-8")
                                    json.dump(stickerstemplate, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessageWithFooter(to, "Succesfully add sticker template with keyword >> {} ".format(str(settings["addStickertemplate"]["namee"])))
                                    settings["addStickertemplate"]["statuss"] = False                
                                    settings["addStickertemplate"]["namee"] = ""

#=========================BAHAN PENDUKUNG MP3========================================================
                            if msg.contentType == 3:
                              if msg._from in admin:
                                if settings["Addaudio"]["status"] == True:
                                    path = client.downloadObjectMsg(msg.id)
                                    audios[settings["Addaudio"]["name"]] = str(path)
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                                    settings["Addaudio"]["status"] = False
                                    settings["Addaudio"]["name"] = ""

#=====================BAHAN PENDUKUNG BAGIAN CONTACT====================================================
                        elif msg.contentType == 13:
                            if settings["checkContact"] == True:
                                try:
                                    contact = client.getContact(msg.contentMetadata["mid"])
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                    ret_ = "╔══[ Details Contact ]"
                                    ret_ += "\n├≽ Nama : {}".format(str(contact.displayName))
                                    ret_ += "\n├≽ MID : {}".format(str(msg.contentMetadata["mid"]))
                                    ret_ += "\n├≽ Bio : {}".format(str(contact.statusMessage))
                                    ret_ += "\n├≽ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                    ret_ += "\n├≽ Gambar Cover : {}".format(str(cover))
                                    ret_ += "\n╚══[ Finish ]"
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus)))
                                    client.sendMessage(to, str(ret_))
                                except:
                                    client.sendMessage(to, "Kontak tidak valid")

                                if settings["delFriend"] == True:
                                    client.deleteContact(msg.contentMetadata["mid"])
                                    client.sendReplyMention(msg_id, to, "Udh Euyyy @!", [sender])

                                if settings["cloneContact"] == True:
                                    client.cloneContactProfile(msg.contentMetadata["mid"])
                                    client.sendMessage(to, "Succes clone profile")
                                    settings["cloneContact"] = False

                                if settings["contactBan"] == True:
                                    ban = msg.contentMetadata["mid"]
                                    hey = client.getContact(ban).displayName
                                    settings["blackList"][ban] = True
                                    f=codecs.open('setting.json','w','utf-8')
                                    json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    settings["contactBan"] = False
                                    client.sendMessage(to, "Succesfully add {} to Blacklist".format(hey))
                                else:
                                    if settings["contactBan"] == True:
                                        if settings["blackList"][ban] == True:
                                            client.sendMessage(to, "The Contact has been BANNED !!!")

                                if settings["unbanContact"] == True:
                                    ban = msg.contentMetadata["mid"]
                                    hey = client.getContact(ban).displayName
                                    del settings["blackList"][ban]
                                    f=codecs.open('setting.json','w','utf-8')
                                    json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    client.sendMessage(to, "Succesfully Del {} in Blacklist".format(hey))
                                    settings["unbanContact"] = False
                                    if msg.contentMetadata["mid"] not in settings["blackList"]:
                                        client.sendMessage(to, "The Contact Isn't in Banned List")
            except Exception as error:
                logError(error)

#=============================================================================================
        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                tatan = settings["tatan"]
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        if msg.contentType == 0:
                            client.sendFakeMessage(to, text,sender)
                        elif msg.contentType == 1:
                            path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-mimic.bin".format(time.time()))
                            client.sendImage(to, path)
                            client.deleteFile(path)
                    if msg.contentType == 0:
                        if settings["autoRead"] == True:
                            client.sendChatChecked(to, msg_id)
                        if sender not in clientMid:
                            if msg.toType != 0 and msg.toType == 2:

#=============================AUTO RESPON===================================================
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    bobb = "u507008f7d7eff80a48c39045e028b86f"
                                    group = client.getGroup(to)
                                    for mention in mentionees:
                                        if clientMid in mention["M"]:
                                            if settings["autoRespon"] == True:
                                                contact = client.getProfile()
                                                mids = [contact.mid]
                                                status = client.getContact(sender)               
                                                data = {
                                                        "type": "flex",
                                                        "altText": "zhr тeaм",
                                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    },
    "header": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "{}".format(status.displayName),
            "size": "xl",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "align": "center"            
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": settings["autoResponMessage"],
                "size": "xs",
                "margin": "none",
                "color": "#00FF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#6A5ACD",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "Φ Cʜᴀᴛ ᴛᴏ ᴄƦᴇᴀᴛᴏƦ Φ",
                  "uri": "https://line.me/ti/p/~maul-703",
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#4682B4",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "url",
                  "label": "ᴅᴏᴡɴ",
                  "url": "https://ibb.co/XzMzpy9][img]https://i.ibb.co/XzMzpy9/1572168015470.jpg",
              }
          }]
      }]
  },
  "header": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "zhr тeaм",
                "size": "xl",
                "weight": "bold",
                "align": "center",            
                "color": "#FFD700",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                                client.postTemplate(to, data)
                                            break

                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    bobb = "u507008f7d7eff80a48c39045e028b86f"
                                    group = client.getGroup(to)
                                    for mention in mentionees:
                                        if clientMid in mention["M"]:
                                            if settings["autoRes"] == True:
                                                contact = client.getProfile()
                                                mids = [contact.mid]
                                                status = client.getContact(sender)               
                                                cover = client.getProfileCoverURL(sender)
                                                warna1 = ("#00ffff","#9933ff","#0033CC","#00ff33","#cc00ff","#ff0000","#003333")
                                                warnanya1 = random.choice(warna1)
                                                data = {
                                                        "type": "flex",
                                                        "altText": "TUKANG TAG",
                                                        "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#ff0000",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.gifer.com/Ui00.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.captechu.edu/sites/default/files/cybersecurity_assessment_framework_detect.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=u9e7b95e0fe30d1b8a23a6c83e73a5d8f",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "RESPON", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/60175432319",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~maul-703",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/__TRSC_OLALA__",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "鈴�"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#93ff00",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "128px",
"backgroundColor": "#4b4b4b",
"offsetStart": "80px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "{}".format(status.displayName),
"weight": "bold",
"color": "#ffff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
#"backgroundColor": "#000000",
"offsetStart": "20px",
"height": "18px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "IA KK AKU DISINI KOK",
"weight": "bold",
"color": "#ff0000",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
#"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "121px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                                                client.postTemplate(to, data)
                                            break

#=======================SIDER MEMBER======================================================

#======================================================================================================================
                        if msg.toType == 0:
                          if settings["autoReply"] == True:
                            if sender in autoanswer:
                              client.sendMessage(sender, settings["autoAnswerMessage"])
            except Exception as error:
                logError(error)

        if op.type == 25 or op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                tatan = settings["tatan"]
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                        if text.lower() == tatan:
                          if msg._from in owner or admin:
                            if msg.toType == 2:
                                group = client.getGroup(to)
                                group.preventedJoinByTicket = False
                                client.updateGroup(group)
                                groupUrl = client.reissueGroupTicket(to)
                                baby = ["ud3cc3d4379fa2254157225b2f7353644","u40b168f75fd0686af355104a05239d78"]
                                for titit in baby:
                                    client.sendMessage(titit, "https://line.me/R/ti/g/{}".format(groupUrl))
                        else:

                            for txt in textsadd:
                                if text.lower() == txt:
                                    img = textsadd[text.lower()]['CHAT']
                                    group = client.getGroup(to)
                                    midMembers = [contact.mid for contact in group.members]
                                    data = random.choice(midMembers)
                                    client.sendMessage(to, "{}".format(img), contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(data).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(data).pictureStatus)})

                            for immg in images:
                                if text.lower() == immg:
                                    img = images[text.lower()]["IMAGE"]
                                    client.sendImage(to, img)

                            for sticker in stickers:
                                if text.lower() in sticker:
                                   sid = stickers[text.lower()]["STKID"]
                                   spkg = stickers[text.lower()]["STKPKGID"]
                                   client.sendReplySticker(msg_id, to, spkg, sid)

                            for stctemplate in stickerstemplate:
                                if text.lower() == stctemplate:                                  
                                    stk_id = stickerstemplate[text.lower()]["STKID"]                                    
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "{}".format(stc),
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://instagram.com/xeberlhyn12345"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)                                   
            except Exception as error:
                logError(error)

        if op.type == 65:
            if settings["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = client.getGroup(at)
                                People = client.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  " GAMBAR DI HAPUS "
                                ry = str(People.displayName)
                                pesan = ''
                                pesan2 = pesan+"{} \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':People.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                data = {
                                        "type": "flex",
                                        "altText": "ZH,BOTS",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    },
    "header": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "url": "https://i.ibb.co/JtqYf3t/AW1238502-06.gif",
            "type": "image"            
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": xpesan,
                "align": "center",            
                "size": "xs",
                "margin": "none",
                "color": "#00FFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Pengirim : {}".format(str(People.displayName)),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Nama Grup : {}".format(str(ginfo.name)),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "header": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "UNSEND",
                "size": "xl",
                "weight": "bold",
                "align": "center",            
                "color": "#00008C",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 1,
              "style": "primary",
              "color": "#0000CC",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "https://line.me/ti/p/~maul-703"
              }
          }]
      }]
  }
}
}
                                client.postTemplate(at, data)
                                client.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = client.getGroup(at)
                                People = client.getContact(msg_dict[msg_id]["from"])
                                seb =  "PESAN TEXT/STICKER DI HAPUS "
                                seber = "📓 Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                data = {
                                        "type": "flex",
                                        "altText": "zhr тeaм",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000A0"
    },
    "footer": {
      "backgroundColor": "#000000"
    },
    "header": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(str(People.pictureStatus)),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "url": "https://i.ibb.co/JtqYf3t/AW1238502-06.gif",
            "type": "image"            
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": seb,
                "align": "center",            
                "size": "xs",
                "margin": "none",
                "color": "#00FFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Pengirim : {}".format(str(People.displayName)),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Nama Grup : {}".format(str(ginfo.name)),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))),
                "size": "xs",
                "margin": "none",
                "color": "#ffffff",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": seber,
                "size": "xs",
                "margin": "none",
                "color": "#FF7F00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "header": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "UNSEND",
                "size": "xl",
                "weight": "bold",
                "align": "center",            
                "color": "#00008C",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#0000CC",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "https://line.me/ti/p/~maul-703"
              }
          }]
      }]
  }
}
}
                                client.postTemplate(at, data)
                                client.sendImage(at, msg_dict[msg_id]["data"])
                        del msg_dict[msg_id]
                except Exception as error:
                    logError(error)

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = client.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n🔭 Sticker ID : {}".format(stk_id)
                   ret_ += "\n🔭 Sticker Version : {}".format(stk_ver)
                   ret_ += "\n🔭 Sticker Package : {}".format(pkg_id)
                   ret_ += "\n🔭 Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = client.downloadFileURL(data)
                            msg_dict[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                                                  
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if settings["sticker"] == True:
                    msg.contentType = 0
                    client.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if settings["contact"] == True:
                    msg.contentType = 0
                    client.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = client.getContact(msg.contentMetadata["mid"])
                        path = client.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        client.sendMessage(msg.to,"📷 Nama : " + msg.contentMetadata["displayName"] + "\n📷 MID : " + msg.contentMetadata["mid"] + "\n📷 Status : " + contact.statusMessage + "\n📷 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        client.sendImageWithURL(msg.to, image)

    except Exception as error:
         logError(error)


#==========================TERIMAKASIH- SALAM TEAM THE PEOPLE======================================
if __name__=="__main__":
    while True:
        try:
            delExpire()
            ops = clientPoll.singleTrace(count=50)
            if ops is not None:
                for op in ops:
                    clientPoll.setRevision(op.revision)
                    loop.run_until_complete(clientBot(op))
        except Exception as e:
            print(e)
            traceback.print_tb(e.__traceback__)
