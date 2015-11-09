castle = {
         '1': {
             'a': {
                  'contents': {
                              'You find yourself in an dark cell'
                              },
                   'actions': {
                              'move': {
                                      'doors': {'north': 'b'}
                                      },
                              'search room' : {
                                              'bed' : 'Under the pillow you find a knife'
                                                      '\n'
                                                      'You now have a knife'
                                              }
                                }
                  },
             'b': {
                  'contents': {
                              'You are in a deserted guard room'
                              },
                  'actions': {
                             'move': {
                                     'doors': {'south': 'a',
                                                'west': 'c',
                                               'north': 'd'}
                                     },
                             'search room': {
                                            'table' : 'On the table you find a cracked shield'
                                                      '\n'
                                                      'You now have a cracked shield',
                                            'desk': 'In the drawer you find a coin pouch'
                                                    '\n'
                                                    'You now have 7 coins',
                                            'cabinet' : 'You open to cabinet to have a dead body shot in the head by an arrow fall out'
                                            }
                             }
                  },
             'c': {
                  'contents': {},
                   'actions': {
                              'move': {
                                      'doors': {'east': 'b'}
                                      }
                               }
                   },ls
             'd': {
                  'contents': {},
                   'actions': {
                              'move': {
                                      'doors': {'south': 'b',
                                                 'west': 'e',
                                                 'east': 'f'}
                                      }
                               }
                  },
             'e': {
                  'contents': {},
                   'actions': {
                              'move': {
                                      'doors': {'east': 'd',
                                               'north': 'g'}
                                      }
                              }
                  },
             'f': {
                  'contents': {},
                   'actions': {
                              'move': {
                                      'doors': {'west': 'd'}
                                      }
                              }
                  },
             'g': {
                  'contents': {},
                   'actions': {
                              'move': {
                                      'doors': {'south': 'e'}
                                      }
                              }
                   }
              },
         '2': {
              'Room': {
                      'a': {
                           'contents': {},
                              'doors': {'front': 'b'}
                           },
                      'b': {
                           'contents': {},
                              'doors': {'back': 'b'}
                           }
                      }
              }
          }

def actions (level, room):        
    title = False
            
    while True:
        if title:
            print('--------------------------------------------------------------')
            print('Level:',  level)
            print('Room:', room)            
            print('It contains', castle[level][room]['actions']['search room'].keys())
            print('You can:  ([\'inspect\', \'move\'])')
            decide = input('What wil you do: ')
 
            if decide == 'inspect':
                print('--------------------------------------------------------------')
                print('Level:',  level)
                print('Room:', room)
                print('You can inspect', castle[level][room]['actions']['search room'].keys())
                object = input('Choose what to inspect: ')

                if object in castle[level][room]['actions']['search room']:
                    print('--------------------------------------------------------------')
                    print('Level:',  level)
                    print('Room:', room)
                    print(castle[level][room]['actions']['search room'][object])
                else:
                    print('****You can\'t do that****')

            elif decide == 'move':
                print('You can move:', castle[level][room]['actions']['move']['doors'].keys())
                move = input('Where will you go: ')
                return move
            else:
                print('****You can\'t do that****')
            
        print('You can:', castle[level][room]['actions'].keys())
        action = input('What will you do: ')

        if action in castle[level][room]['actions']:
            if action == 'search room':        
                title = True
            if action == 'move':
                print('You can move:', castle[level][room]['actions']['move']['doors'].keys())
                move = input('Where will you go: ')
                return move
        else:
            print('****You can\'t do that****')


def main():
    level = '1'
    room = 'a'

    while True:
        print('--------------------------------------------------------------')
        print('Level:',  level)
        print('Room:', room)
        print(castle[level][room]['contents'])
            
        move = actions(level, room)
        
        if move in castle[level][room]['actions']['move']['doors']:
            room = castle[level][room]['actions']['move']['doors'][move]
        else:
            print('****You can\'t do that****')

main()


#convert to list for no keys