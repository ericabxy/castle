#!/usr/bin/env python
from deh9000 import *

f = DehackedFile()

mobjinfo[MT_MISC2].clear_states()
mobjinfo[MT_MISC3].clear_states()
mobjinfo[MT_MISC4].clear_states()
mobjinfo[MT_MISC5].clear_states()
mobjinfo[MT_MISC6].clear_states()
mobjinfo[MT_MISC7].clear_states()
mobjinfo[MT_MISC8].clear_states()
mobjinfo[MT_MISC9].clear_states()
mobjinfo[MT_MISC12].clear_states()
dehfile.reclaim_states(32)
mobjinfo[MT_MISC2].update(states.parse('''
    Spawn:
        BON1 A 10
        BON1 B 10
        BON1 C 10
        BON1 D 10
        Loop
'''))
mobjinfo[MT_MISC3].update(states.parse('''
    Spawn:
        BON2 A 6
        BON2 B 6
        BON2 C 6
        BON2 D 6
        Loop
'''))
mobjinfo[MT_TFOG].update(states.parse('''
    Spawn:
        TFOG A {tics}
        TFOG B {tics}
        TFOG C {tics}
        TFOG D {tics}
        TFOG E {tics}
        TFOG F {tics}
        TFOG G {tics}
        TFOG H {tics}
        TFOG I {tics}
        TFOG J {tics}
        TFOG K {tics}
        Stop
'''.format(tics = '2')))
mobjinfo[MT_TFOG].flags = MF_NOBLOCKMAP | MF_NOGRAVITY | MF_SLIDE
soulsphere = mobjinfo[MT_MISC12]
soulsphere.update(states.parse('''
    Spawn:
        SOUL A 6
        SOUL B 6
        SOUL C 6
        SOUL D 6
        Loop
'''))
soulsphere.flags = MF_SPECIAL | MF_COUNTITEM | MF_SLIDE
keythings = {}
keythings[MT_MISC4] = 'BKEY'
keythings[MT_MISC5] = 'RKEY'
keythings[MT_MISC6] = 'YKEY'
keythings[MT_MISC7] = 'YSKU'
keythings[MT_MISC8] = 'RSKU'
keythings[MT_MISC9] = 'BSKU'
for key, value in keythings.items():
    mobjinfo[key].update(states.parse('''
        Spawn:
            {spr} A 5
            {spr} B 5
            {spr} C 5
            {spr} D 5
            Loop
    '''.format(spr = value)))
dehfile.miscdata.initial_bullets = 0
dehfile.sprnames[SPR_SOUL] = 'WICH'
dehfile.strings.GOTHTHBONUS = 'Got a sapphire cask!'
dehfile.strings.GOTARMBONUS = 'Picked up a ruby phial!'
dehfile.strings.GOTSUPER = 'You found a witch orb!'
dehfile.strings.GOTBLUECARD = 'You found a soul key!'
dehfile.strings.GOTREDCARD = 'You found a soul key!'
dehfile.strings.GOTYELWCARD = 'You found a soul key!'
dehfile.strings.GOTBLUESKUL = 'You found a soul key!'
dehfile.strings.GOTREDSKULL = 'You found a soul key!'
dehfile.strings.GOTYELWSKUL = 'You found a soul key!'
dehfile.strings.HUSTR_1 = 'Course 1: Battlefield'
dehfile.save('dehacked.lmp')
