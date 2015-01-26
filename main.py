import urllib
import urllib2
import json

url = 'http://www.directv.com/entertainment/data/guideScheduleSegment.json.jsp'
values = {'numchannels':'20', 'channelnum':'1'}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)

page = response.read()
#print page
guideData = json.loads(page)

for x in range(0,len(guideData['channels'])):
	if 'chHd' in guideData['channels'][x]:
		chNum = guideData['channels'][x]['chNum']
		chCall = guideData['channels'][x]['chCall']
		swTitle = guideData['channels'][x]['schedules'][0]['prTitle']
		print str(chNum) + ': ' + chCall + ' - ' + swTitle

#print guideData['channels'][1]