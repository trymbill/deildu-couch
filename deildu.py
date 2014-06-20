from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.torrents._deildu import Deildu
from couchpotato.core.media.movie.providers.base import MovieProvider

def start():
    return Deildu()

config = [{
    'name': 'deildu',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'Deildu.net',
            'description': 'See <a href="http://deildu.net">Deildu.net</a>',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                }
            ],
        }
    ]
}]
