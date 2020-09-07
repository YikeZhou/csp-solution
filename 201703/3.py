'''
File: 3.py
Project: 201703
File Created: Sunday, 6th September 2020 9:25:16 pm
Author: zyk
-----
Last Modified: Monday, 7th September 2020 3:57:02 pm
Modified By: zyk
-----
2020 - HUST
'''

from sys import stdin

state = {'header': 0, 'para': 1, 'item': 2}

last_state = state['header']

line = stdin.readline()
while line != '':
    # judge current state
    if line.strip() == '':
        # this is a blank line
        if last_state == state['para']:
            print('</p>')
            last_state = state['header']
        elif last_state == state['item']:
            print('</ul>')
            last_state = state['header']
        
        line = stdin.readline()
        continue
    elif line[0] == '#' and line.lstrip('#')[0] == ' ':
        cur_state = state['header']
    elif line[0] == '*' and line[1] == ' ':
        cur_state = state['item']
    else:
        cur_state = state['para']

    # parse inline syntax
    if '_' in line:
        start = 0
        flag = False
        place = line.find('_', start)
        while place >= 0:
            if flag:
                new = '</em>'
            else:
                new = '<em>'
            
            line = line.replace('_', new, 1)

            flag = not flag
            start = place + 1
            place = line.find('_', start)

    if '[' in line:
        start = 0
        place = line.find('[', start)
        while place >= 0:
            text_left = place + 1
            link_left = line.find('(', start) + 1
            link_right = line.find(')', start)
            text_right = link_left - 2

            text = line[text_left:text_right]
            link = line[link_left:link_right]
            line = line[:text_left - 1] + '<a href="' + link + '">' + text + '</a>' + line[link_right + 1:]
            
            start = link_right + 1
            place = line.find('[', start)

    # print HTML
    if cur_state == state['header']:
        dep = str(len(line) - len(line.lstrip('#')))
        if last_state == state['header']:
            print('<h' + dep + '>' + line.strip('# \n') + '</h' + dep + '>')
        elif last_state == state['para']:
            print('</p>' + '\n' + '<h' + dep + '>' + line.strip('# \n') + '</h' + dep + '>')
        else: # item
            print('</ul>' + '\n' + '<h' + dep + '>' + line.strip('# \n') + '</h' + dep + '>')
    
    elif cur_state == state['item']:
        if last_state == state['header']:
            print('<ul>\n<li>' + line.strip('* \n') + '</li>')
        elif last_state == state['para']:
            print('</p>' + '\n' + '<ul>\n<li>' + line.strip('* \n') + '</li>')
        else: # item
            print('<li>' + line.strip('* \n') + '</li>')
    
    else: # para
        if last_state == state['para']:
            print('\n' + line[:-1], end='')
        elif last_state == state['item']:
            print('</ul>\n<p>' + line[:-1], end='')
        else: # blank or header
            print('<p>' + line[:-1], end='')
    
    # update
    last_state = cur_state
    line = stdin.readline()

if last_state == state['para']:
    print('</p>')
elif last_state == state['item']:
    print('</ul>')
