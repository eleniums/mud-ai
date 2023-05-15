# Welcome to Evennia!

This is your game directory, set up to let you start with
your new game right away. An overview of this directory is found here:
https://github.com/evennia/evennia/wiki/Directory-Overview#the-game-directory

You can delete this readme file when you've read it and you can
re-arrange things in this game-directory to suit your own sense of
organisation (the only exception is the directory structure of the
`server/` directory, which Evennia expects). If you change the structure
you must however also edit/add to your settings file to tell Evennia
where to look for things.

Your game's main configuration file is found in
`server/conf/settings.py` (but you don't need to change it to get
started). If you just created this directory (which means you'll already
have a `virtualenv` running if you followed the default instructions),
`cd` to this directory then initialize a new database using

    evennia migrate

To start the server, stand in this directory and run

    evennia start

This will start the server, logging output to the console. Make
sure to create a superuser when asked. By default you can now connect
to your new game using a MUD client on `localhost`, port `4000`.  You can
also log into the web client by pointing a browser to
`http://localhost:4001`.

# Getting started

From here on you might want to look at one of the beginner tutorials:
http://github.com/evennia/evennia/wiki/Tutorials.

Evennia's documentation is here:
https://github.com/evennia/evennia/wiki.

Enjoy!

# Notes for mud-ai

Run the MUD server:
```
evennia start
```

Attach to server for logs:
```
evennia -l
```

Stop the server:
```
evennia stop
```

NOTE: An Oobabooga server with the REST API enabled will need to be running for
all commands to work properly. Set the REST API endpoint here in `ai/ai.py`:
```py
host = "ec2-35-90-219-160.us-west-2.compute.amazonaws.com"
```

Files I changed:

- Changed `SERVERNAME` in `server/conf/settings.py`
- Added `ai` package to prompt a chat ai for a response
- Added `commands/pray.py` to integrate with the `ai` package
- Added `world/rooms.py` containing some custom rooms
- Added `create_world.ev` batchcommand file to create the world
