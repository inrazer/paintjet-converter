# paintjet-converter
Primarily designed for converting PaintJet Color PCL-data from 80's Rohde &amp; Schwarz spectrum analysers
or other devices outputting this format of data.

Note: Script was designed to run with Python 2.7, review for Python 3 following.
I have kind a linking for old tech ;-)

## Why ?

Getting screenshots from 80's metrology equipment is not always as easy as plugging in a USB storage or
capturing over LXI.

Looking for a solution I thought about using the since ever existing printer port,
so speaking to 'print' my screenshots out.

Looking around for a still existing solution, I found the project Retro-Printer. 
Replacing the most common Epson-ESC/P and HP-PCL printers a very useful device.

But still not satisfied with the PDF-files in black-white the combo of spectrum analyser (SA) and retroprinter
is able to output, I selected one, probably PCL, color printers at my SA and hit 'PRINT'.

I got an document with an empty cross-hair and legends, the trace was missing.

Digging down the rabbit hole, this historical printer seems be using a custom colour palette, GhostPCL isn't
able to handle.

I could have chosen to solve this by requesting implementation by the GhostPCL developers.

I dug deeper into PCL format and found a number of set screws I try to manipulate with this project.

## Deeper into PCL

Beeing a language developed by HP and documented well (just search the web) I took the trip down into.
It is based on the concept of ESC-sequences, like ESC/P from Epson is.

So direct to the core.

My SA uses the raster graphic mode. This means every line of the printed picture beeing represented by a
predefined number of pixels.

Taking a look at the actual PCL-data, I were able to capture from serial to file with another
python script paired with a parallel-to-serial converting arduino, we will see how PCL is build up.

Take a look at the file where I documented the structure.
