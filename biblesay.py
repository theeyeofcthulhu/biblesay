#!/usr/bin/python

import random
import textwrap
from optparse import OptionParser

ascii_dove = """            \                                                                                           
             \                                                                          
              \                                                                         
               \                                                    O,                  
                \                                                   o;,                 
                 \                                                 ,j l,                
                  \                                                l,  o;               
                   \                 d,                           ;,    v,              
                    \                ;loo,                        ;c     ,c             
                     \               'd  olo,                    c;       :;            
                      \               lc   'ol;                 l;        'd            
                       \              ;,      dl,              d;          c,           
                        \             :l       'lo,           d:           g;           
                         \            o:         ;d          d:            c,           
                          \           d:          ;d        lc             l            
                           \          ;c           ;O      co             ,d            
                            \         Oc            O,    c;              ;:            
                             \        0l            ;d  ,O;              :o             
                              \      ;o             0:,;o                c;             
                                 ,;oo;             Oolp                 :;              
                                ;O 0  O;o,       ,dd;                  c;               
                               ,o        'OlO:ideO;'                  lO                
                              <:dc,e,qo,                           ,dd                  
                                       '0,                      ;00                     
                                         dO,                  0m       ,t;              
                                          'd,                  'tdoodc;' ;              
                                            'd.                          l              
                                              'io;,                     o:              
                                                 'z:;idri;ip;hd0l;,    d;               
                                                                  l0;,d;                
                                                                    'n'                 
                                                                          """

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-d', '--no-dove', help='do not display a dove', action='store_true', dest='nodove')
    parser.add_option('-s', '--no-speech-bubble', help='do not display a speech bubble', action='store_true', dest='nospeechbubbles')
    parser.add_option('-f', '--file', dest='file', help='load verses from a specific FILE', metavar='FILE')
    (options, args) = parser.parse_args()

    # Read verse file
    if not options.file:
        try:
            verses_file = open('verses.txt')
        except FileNotFoundError:
            verses_file = open('/usr/share/biblesay/verses.txt')
    else:
        verses_file = open(options.file)

    verses_file.close()

    # Choose a verse
    verse = random.choice(verses)

    # Wrap the text
    verse = textwrap.wrap(verse, width=50)

    # This int is for generating the speech bubble around the text later
    longest_line = 0

    # Get the longest line
    for i in range(len(verse)):
        longest_line = len(verse[i]) if len(verse[i]) > longest_line else longest_line

    if not options.nospeechbubbles:
        # Print the top speech bubble line
        print(' ' + (longest_line + 2) * '_' + ' ');
        print('/' + (longest_line + 2) * ' ' + '\\');

    # Print the lines with vertical lines on the side for speech bubbles
    for i in range(len(verse)):
        # Add empty spaces to 'verse' until 'longest_line'
        if not options.nospeechbubbles:
            for j in range(len(verse[i]), longest_line + 1):
                verse[i] += ' '
            verse[i] = '| ' + verse[i] + '|'
        print(verse[i])

    # Print the bottom speech bubble line
    if not options.nospeechbubbles:
        print('\\' + (longest_line + 2) * '_' + '/');

    if not options.nodove:
        # Print the dove
        print(ascii_dove)
