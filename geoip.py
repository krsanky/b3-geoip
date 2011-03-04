#
# GeoIP Plugin for BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2010 <Your Name Here>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# Changelog:
#

__version__ = '0.0.1'
__author__  = 'Paul Wisehart'

import b3
import b3.events
import b3.plugin


class GeoipPlugin(b3.plugin.Plugin):

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

    # Register commands
    # something needs help here:
    self._adminPlugin.registerCommand(self, 'helloworld', 1, self.cmd_helloWorld, 'helloworld')

    # Register our events
    self.verbose('Registering events')
    self.registerEvent(b3.events.EVT_CLIENT_AUTH)

    self.debug('Started')


  def onLoadConfig(self):
    # load our settings
    self.verbose('Loading config')


  def onEvent(self, event):
    """
    Handle intercepted events
    """
    if event.type == b3.events.EVT_CLIENT_AUTH:
        helloWorld(event.client)
        pass
    else:
      self.dumpEvent(event)


  def helloWorld(self, client):
    """
    Say 'Hello World!' to a client
    """
    client.console.say('Hello World!')
    return

  def cmd_helloWorld(self, data, client, cmd=None):
    """
    - Say 'Hello World!' to yourself
    """
    self.helloWorld(client)
    return
