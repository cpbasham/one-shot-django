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

def get_items():
	url = full_url("/api/lol/static-data/%s/v1.2/item" %REGION,
					"version=%s" %ITEM_DD_VERSION,
					"itemListData=all")
	print "URL: " + url
	data = get(url)
	return __format_items(data)

def __format_items(data):
	return data["data"]
	# data = data["data"].map {|key, value| value}
	# data.sort! { |a, b| a["name"] <=> b["name"] }

# def get_item(id):
# 	url = full_url("/api/lol/static-data/na/v1.2/item/#{id}",
# 	              "version=#{item_dd_version}",
# 	              "itemData=all")
# 	data = get(url)


# # Temp function til API working correctly
# def item_availability:
# 	data = get("http://ddragon.leagueoflegends.com/cdn/5.14.1/data/en_US/map.json")
# 	data = data["data"]
# 	data = {TT: data["10"]["UnpurchasableItemList"], SR: data["11"]["UnpurchasableItemList"]}
