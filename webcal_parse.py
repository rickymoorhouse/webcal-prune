import random
import string
import os
import cherrypy
from ics import Calendar
from urllib2 import urlopen

class CalendarPruner(object):
    @cherrypy.expose
    def index(self, calendar=None, keyword=None, find="", replacement=None, t=0):
        """ Retrieve calendar, reduce to events matching keyword and apply find/replace """
        if calendar:
            if t == 0:
                cherrypy.response.headers['Content-Type'] = 'text/calendar'
            else:
                cherrypy.response.headers['Content-Type'] = 'text/plain'
            new_cal = Calendar()
            calendar = calendar.replace('webcal','http')
            c = Calendar(urlopen(calendar).read().decode('iso-8859-1'))
            for event in c.events:
                if keyword in event.name:
                    if replacement:
                        event.name = event.name.replace(find, replacement)
                    new_cal.events.append(event)
            return new_cal
        else:
            return """
<!DOCTYPE html>
<html>
<body>
<h1>Webcal pruner</h1>
Required parameters: calendar (ics url) and keyword (events to find)
<h2>Parameters</h2>
<form method="GET">
<input type="hidden" name="t" value="1" /><dl>
<dt>calendar</dt>
<dd>webcal url to calendar</dd>
<dd><input type="text" name="calendar" /></dd>
<dt>keyword</dt>
<dd>Filter to events containing this in the name</dd>
<dd><input type="text" name="keyword" /></dd>
<dt>find (optional)</dt>
<dd>Find this string in event names and replace with <em>replacement</em></dd>
<dd><input type="text" name="find" /></dd>
<dt>replacement (optional)</dt>
<dd>Replace found string <em>find</em> with this string in the event name</dd>
<dd><input type="text" name="replacement" /></dd>
<button type="submit">Get calendar</button>
</form>
"""

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    _port = int(os.getenv('PORT', 8080))
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': _port,})
    cherrypy.quickstart(CalendarPruner(), '/',)
