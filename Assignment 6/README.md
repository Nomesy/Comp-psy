## Dialog box exercises


2. Set the variable "session" as fixed. What happens? 

Setting session as fixed make the dialog box for that variable locked/uneditable for the participant. The value it is locked as is '1' which is what we defined it as in the code.

## Monitor and window exercises


1. How does changing "units" affect how you define your window size?



2. How does changing colorSpace affect how you define the color of your window? Can you define colors by name?

ColorSpace chagnes the way you define colour for instance 'rgb' colorSpace has the three values scale from -1 to 1 where as 'rgb1' has its three values scale from 0 to 1. This means to get the same gray with both colorSpaces you need different values [0,0,0] for 'rgb' and [0.5,0.5,0.5] for 'rgb1.'

you can define colours by name for instance the trial end message was made aquamarine by defining its like "colors = 'aquamarine'."

## Stimulus exercises


1. Write a short script that shows different face images from the image directory at 400x400 pixels in size. What does this do to the images? How can you keep the proper image dimensions and still change the size?

this will strech and compress the entirty of picture to fit into a perfect 400 by 400 pixel square, resulting in distortion if the image isnt a perfect square.

You could use scalers instead. This will increase each dimension by a proportional amount effectively keeping the proportions of the image while increasing the size.


