import Foundation
import objc
import AppKit
import sys
import requests
import time

NSUserNotification = objc.lookUpClass('NSUserNotification')
NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')

# Mark Pokemon you want alerts for as True and those you do not
# want to be alerted about as False

# TODO add Nidoran - handle symbols
pokemonList = {
"Bulbasaur": False, 
"Ivysaur": False, 
"Venusaur": True,
"Charmander": True,
"Charmeleon": True,
"Charizard": True,
"Squirtle": True,
"Wartortle": True,
"Blastoise": True,
"Caterpie": False,
"Metapod": False,
"Butterfree": False,
"Weedle": False,
"Kakuna": False,
"Beedrill": False,
"Pidgey": False,
"Pidgeotto": False,
"Pidgeot": False,
"Rattata": False,
"Raticate": False,
"Spearow": False,
"Fearow": False,
"Ekans": False,
"Arbok": False,
"Pikachu": True,
"Raichu": True,
"Sandshrew": True,
"Sandslash": True,
"Nidorina": True,
"Nidoqueen": True,
"Nidorino": True,
"Nidoking": True,
"Clefairy": True,
"Clefable": True,
"Vulpix": True,
"Ninetales": True,
"Jigglypuff": True,
"Wigglytuff": True,
"Zubat": False,
"Golbat": False,
"Oddish": True,
"Gloom": True,
"Vileplume": True,
"Paras": False,
"Parasect": False,
"Venonat": True,
"Venomoth": True,
"Diglett": True,
"Dugtrio": True,
"Meowth": True,
"Persian": True,
"Psyduck": True,
"Golduck": True,
"Mankey": True,
"Primeape": True,
"Growlithe": True,
"Arcanine": True,
"Poliwag": True,
"Poliwhirl": True,
"Poliwrath": True,
"Abra": True,
"Kadabra": True,
"Alakazam": True,
"Machop": True,
"Machoke": True,
"Machamp": True,
"Bellsprout": True,
"Weepinbell": True,
"Victreebel": True,
"Tentacool": True,
"Tentacruel": True,
"Geodude": True,
"Graveler": True,
"Golem": True,
"Ponyta": True,
"Rapidash": True,
"Slowpoke": True,
"Slowbro": True,
"Magnemite": True,
"Magneton": True,
"Farfetch'd": True,
"Doduo": False,
"Dodrio": False,
"Seel": True,
"Dewgong": True,
"Grimer": True,
"Muk": True,
"Shellder": True,
"Cloyster": True,
"Gastly": True,
"Haunter": True,
"Gengar": True,
"Onix": True,
"Drowzee": True,
"Hypno": True,
"Krabby": True,
"Kingler": True,
"Voltorb": True,
"Electrode": True,
"Exeggcute": True,
"Exeggutor": True,
"Cubone": True,
"Marowak": True,
"Hitmonlee": True,
"Hitmonchan": True,
"Lickitung": True,
"Koffing": True,
"Weezing": True,
"Rhyhorn": True,
"Rhydon": True,
"Chansey": True,
"Tangela": False,
"Kangaskhan": True,
"Horsea": False,
"Seadra": False,
"Goldeen": False,
"Seaking": False,
"Staryu": False,
"Starmie": False,
"Mr. Mime": True,
"Scyther": True,
"Jynx": True,
"Electabuzz": True,
"Magmar": True,
"Pinsir": False,
"Tauros": False,
"Magikarp": False,
"Gyarados": True,
"Lapras": True,
"Ditto": True,
"Eevee": True,
"Vaporeon": True,
"Jolteon": True,
"Flareon": True,
"Porygon": True,
"Omanyte": True,
"Omastar": True,
"Kabuto": True,
"Kabutops": True,
"Aerodactyl": True,
"Snorlax": True,
"Articuno": True,
"Zapdos": True,
"Moltres": True,
"Dratini": True,
"Dragonair": True,
"Dragonite": True,
"Mewtwo": True,
"Mew": True}

# The lat/lon bounds of the area you want to watch
bounds = '40.740504,-74.004287,40.741496,-74.001713'

def notify(title, subtitle, info_text, delay=0, sound=False, userInfo={}):
  notification = NSUserNotification.alloc().init()
  notification.setTitle_(title)
  notification.setSubtitle_(subtitle)
  notification.setInformativeText_(info_text)
  notification.setUserInfo_(userInfo)
  if sound:
      notification.setSoundName_("NSUserNotificationDefaultSoundName")
  notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))
  NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)

def getData():
  r = requests.get('https://skiplagged.com/api/pokemon.php?bounds=' + bounds)
  print r.json()["pokemons"]

  for pokemon in r.json()["pokemons"]:
    name = pokemon["pokemon_name"]
    if pokemonList[name]:
      lat = str(pokemon["latitude"])
      lon = str(pokemon["longitude"])

      despawn_time = time.strftime('%Y-%m-%d %I:%M:%S', time.localtime(pokemon["expires"]))

      notify(name, lat + "," + lon, "Despawns at " + despawn_time, sound=True)

getData();
