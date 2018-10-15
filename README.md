# GIMP Pythonfu - Reminders and Resources

~~The "full" gimp documentation here: https://www.gimp.org/docs/python/index.html~~

~~It was last updated in 2006 - long before the 2.10.X update. It is a good resource for covering the basics - but it likely will not tell you why certain plug-ins in the Python Procedure Browser aren't working as expected~~

Full gimp document here: https://developer.gimp.org/api/2.0/libgimp/index.html Up to date as of 2.8.X

## Objects

The objects within Gimp have "members" and "methods". Members are aspects about the object, while methods are actions that can be taken upon the object.

### Image Object

The image object represents an open image. 

#### Example Image member:
_image.active_layer_ is the active layer of the image. 

_image.layers_ is a list of the layers of the image.

#### Example Image Methods:
_image.add_layer(layer, position)_ adds layer to image in the position defined.

_image.resize(width, height, x, y)_ Resizes the image to size (width, height) and places the old contents at position (x,y).

### Other Objects
There are also "Channel" and "Layer" objects with their own members and methods.

## Gimpshelf Module
To be explored in the future. Used for persistent storage while GIMP is open.

## Missing and confusing parameters descriptions

**Units** expects INT32 parameter, despite the units being described as strings in the GIMP interface. Presumably use the following:  { PIXELS (0), INCHES (1), etc.. }

**Finding x and y positions of a layer** the language used by gimp and pythonfu is "offsets", because you are looking for the numbers offset from the 0,0 base coordinate. Search for plugins using the keyword "offset" to find what you're looking for.

**Position does not mean x and y at all**. The position refers to the order of the layers and the relative position of the layer in that order. 
