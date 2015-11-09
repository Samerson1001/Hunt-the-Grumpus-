maze = {
             'a': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
             'b': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'c': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'd': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },

              'e': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'f': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'g': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'h': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'i': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'j': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'k': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'l': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'm': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'n': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'm': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'o': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'p': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'q': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              'r': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
              's': {
                   'actions': {
                              'move': {
                                      'doors': {'': ,
                                                '': ,
                                                '': }
                                      },
                              'shoot'
                                }
                  },
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