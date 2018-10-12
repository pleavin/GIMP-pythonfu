# GIMP-pythonfu

The "full" gimp documentation here: https://www.gimp.org/docs/python/index.html
It was last updated in 2006 - long before the 2.10.X update. 

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

