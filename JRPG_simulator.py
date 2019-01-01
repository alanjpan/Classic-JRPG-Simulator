# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:23:12 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

program framework for description and simulation of classic JRPG experiences with one life and no save points

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Classic JRPG Simulator [Computer software]. Github repository <https://github.com/alanjpan/Classic-JRPG-Simulator>

Note this software's license is GNU GPLv3.
"""

import random
secure_random = random.SystemRandom()

experience = 0
roll = [2, 3, 4, 5, 6, 7, 8]
dungeon = []
dungeon_length = 0
boss_table = []

def generate_dungeon(dungeon_length):
        global dungeon
        for i in range(dungeon_length):
                quest(i)
        placeboss()

def quest(i):
        global dungeon
        global experience
        experience_roll = 0
        experience_roll = secure_random.choice(roll)
        experience_gained = 50 + i*10 + experience_roll*5
        dungeon.append(experience_gained)

def placeboss():
        boss_interval = int(len(dungeon) / 10)
        boss_table.append(5000)
        for i in range(boss_interval):
                boss_roll = random.randrange(2, 4, 1)
                boss_placement = random.randrange(4, len(dungeon), 1)
                try:
                        boss_table.append(boss_roll * dungeon[boss_placement] + boss_placement*500 + int(boss_table[i-1]*.5))
                        dungeon[boss_placement] = 'boss'
                except:
                        i - 1
        total = 0
        for i in dungeon:
                try:
                        total += i
                except:
                        continue
        final_boss = 0
        final_boss = int(total * 4)
        dungeon[len(dungeon)-1] = 'boss'
        boss_table.append(final_boss)

generate_dungeon(100)
game_over = False
location = 0
doodads = [',', ',', '.', ' ', ' ']
turns = 0
bosses_defeated = 0
villagertips = ['[VILLAGER]: don\'t tell others, but sometimes I like to imagine our world is three dimensional', '[VILLAGER]: would you like a flower? here [,]', '[VILLAGER]: all is well~ all is well~', '[VILLAGER]: what is permadeath? do you mean there will be another famine?', '[VILLAGER]: [A] is the demon lord plaguing our land', '[VILLAGER]: can you even spam?', '[VILLAGER]: bosses are tough! do not go in unprepared!', '[VILLAGER]: our land used to be so beautiful with ~s', '[VILLAGER]: i heard the next boss requires at least ' + str(int(boss_table[bosses_defeated]*.75)) + ' experience points', '[VILLAGER]: did you know? you can rush forward ten paces with input qq', '[VILLAGER]: at least I am not living in that far away land that chooses tv stars as leaders']
print('[VILLAGER]: the first boss always requires 5000 experience points to defeat!')
while game_over == False:
        if dungeon[location] == 'boss':
                print('boss fight: ' + str(boss_table[bosses_defeated]) + ' experience required')
                if experience > boss_table[bosses_defeated]:
                        print('boss defeated')
                        boss_experience = int(boss_table[bosses_defeated] * .1)
                        bosses_defeated += 1
                        dungeon[location] = 0
                        print(str(boss_experience) + ' experience gained')
                        experience += boss_experience
                else:
                        print('GAME OVER')
                        print('you were slain by a boss')
                        print('total experience gained: ' + str(experience))
                        print('bosses defeated: ' + str(bosses_defeated))
                        print('total turns taken: ' + str(turns))
                        print('grinding turns: ' + str(turns - location))
                        game_over = True
        else:
                experience += dungeon[location]
                print('total experience: ' + str(experience))
                draw = ''
                for i in range(len(dungeon)):
                        paint = ''
                        paint = secure_random.choice(doodads)
                        
                        if location == i:
                                draw += '@'
                        elif len(draw) == len(dungeon)-1:
                                draw += '[A]'
                        elif dungeon[i] == 'boss':
                                draw += 'A'
                        else:
                                draw += paint
                print(draw)
                print('input d to advance, input a to step back')
                response = input()
                if response.startswith('d'):
                        location += 1
                elif response.startswith('a'):
                        location -= 1
                elif response.startswith('qq'):
                        location += 10
                elif response == '':
                        experience -= dungeon[location]
        
                if (location < 0) or (location > len(dungeon)):
                        print('GAME OVER')
                        print('you went off the map')
                        print('total experience gained: ' + str(experience))
                        print('bosses defeated: ' + str(bosses_defeated))
                        print('total turns taken: ' + str(turns))
                        print('grinding turns: ' + str(turns - location))
                        game_over = True
                turns += 1
                villager_encounter = 20
                if random.randrange(0, 100, 1) <= villager_encounter:
                        print(secure_random.choice(villagertips))