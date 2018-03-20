import urllib
import flickrapi
import pandas as pd

api_key = u'5905e45c80665dfe86f7ad72d3ab2823'
api_secret = u'77fea4e0f44c3ab8'

dp = pd.read_csv('image_data.csv')
photo_id = dp.id

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

for pic_id in photo_id[2794:]:
	try: 
		sets = flickr.photos.getSizes(photo_id = pic_id)
	except:
		continue
	list1 = sets['sizes']['size']
	for url in list1:
		if url['label'] == 'Large':
			print url['source']
			f = open(str(pic_id)+'.jpg','wb')
			f.write(urllib.urlopen(url['source']).read())
			f.close()
