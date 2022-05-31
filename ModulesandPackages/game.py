#import draw
# also we can import the module objects to the current namespace
# from draw import draw_game
# import all object form a module 
from draw import *
def play_game():
     ...

def main():
    result = play_game()
    #draw.draw_game(result)
    draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()


# custom import name
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)