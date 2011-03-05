# GeoIP Plugin for BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2010 Paul Wisehart
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

__version__ = '0.0.1'
__author__  = 'Paul Wisehart'

import GeoIP

import b3
import b3.events
import b3.plugin

class GeoipPlugin(b3.plugin.Plugin):
    """
    """
    def startup(self):
        """
        Initialize plugin settings
        """
        # get the admin plugin so we can register commands
        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            # something is wrong, can't start without admin plugin
            self.error('Could not find admin plugin')
            return False

        #get a geo obj.:
        #gi = GeoIP.open("/usr/local/share/GeoIP/GeoIPCity.dat",GeoIP.GEOIP_STANDARD)
        #gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
        self.geoip = GeoIP.open(self._geoip_dat, GeoIP.GEOIP_MEMORY_CACHE)


        # Register commands
        # something needs help here:
        #def registerCommand(self, plugin, command, level, handler, alias=None, secretLevel=None):
        self._adminPlugin.registerCommand(self, 'geoip', 2, self.cmd_geoip, 'gi')

        # Register our events
        self.verbose('Registering events')
        self.registerEvent(b3.events.EVT_CLIENT_AUTH)

        self.debug('Started')


    def onLoadConfig(self):
        """load our settings"""
        self.verbose('Loading config')
        #self.config.get('settings', 'levels')
        # <configuration plugin="tk">
        # 	<settings name="settings">
        # 		<set name="levels">0,1,2,20,40</set>
        self._geoip_dat = self.config.get('settings', 'geoip_dat')

    def onEvent(self, event):
        """
        Handle intercepted events
        """
        if event.type == b3.events.EVT_CLIENT_AUTH:
            #helloWorld(event.client)
            pass
        else:
            self.dumpEvent(event)

    def get_geo_record(self, client):
        """
        gi.record_by_addr("**.***.**.***")
        {'area_code': 603,
        'city': 'New London',
        'country_code': 'US',
        'country_code3': 'USA',
        'country_name': 'United States',
        'dma_code': 506,
        'latitude': 43.437999725341797,
        'longitude': -72.005996704101562,
        'metro_code': 506,
        'postal_code': '03257',
        'region': 'NH',
        'region_name': 'New Hampshire',
        'time_zone': 'America/Chicago'}
        """
        r = self.geoip.record_by_addr(client.ip)
        return r['region_name']

    def cmd_geoip(self, data, client, cmd=None):
        """
        given a player slot number, return the
        country code of their ip
        """
        self.debug('data:%s' % data,)
        #self.helloWorld(client)
        client.console.say('hello: %s %s' % (client.ip, self._geoip_dat))
        client.console.say('what?: %s' % self.get_geo_record(client))

        return
