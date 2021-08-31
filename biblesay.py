#!/usr/bin/python

import random
import textwrap

ascii_dove = """            \                                                                                           
             \                                                                          
              \                                                                         
               \                                                    O,                  
                \                                                   o.'                 
                 \                                                 0, l,                
                  \                                                l,  o'               
                   \                 O                            ;,    :,              
                    \                'loo                         ;c     ,c             
                     \               ;d  olo                     c;       ,;            
                      \              l;0   ;ol;                 l;        'd            
                       \              ;       dl               d;          c            
                        \             :l        lo            d:           :            
                         \            o:          d          d:            c            
                          \           d:           d        lc             l            
                           \           c            O      co             ,d            
                            \         Oc            O0    c;              ;             
                             \        0l             d  oo               :o             
                              \      ;o             0 l;                 ;              
                                 ,;oo;             Ool                  :;              
                                ;O 0  O;o,        dd0                  c,               
                               ,o        'OlO:-/-Oq                   lO                
                              <:dc,x,q,s                           ,dd                  
                                       ;0,                      ;00                     
                                         dO,                  0m       /t;              
                                          ;d,                   -doodc;  ;              
                                            .d.                          l              
                                              'io;                      o:              
                                                 'z:;0dOO;,,;hd0l;     d.               
                                                                  l0; d;                
                                                                    '0,                 
                                                                          """

if __name__ == '__main__':
    # Read verse file
    try:
        verses_file = open("verses.txt")
    except FileNotFoundError:
        verses_file = open("/usr/share/biblesay/verses.txt")

    verses = verses_file.readlines();

    # Choose a verse
    verse = random.choice(verses)

    # Wrap the text
    verse = textwrap.wrap(verse, width=50)

    # This int is for generating the speech bubble around the text later
    longest_line = 0

    # Get the longest line
    for i in range(len(verse)):
        longest_line = len(verse[i]) if len(verse[i]) > longest_line else longest_line

    # Print the top speech bubble line
    print(' ' + (longest_line + 2) * '_' + ' ');
    print('/' + (longest_line + 2) * ' ' + '\\');

    # Print the lines with vertical lines on the side for speech bubbles
    for i in range(len(verse)):
        # Add empty spaces to 'verse' until 'longest_line'
        for j in range(len(verse[i]), longest_line + 1):
            verse[i] += ' '
        verse[i] = '| ' + verse[i] + '|'
        print(verse[i])

    # Print the bottom speech bubble line
    print('\\' + (longest_line + 2) * '_' + '/');

    # Print the dove
    print(ascii_dove)
