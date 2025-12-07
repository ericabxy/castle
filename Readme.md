Castle
======

Collect-a-thon challenge game made for Boom.

Roadmap
-------

Currently only Level 1 is drafted. Its playable as a proof-of-concept but requires further design and refinement.

### Levels

1. Battlefield
2. ???
3. ???
4. ???
5. ???

Requirements
------------

Running the game requires a Boom-compatible [source port](https://doomwiki.org/wiki/Source_port).

The scripted build process requires [GNU Make](https://www.gnu.org/software/make/) or equivalent.

Getting Started
---------------

Run Make build the Wad.

    make

If you have [Boom](https://doomwiki.org/wiki/Boom) installed or a shortcut to a Boom-compatible source port like [DSDA-Doom](https://doomwiki.org/wiki/DSDA-Doom), running Make again with the "run" target will start the game.

    make run

The game at this point is self-contained within the resulting Wad file. You can copy it anywhere you want and clean up from the build process.

    make clean

How to Play
-----------

Course 1 requires you to collect all six "soul keys" which look like shining orbs with a yellow skull inside. Some are easier to collect than others. Your progress on collecting soul keys is displayed on your screen by yellow numbers 1 through 6.

There are a variety of other items and secrets to collect. Open the auto-map (on keyboards usually by pressing Tab), to see your progress on items and secrets. They are not required to finish the course, but they do count toward 100% completion.

Here are some tips for finding all keys, items, and secrets.

### Look Up

You'll notice many collectible objects are out-of-reach vertically. They may be triggered to lower by crossing a line, punching something, or pressing Use. Some you must find steps to raise yourself up to.

### Hurry Up

Some lowered pillars raise up again after a short time. You'll need to find a way to reach them after crossing the line that lowers them, but before they raise up again.

### Look Around

You can see a lot of the collectibles from somewhere on the map. Some of them mark a line that you need to cross to lower another collectible. The map secrets are invisible, but may be marked out in violet on your automap if you've seen the tops of them.

### Doomguy Doesn't Need to Jump

This is a Doom platformer game. As such although you can't jump, you can cross pretty large gaps without falling, and you can reach higher platforms if they are low enough to step up on. Try "strafe-running" if moving straight isn't fast enough to make a crossing (run Forward and to one side at the same time; its actually faster than moving in only one direction).
