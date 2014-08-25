# Deildu.net Search Provider for Couch Potato Server v2.4.0

####SETUP INSTRUCTIONS

```
# Download the Deildu.net search provider
https://github.com/trymbill/deildu-couch/archive/master.zip and extract it somewhere.

# Shut down CouchPotatoServer, either by opening it up in a browser 
# and going to "settings" -> "shutdown", or by terminating the process

# Open your CouchPotatoServer folder and traverse into the following directory
cd [pathtocouchpotato]/.couchpotato/couchpotato/core/media/_base/providers/torrent
From the extracted folder, put _deildu.py in this directory.

# Now traverse into the following directory
cd [pathtocouchpotato]/.couchpotato/couchpotato/core/media/movie/providers/torrent
From the extracted folder, put deildu.py in this directory.

# Startup CouchPotatoServer
cd ~/CouchPotatoServer # or wherever you have it stored
python CouchPotato.py

# Now you should see Deildu.net as one of the prodivers for Torrents.
```

####SHOUT OUT

A huge shout out to RuudBurger (https://github.com/RuudBurger) for making CouchPotato. 
It's a really well thought out machine, easily extendable for anyone with basic python 
knowledge. Kudos to you, sir!
