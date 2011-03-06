I wrote a GeoIP plugin.
It uses the GeoIP python library from maxmind http://www.maxmind.com/app/python

So you have to install that.

then:
!geoip <player>
will spit out
city, region_name, country_name

I have it on github:
https://github.com/krsanky/b3-geoip

PS. There is a python only geoip library that I'm pretty sure I could get to work
if installing the Maxmind one is not an option.


======== How to Install ============

1. install Maxmind's GeoIP stuff.
http://www.maxmind.com/app/python
Both the C library and the python bindings.
(some linuxes prob. have packages for them.)

2. Get the free City data file:
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
gunzip it and put it somewhere.
Mine is at /usr/share/GeoIP/

3. Put the full path to the above file into plugin_geoip.xml

4. Put geoip.py in your extplugins folder.
5. Put plugin_geoip.xml into the extplugins/conf folder.

6. Add   <plugin config="/data/b3/extplugins/conf/plugin_geoip.xml" name="geoip" />
to your b3.xml
(modify according to where you put it on your system.)
