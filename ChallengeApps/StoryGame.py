print('Would you like to play?')
choice = input('Enter \'Y\' for yes or \'N\' for no ')
choice = choice.lower()


if choice == 'y':
    name = input('Type your name then press Enter ')
    home = input( 'Type your home then press Enter   ')
    story = input('Would you like to be in Sleepless or Forgotten? Type your answer then press Enter')
    story = story.lower()
    if story == 'sleepless':
        print(name + ' was a very brave human. He was intent on saving\n the world from all the evildoers')
        print('However, ' + name +' lived in a very peaceful land called\n ' + home + ' where there was no evil.')
        print('Therefore ' + name + ' had many sleepless nights worrying about\n the rest of the world and missing their own.')
    if story == 'forgotten':
        print(name + ' was born in ' + home + '.')
        print('Unfortunately '+ name + ' was orphaned at a very young age.')
        print(name + ' was forgotten.')
else:
    print('Ok, maybe next time!')

print('You need to make a choice!')
decision1 = input('Will you stay and try make your situation better?  Or will you leave?'
                  'Type stay or leave then press Enter to make your choice     ')
if decision1 == 'stay':
    print(name + ' decides to stay and make things better.  It will be a hard time but '+name+ ' is strong!')
    print(name+ ', good luck on your new adventure!')
else:
    print(name+ ' leaves '+home+ ' and journeys out into the world looking for people she can help')