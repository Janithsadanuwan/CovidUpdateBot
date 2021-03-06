from telethon import TelegramClient, events
import json
import requests

APP_ID=8064991 #my.telegram.org
APP_HASH='9c1ef35f4339c2153f3f6254eee60691' #my.telegram.org
BOTT='5052451772:AAHw5IxdCTRJCNYI4HfQcV5LbWXl4zHxfSc'#@botfather

bot = TelegramClient('bot', APP_ID, APP_HASH).start(bot_token=BOTT)



def staat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo": "https://telegra.ph/file/50c08ca1f3b851a09b960.jpg",
    "caption": "Get instant access to Corona in Sri Lanka π .  Automatically retrieve the latest corona information after adding it to the @janithsbots Group π¦  . Developer @janith_sadanuwan.  ",
    "parse_mode": "HTML",
    "reply_markup": {
        "inline_keyboard": [
            [
                {
                    "text": " π» Youtube π»  ",
                    "url": "https://www.youtube.com/c/janithsadanuwan"
                }, 
                {
                    "text": " π Channel π ",
                    "url": "https://t.me/janithsbots" 
                 }, 
                {
                            
                  "text": " π·Add To Groupπ·  ",
                    "url": "http://t.me/covid19lkbot?startgroup=botstart"
                }
            ]
        ]
    }
}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)

def staa():
    r = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
    jsondata = json.loads(r.text)
    update_date_time    = str(jsondata['data']['update_date_time'])
    local_new_cases     = str(jsondata['data']['local_new_cases'])
    local_active_cases  = str(jsondata['data']['local_active_cases'])
    local_total_cases   = str(jsondata['data']['local_total_cases'])
    local_deaths        = str(jsondata['data']['local_deaths'])
    local_recovered     = str(jsondata['data']['local_recovered'])
    local_total_number_of_individuals_in_hospitals = str(jsondata['data']['local_total_number_of_individuals_in_hospitals'])
    global_new_cases    = str(jsondata['data']['global_new_cases'])
    global_total_cases  = str(jsondata['data']['global_total_cases'])
    global_deaths       = str(jsondata['data']['global_deaths'])
    global_new_deaths   = str(jsondata['data']['global_deaths'])
    global_recovered    = str(jsondata['data']['global_recovered'])

    textt = str(
                    '<b>CURRENT SITUATION</b>' + '\n' + '\n' + '<b>' +
                    update_date_time + ' now </b>' + '\n' + '\n' +
                    '<b>π±π° Situation in Sri Lanka</b>' + '\n' + '\n'  +
                    'π€ Number of confirmed patients (cumulative) = ' + '<code>' +
                    local_total_cases + '</code>' + '\n' +
                    'π€ Number of patients receiving treatment = ' + '<code>' + local_active_cases + '</code>' +
                    '\n' + 'π· Number of new patients = ' + '<code>' + local_new_cases + '</code>' +
                    '\n' +
                    'π₯ Persons currently under investigation in hospitals = ' + '<code>' +
                    local_total_number_of_individuals_in_hospitals +  '</code>' + '\n' +
                    'π The number of people who have recovered and left = ' + '<code>' + local_recovered + '</code>' + 
                    '\n' + 'β° Number of deaths = ' + '<code>'  + local_deaths + '</code>' + '\n' +
                    '\n' + '<b>π Worldwide status</b>' + '\n' +
                    '\n' + 'π€ Number of confirmed patients (cumulative) = ' '<code>'  +
                    global_total_cases + '</code>' + '\n' + 'π· Number of new patients = ' '<code>'  +
                    global_new_cases + '</code>' + '\n' + 'β° Number of deaths = ' '<code>'  +
                    global_deaths + '</code>' + '\n' + 'π Healed number = ' '<code>'  +
                    global_recovered + '</code>' + '\n' + '\n' + '\n' +
                    'β All information is provided by the government and reputable sources' + '\n' +
                    '~ @janithsbots π±π° ~')
    return textt


def sta():
         r = requests.get(f"https://corona.lmao.ninja/v2/countries/{variabla}").json()
         reply_text = f"**ΰΆ»ΰΆ§ {r['country']} π¦ **\nπ€ Number of confirmed patients (cumulative) = {r['cases']:,}\nπ· Number of new patients= {r['todayCases']:,}\nβ° Number of deaths = {r['deaths']:,}\nβ° New death toll= {r['todayDeaths']:,}\nπ Healed number =  {r['recovered']}"
         message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)



@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    staat(event.original_update.message.peer_id.user_id)
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/corona'))
async def corona(event):
    await event.respond(staa(),parse_mode='html')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/corona {variabla}'))
async def corona(event):
    await event.respond(sta(),parse_mode='MARKDOWN')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/help'))
async def help(event):
    await event.respond('This Is Covid 19 Update Botπ±π° Developer - @janith_sadanuwan π­Use the /corona command to view the latest corona newsπ» ')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
   
