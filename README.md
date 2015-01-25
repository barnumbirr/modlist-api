<h1><img src="https://raw.github.com/c0ding/modlist-api/master/doc/modlist.png" height=65 alt="modlist" title="modlist"> modlist-api</h1>

[![PyPi Version](http://img.shields.io/pypi/v/modlist.svg)](https://pypi.python.org/pypi/modlist/)   [![Downloads](http://img.shields.io/pypi/dm/modlist.svg)](https://pypi.python.org/pypi/modlist/)

**modlist** is an APACHE licensed library written in Python designed to provide a simple to use API wrapper for [MCF Modlist](http://modlist.mcf.li/).

## More about MCF Modlist:

MCF Modlist was created to be a comprehensive list of as many mods as possible. The MCF Mods Forum is quite hectic and popular threads easily bury fresh, new ideas that pop up and never quite gain attention.
Furthermore, searching within the forums was limited, as you could not accurately pinpoint mod versions, and each thread had its own format to display things. There was also the matter of compatibility and dependency. Thus the list was born.

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install modlist

## Modlist APIv3 Documentation:

This API can currently retrieve the following data from [MCF Modlist](http://modlist.mcf.li/):

  - /api/v3/:version.json:

```
>>> import modlist
>>> modlist.mods(VERSION)
[
    {
        "name": "Ambient Birds", 
        "author": [
            "the_tubes"
        ], 
        "versions": [
            "1.8"
        ], 
        "dependencies": [
            "Not Forge Compatible", 
            "Base Edit"
        ], 
        "link": "https://www.reddit.com/r/Minecraft/comments/2fabek/18_mod_ambient_birds/", 
        "type": [
            "SSP"
        ], 
        "desc": "Adds small birds of different colors."
    }, 
    {
        "other": "(Beta)", 
        "link": "http://www.minecraftforum.net/forums/mapping-and-modding/minecraft-mods/1278239-animal-bikes-added-wither-and-flower-bikes-1-8", 
        "name": "Animal Bikes", 
        "dependencies": [
            "Forge Compatible"
        ], 
        "author": [
            "Noppes"
        ], 
        "versions": [
            "1.8"
        ], 
        "type": [
            "Universal"
        ], 
        "desc": "A multiplayer mod which allows you to ride animals."
    },
	...
	...
	...
]
```

  - /api/v3/:version.md5:

```
>>> modlist.md5hash(VERSION)
b7b9fb60af57342d6c4fc8a0fc61891b
```

  - /api/v3/recent.json:

```
>>> modlist.recent()
{
    "1.7.2": [
        "(January/16/2015)",
        "  *Updated \"Dense Ores\": Updated link to CurseForge page",
        "  +Added \"Bladecraft\"",
        "  +Added \"Better Rain\"",
        "  +Added \"DecoCraft\"",
        "  +Added \"XtraBlocks Extreme Edition\"",
        "  +Added \"Kwasti Villagers\"",
        "  +Added \"Village Marker\"",
        "  +Added \"The Seasons Mod\": Currently in Alpha"
    ],
    "1.6.4": [
        "(January/16/2015)",
        "  +Added \"DecoCraft\"",
        "  +Added \"XtraBlocks Extreme Edition\""
    ],
    "1.5.2": [
        "(January/16/2015)",
        "  +Added \"Bladecraft\"",
        "  +Added \"DecoCraft\"",
        "  +Added \"XtraBlocks Extreme Edition\""
    ]
}
```

## License:

```
  Apache v2.0 License
  Copyright 2014-2015 Martin Simon

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

## Useful links:

* [MCF Modlist](http://modlist.mcf.li/)
* [Minecraft](https://minecraft.net/)

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
