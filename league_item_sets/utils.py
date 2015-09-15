from django.conf import settings
import requests

def full_url(url, *params):
	url += "?"
	for param in params:
		url += param + "&"
	return LEAGUE_API_HEAD + url + "api_key=" + str(API_KEY)

def get(url):
	response = requests.get(url)
	return response.json()

LEAGUE_API_HEAD = "https://global.api.pvp.net"
API_KEY = settings.LEAGUE_API_KEY
REGION = "na"
REALM_DATA = get(full_url("/api/lol/static-data/%s/v1.2/realm" %REGION))
DD_UL_HEAD = REALM_DATA["cdn"]
ITEM_DD_VERSION = REALM_DATA["n"]["item"]
ITEM_SPRITE_HEAD = "%s/%s/img/sprite" %(DD_UL_HEAD, REALM_DATA["n"]['item'])

def get_items():
	url = full_url("/api/lol/static-data/%s/v1.2/item" %REGION,
					"version=%s" %ITEM_DD_VERSION,
					"itemListData=all")
	data = get(url)
	return __format_items(data)

def __format_items(data):
	return data["data"]
	# data = data["data"].map {|key, value| value}
	# data.sort! { |a, b| a["name"] <=> b["name"] }

# # Temp function til API working correctly
def get_item_availability():
	data = get("http://ddragon.leagueoflegends.com/cdn/5.14.1/data/en_US/map.json")
	data = data["data"]
	data = {"TT": data["10"]["UnpurchasableItemList"], "SR": data["11"]["UnpurchasableItemList"]}
	return data