maze = {
             'a': {
                   'actions': {
                              'move': {
                                      'doors': {'north': 'b'}
                                      },
                              'shoot'
                                }
                  },
             'b': {
                  'actions': {
                             'move': {
                                     'doors': {'south': 'a',
                                                'west': 'c',
                                               'north': 'd'}
                                     },
                             'search room'
                             }
                  },
             'c': {
                   'actions': {
                              'move': {
                                      'doors': {'east': 'b'}
                                      }
                               }
                   },
             'd': {
                   'actions': {
                              'move': {
                                      'doors': {'south': 'b',
                                                 'west': 'e',
                                                 'east': 'f'}
                                      }
                               }
                  },
             'e': {
                   'actions': {
                              'move': {
                                      'doors': {'east': 'd',
                                               'north': 'g'}
                                      }
                              }
                  },
             'f': {
                   'actions': {
                              'move': {
                                      'doors': {'west': 'd'}
                                      }
                              }
                  },
             'g': {
                   'actions': {
                              'move': {
                                      'doors': {'south': 'e'}
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