maze = {
             'a': {
                    {e, f, b}
                  },

                  },
             'b': {
                   'actions': {
                              'move': {
                                      'doors': {'a': a,
                                                'h': h,
                                                'c': c}
                                      },
                              'shoot'
                                }
                  },
              'c': {
                   'actions': {
                              'move': {
                                      'doors': {'b': b,
                                                'j': j,
                                                'd': d}
                                      },
                              'shoot'
                                }
                  },
              'd': {
                   'actions': {
                              'move': {
                                      'doors': {'c': c,
                                                'l': l,
                                                'e': e}
                                      },
                              'shoot'
                                }
                  },
              'e': {
                   'actions': {
                              'move': {
                                      'doors': {'d': d,
                                                'n': n,
                                                'a': a}
                                      },
                              'shoot'
                                }
                  },
              'f': {
                   'actions': {
                              'move': {
                                      'doors': {'a': a,
                                                'g': g,
                                                'o': o}
                                      },
                              'shoot'
                                }
                  },
              'g': {
                   'actions': {
                              'move': {
                                      'doors': {'f': f,
                                                'h': h,
                                                'p': p}
                                      },
                              'shoot'
                                }
                  },
              'h': {
                   'actions': {
                              'move': {
                                      'doors': {'g': g,
                                                'b': b,
                                                'i': i}
                                      },
                              'shoot'
                                }
                  },
              'i': {
                   'actions': {
                              'move': {
                                      'doors': {'h': h,
                                                'j': j,
                                                'q': q}
                                      },
                              'shoot'
                                }
                  },
              'j': {
                   'actions': {
                              'move': {
                                      'doors': {'i': i,
                                                'c': c,
                                                'k': k}
                                      },
                              'shoot'
                                }
                  },
              'k': {
                   'actions': {
                              'move': {
                                      'doors': {'j': j,
                                                'l': l,
                                                'r': r}
                                      },
                              'shoot'
                                }
                  },
              'l': {
                   'actions': {
                              'move': {
                                      'doors': {'d': d,
                                                'k': k,
                                                'm': m}
                                      },
                              'shoot'
                                }
                  },
              'm': {
                   'actions': {
                              'move': {
                                      'doors': {'n': n,
                                                's': s,
                                                'l': l}
                                      },
                              'shoot'
                                }
                  },
              'n': {
                   'actions': {
                              'move': {
                                      'doors': {'e': e,
                                                'o': o,
                                                'm': m}
                                      },
                              'shoot'
                                }
                  },
              'o': {
                   'actions': {
                              'move': {
                                      'doors': {'t': t,
                                                'f': f,
                                                'n': n}
                                      },
                              'shoot'
                                }
                  },
              'p': {
                   'actions': {
                              'move': {
                                      'doors': {'q': q,
                                                'g': g,
                                                't': t}
                                      },
                              'shoot'
                                }
                  },
              'q': {
                   'actions': {
                              'move': {
                                      'doors': {'p': ,
                                                'i': ,
                                                'r': }
                                      },
                              'shoot'
                                }
                  },
              'r': {
                   'actions': {
                              'move': {
                                      'doors': {'k': ,
                                                's': ,
                                                'q': }
                                      },
                              'shoot'
                                }
                  },
              's': {
                   'actions': {
                              'move': {
                                      'doors': {'t': ,
                                                'm': ,
                                                'r': }
                                      },
                              'shoot'
                                }
                  },
                't': {
                   'actions': {
                              'move': {
                                      'doors': {'o': ,
                                                's': ,
                                                'p': }
                                      },
                              'shoot'
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







a = [e, f, g]



maze = [
		[a[e,f,g]],
	    [b[e, f, g]]
	    ]








