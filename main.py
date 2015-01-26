import urllib
import urllib2
import json
from datetime import datetime
from dateutil import tz

url = 'http://www.directv.com/entertainment/data/guideScheduleSegment.json.jsp'
values = {'numchannels':'1', 'channelnum':'500'}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)

page = response.read()
#print page
guideData = json.loads(page)

tempChNum = 0
for x in range(0,len(guideData['channels'])):
	if guideData['channels'][x]['chNum'] != tempChNum:
		tempChNum = chNum = guideData['channels'][x]['chNum']
		chCall = guideData['channels'][x]['chCall']
		swTitle = guideData['channels'][x]['schedules'][0]['prTitle']
		upNext = guideData['channels'][x]['schedules'][1]['prTitle']
		startTime = datetime.strptime(guideData['channels'][x]['schedules'][0]['prAir'][:16], '%Y-%m-%dT%H:%M').replace(tzinfo=tz.tzutc()).astimezone(tz.tzlocal()).strftime('%I:%M%p')
		print str(chNum) + ': ' + chCall + ' - (' + startTime + ') ' + swTitle #+ ' -- Up Next: ' + upNext

#print '2015-01-26T20:00:00.000+0000'[:16]
# showTime = datetime.strptime('2015-01-26T20:00:00.000+0000'[:16], '%Y-%m-%dT%H:%M')

# print showTime.time().strftime('%I:%M%p')
#datatime.striptime(guideData['channels'][0]['schedules'][0]['prAir'], 
