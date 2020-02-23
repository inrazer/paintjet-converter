# paintjet-converter
Primarily designed for converting PaintJet Color PCL-data from 80's Rohde &amp; Schwarz spectrum analysers
or other devices outputting this format of data.

Note: Script was designed to run with Python 2.7, review for Python 3 following.
I have kind of linking for old tech ;-)

## What ?
- The script replaces the colour palette parameter in the head of the PCL printer data. (working)  
- Next the first and second colour plane in every raster line are exchanged with each other. (still glitchy)  
So e.g. changing the appearances of the colour red and green by respectively becoming the other one (with RGB-model used)

## Source
- PCLViewer (https://www.pclviewer.com/de/resources/reference/index.html)
- Offical PCL Documentation by HP (http://www.maths.usyd.edu.au/u/psz/ps.html#PJLref)

## Why ?
Getting screenshots from 80's metrology equipment is not always as easy as plugging in a USB storage or
capturing over LXI.

Looking for a solution I thought about using the since ever existing printer port,
so speaking to 'print' my screenshots out.

Looking around for a already existing solution, I found the project Retro-Printer.  
A piece of hardware with some software emulating a centronics printer and capturing
the data to chooseable formats, also PDF.  

For PDF them use GhostPCL.  
All in all, replacing the most common Epson-ESC/P and HP-PCL printers a very useful device.

But still not satisfied with the PDF-files in black-white the combo of spectrum analyser (SA) and retroprinter
is actual able to output, I selected one probably PCL color printer at my SA and hit 'PRINT'.

Getting a document with just the cross-hair and legends and the trace missing.  
Not very satisfying.

I assume the HP PaintJet Color printer seemd using a custom colour palette, maybe at least on the data side.
One GhostPCL may not be able to handle.

I could have chosen to solve this by requesting implementation by the GhostPCL developers.

Instead I dug deeper into PCL format and found a number of set screws I try to manipulate with this script.

## Deeper into PCL

Beeing a language developed by HP and documented well I took the trip down into.
It is based on the concept of ESC-sequences, like ESC/P from Epson is.

So direct to the core.

My SA uses the raster graphic mode. This means every line of the printed picture beeing represented by a
predefined number of pixels.

Taking a look at the actual PCL-data, I were able to capture from serial to file with another
python script paired with a parallel-to-serial converting arduino, we will see how PCL is build up.

Take a look at 'paintjet-pcl-structure' where I documented the detailed structure .
