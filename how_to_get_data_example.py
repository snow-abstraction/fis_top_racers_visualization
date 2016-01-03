import requests

r = requests.get("""https://data.fis-ski.com/global-links/statistics/overview-top-ranked-in-all-races.html?place=&season=2016&sector=CC&nation_place=&gender=L&category=WC&nbr=13&nation_comp=&discipline=ALL&Submit=Search""")

f = open("ladies2016.txt", "w")
f.write(r.text.encode("utf-8"))
f.close()
