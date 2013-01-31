# Deildu.net Search Provider for Couch Potato Server

####SETUP INSTRUCTIONS (TLDR)

Download the master branch *https://github.com/trymbill/deildu-couch/archive/master.zip* and throw it into
your Couch Potato torrent providers folder.

####SETUP INSTRUCTIONS

```
# Download the Deildu.net search provider
https://github.com/trymbill/deildu-couch/archive/master.zip

# Shut down CouchPotatoServer, either by opening it up in a browser 
# and going to "settings" -> "shutdown", or by terminating the process

# Open your CouchPotatoServer folder and traverse into the torrent providers folder
cd ~/CouchPotatoServer # or wherever you have it stored
cd ./couchpotato/core/providers/torrent

# Extract the downloaded master.zip into a folder named deildu
unzip master.zip -d deildu # note, your master.zip might be located somewhere else

# Startup CouchPotatoServer
cd ~/CouchPotatoServer # or wherever you have it stored
python CouchPotato.py

# Now you should see Deildu.net as one of the prodivers for Torrents.
```

####SHOUT OUT

A huge shout out to RuudBurger (https://github.com/RuudBurger) for making CouchPotato. 
It's a really well thought out machine, easily extendable for anyone with basic python 
knowledge. Kudos to you, sir!
