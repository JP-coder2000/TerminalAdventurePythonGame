import time

print('\n ================================================')
time.sleep(1)
print('        Once in a very distant kingdom...')
time.sleep(1)
print(' ================================================')

print('\n JP: Hello there!')
time.sleep(2)
print(' JP: I thought you were dead...')
time.sleep(2)
print(" JP: I'm glad to see you are fine!")
time.sleep(2)
name = input("JP: It's been a long time since I last saw you... (ENTER YOUR NAME) ")
time.sleep(1.5)
print(f'\n JP: Welcome back, {name}!')
time.sleep(2)
print(f'{name}: What...what in the hell happened? For how long have I been sleeping?')
time.sleep(2)

print(' JP: You\'ve been sleeping for far too long, my friend...')
time.sleep(3)
print('JP: Remember how once we were a peaceful kingdom?')
time.sleep(3)
print(' JP: Well, all of that changed when the emperor died and his son took the throne...')
time.sleep(3)
print('(Loud noises in the background)')
time.sleep(2)

print(' JP: Shit, they\'ve found us!')
time.sleep(2)
print(' JP: Quick, take this sword and remember who you once were!')
time.sleep(2)



print('\n Take the sword?')
print('1 = YES')
print('2 = NO')

first_res = input('Select the number of the answer you desire...')

while first_res != '1':
    print(f'\n JP: Please {name}, we are both going to die if you don\'t help me!')
    time.sleep(2)
    print('\n Take the sword?')
    print('1 = YES')
    print('2 = NO')

    first_res = input('Select the number of the answer you desire...')

if first_res == '1':
    print(f'\n {name}: Don\'t worry JP, there\'s a reason they call me {name} the mightiest of all!')
time.sleep(2)


print(f'{name} start\'s running toward\'s the enemy!')
time.sleep(1.5)
print(f'The enemy {name} has to beat to get out of the dungeon is a Goblin!')
time.sleep(1.5)
print(f'The Goblin has 20 HP and has 2 DP')
time.sleep(1.5)
print(f'{name} has 10 HP and 5 DP ')
time.sleep(1.5)


print(f'Would you like to start the encounter?')
print('1 = YES')
print('2 = NO')

second_res = input('Select the number of the answer you desire...')

if second_res == '1':
    print('LET\'S GO!')
    player_hp = 10
    player_dp = 5
    gob_hp = 20
    gob_dp = 2
    
    while gob_hp > 0 and player_hp > 0:
        print(f'{name} what would you like to do?')
        print('1 = ATTACK')
        print('2 = DODGE')
        print('3 = RUN')
        third_res = int(input('Select the number of the answer you desire...'))
        
        if third_res == 1:

            print(f'The Goblin attacks {name}!')
            time.sleep(1.5)
            player_hp = player_hp - gob_dp
            print(f'{name} has {player_hp} HP left!')
            time.sleep(1.5)

            print(f'{name} attacks the Goblin!')
            time.sleep(1.5)
            gob_hp = gob_hp - player_dp
            print(f'The Goblin has {gob_hp} HP left!')
            time.sleep(1.5)



        elif third_res == 2:
            print(f'{name} dodges the Goblin\'s attack!')
            time.sleep(1.5)
            print(f'{name} regenerates 1 HP!')
            time.sleep(1.5)
            player_hp = player_hp + 1
            print(f'{name} has {player_hp} HP left!')
            time.sleep(1.5)

        elif third_res == 3:
            print(f'{name} runs away!')
            break

        else:
            print(f'Invalid choice, {name}!')
    
    if player_hp <= 0:
        print(f'{name} has been defeated by the Goblin!')
        time.sleep(2)
        print(f'JP: Noooooo! {name}!')
        time.sleep(2)
        exit()

    if gob_hp <= 0:
        time.sleep(2)
        print(f'{name} has defeated the Goblin!')
        time.sleep(2)
        print(f'JP: Well done {name}! You\'ve defeated the Goblin!')
        time.sleep(2)
        print(f'JP: Now let\'s get out of here!')
        time.sleep(2)
        print(f'{name} and JP start running towards the exit!')
        time.sleep(2)
        print(f'JP: We\'re almost there!')
        time.sleep(2)
        print(f'JP: Oh no! There\'s a guard blocking the exit!')
        time.sleep(2)
        print(f'JP: {name}, you have to defeat him!')
        time.sleep(2)
        print(f'{name} has to defeat the guard to get out of the dungeon!')
        time.sleep(2)
        print(f'The guard has 30 HP and 5 DP')
        time.sleep(2)
        print(f'{name} has {player_hp} HP and {player_dp} DP')
        time.sleep(2)
        print(f'Would you like to start the encounter?')
        print('1 = YES')
        print('2 = NO')
        fourth_res = input('Select the number of the answer you desire...')
        if fourth_res == '1':
            time.sleep(2)
            print('LET\'S GO!')
            time.sleep(2)
            guard_hp = 30
            guard_dp = 2
            while guard_hp > 0 and player_hp > 0:
                print(f'{name} what would you like to do?')
                print('1 = ATTACK')
                print('2 = DODGE')
                print('3 = RUN')
                print('Hint: First, YOU MUST regenerate 10 HP by dodging the guard\'s attack!')
                fifth_res = int(input('Select the number of the answer you desire...'))
                if fifth_res == 1:
                    print(f'The guard attacks {name}!')
                    time.sleep(2)
                    player_hp = player_hp - guard_dp
                    print(f'{name} has {player_hp} HP left!')
                    time.sleep(2)
                    
                    print(f'{name} attacks the guard!')
                    time.sleep(2)
                    guard_hp = guard_hp - player_dp
                    print(f'The guard has {guard_hp} HP left!')
                    time.sleep(2)


                elif fifth_res == 2:
                    print(f'{name} dodges the guard\'s attack!')
                    time.sleep(2)
                    print(f'{name} regenerates 10 HP!')
                    time.sleep(2)
                    player_hp = player_hp + 10

                elif fifth_res == 3:
                    print(f'{name} runs away!')
                    break

                else:
                    print(f'Invalid choice, {name}!')
            
            if player_hp <= 0:
                print(f'{name} has been defeated by the guard!')
                time.sleep(2)
                print(f'JP: Noooooo! {name}!')
                time.sleep(2)
                exit()

            if guard_hp <= 0:
                print(f'{name} has defeated the guard!')
                time.sleep(2)
                print(f'JP: Well done {name}! You\'ve defeated the guard!')
                time.sleep(2)
                print(f'JP: Now let\'s finally get out of here!')
                time.sleep(2)
                print(f'{name} and JP start running towards the exit!')
                time.sleep(2)
                print(f'JP: We\'re finally out of here!')
                time.sleep(2)
                print(f'JP: Thank you {name}! You\'ve saved my life!')
                time.sleep(2)
                print(f'{name}: No problem JP, I\'m glad I could help!')
                time.sleep(2)
                print(f'JP: It\'s now time for you to go back to the kingdom and take back what\'s yours!')
                time.sleep(2)
                print(f'{name}: I will JP, I will!')
                time.sleep(2)
                print(f'JP: Good luck {name}!')
                time.sleep(2)
                exit()
        else:
            print(f'Invalid choice, {name}!')
            exit()
else:
    print(f'Invalid choice, {name}!')
    exit()