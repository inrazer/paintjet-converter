#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#import serial
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inp", help="Input file")
parser.add_option("-o", "--out", dest="out", help="Output file")
#parser.add_option("-c1", "--color1", dest="colour", help="ColourMode 1")
#parser.add_option("-c2", "--color2", dest="colour", help="ColourMode 2")
#parser.add_option("-c3", "--color3", dest="colour", help="ColourMode 3")
(options, args) = parser.parse_args()

if options.inp == None :
        print ('Please enter a input file !')
        sys.exit(1)

if options.out == None :
        print ('Please enter a outout file !')
        sys.exit(1)

plane_c = ''
plane_m = ''

setColourMode = "\x2A\x72\x2D\x33\x55" # represents for *r-3U

print ('Started converting the weird HP Painjet Color palette based to ghostscript CMY')

print ('Open files ....')
f_in = open(options.inp,"rb")
f_out = open(options.out,'w')
print ('Ready ?')
while True:
#if f_in.mode == 'rb':
        #print ('Reading ...')
        content_in = f_in.read()
        if not content_in:
                print('..think, we are done. Time for coffee & cookies...')
                break
        
        # split string at every ESC
        content_filter = content_in.split("\x1B")
        # determine index of hor. pos. command
        # by finding first appearance of command
        idx_headStart = content_filter.index('&a900H')
        #idx_headStart = content_filter.index("\x00\x00")

        # determine index of termination command
        idx_rasterEnd = content_filter.index('*rB\n\n\n\n')
        
        # colorMode command is 2 seq. ahead
        idx_colorMode = idx_headStart+2

        # manipulate color mode if wrong
        data_colorMode = content_filter[idx_colorMode]
        if data_colorMode != setColourMode:
                content_filter[idx_colorMode] = "\x2A\x72\x2D\x33\x55"

        print('splitted INPUT string following')
        print(content_filter)
        
        #create a list of all colour planes
        lst_planes = []
        for i in range(len(content_filter)):
                if '*b128V' in content_filter[i]:
                        lst_planes.append(i)
                        #print '"*b128V" found in item %s' % i
        print('For reference following list if found colour planes')
        print(lst_planes)

        # DEBUG - get idx from lst_planes of the first colour planes C/R and M/G
        idx_row1plane1 = lst_planes[0]
        idx_row1plane2 = lst_planes[1]        

        # determine idx of last 2nd-colour plane
        idx_rowLastplane2 = lst_planes[-1]-1

        #skip 3rd colour and 128W planes
        stepSize_color1 = 3
        stepSize_color2 = 3

        # define some variables for data manipulation

        #plane1Old_idx = ''
        #plane1Old_data = ''

        #plane1New_idx = ''
        #plane1New_data = ''
        
        #plane2Old_idx = ''
        #plane2Old_data = ''

        #plane2New_idx = ''
        #plane2New_data = ''

        # set a point to start
        plane1New_idx = 0
        plane2New_idx = 1
        
        # manipulate data until hitting the last 2nd-colour plane
        while plane2New_idx < idx_rowLastplane2:
                # allocate idxes from last run to actual one
                plane1Old_idx = plane1New_idx
                plane2Old_idx = plane2New_idx
                # load data from content_filter list
                plane1Old_data = content_filter[plane1Old_idx]
                plane2Old_data = content_filter[plane2Old_idx]
                # cross-change colour planes 1 and 2
                plane1New_data = plane2Old_data
                plane2New_data = plane1Old_data
                # replace data of altered planes in content_filter list
                content_filter[plane1Old_idx] = plane1New_data
                content_filter[plane2Old_idx] = plane2New_data
                # set a new set of idx
                plane1New_idx = plane1Old_idx + stepSize_color1
                plane2New_idx = plane2Old_idx + stepSize_color2

        #fault filter - full picture has ~514 raster lines
        #possible test -> {NoModulo}((idx_rasterEnd-70)/ 4) = (512)TRUE

        #for debug the list to be OUTPUT once again
        print('Following the altered data to be OUTPUT')
        print(content_filter)

        # DEBUG - print some debug msg        
        print(' ')
        print('Some DEBUG information')
        print(' ')
        print('Data blocks in buffer: '+str(len(content_filter)))
        print('Index of head data as abs: '+str(idx_headStart))
        print('Index of ColorMode as abs: '+str(idx_colorMode))
        print('Index of Row1-Plane1 as abs: '+str(idx_row1plane1))
        print('Index of Row1-Plane2 as abs: '+str(idx_row1plane2))
        print('Index of rasterEnd as abs: '+str(idx_rasterEnd))

        ##print(content_filter)
        #for x in range(int(len(content_filter))):
        #        f_out.write('\x1B'+content_filter[x])
        
