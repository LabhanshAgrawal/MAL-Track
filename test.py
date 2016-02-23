import untangle
obj = untangle.parse('http://myanimelist.net/malappinfo.php?u=labho&status=all&type=anime')
target = open('./list', 'w')
for x in obj.myanimelist.anime:
	target.write(x.series_animedb_id.cdata.encode('utf8') + ' ' + x.series_title.cdata.encode('utf8') + '\n')
