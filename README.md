# Deildu.net Search Provider for Couch Potato Server

Clone this repository into **/couchpotato/core/providers/torrent**, and use it 
to enable Deildu.net as a Search Provider for Couch Potato. Deildu.net is 
**restricted to Iceland only**, so if you're not in Iceland, please ignore :)*

#### Note: This repo might not be here for very long. I just decided to set it up for people to try it out until I get a clear response on whether or not these kinds of Search Providers, restricted to countries and what not, will be added to the CouchPotatoServer repo. Until then, it will remain here as a way of developing it further.

SETUP INSTRUCTIONS
---

```
# Go into your CouchPotatoServer folder
cd ~/CouchPotatoServer

# Shut down CouchPotatoServer, either by opening it up in a browser 
# and going to "settings" -> "shutdown", or by terminating the process

# Clone this repository into the torrent providers folder
git clone https://github.com/trymbill/deildu-couch.git ./couchpotato/core/providers/torrent/deildu

# Startup CouchPotatoServer
python CouchPotato.py

# Now you should see Deildu.net as one of the prodivers for Torrents.
```

SHOUT OUT
---

A huge shout out to RuudBurger (https://github.com/RuudBurger) for making CouchPotato. 
It's a really well thought out machine, easily extendable for anyone with basic python 
knowledge. Kudos to you, sir!
