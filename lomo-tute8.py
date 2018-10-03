#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=X0_a6U6PkCA
# Feedback welcome: jacksonbates@hotmail.com
# Adapted by Victoria Pleavin to reflect GIMP 2.10.X updates.

from gimpfu import *


def lomoChoice(image, drawable, direction):
    num_points = 10
    #Note: updated gimpfu scripts require array to be a FLOAT instead of an INT.
    #Note: instead of matching the 256 x 256 coordinates in the histogram, it treats it like a scale of 0 to 1. To make the conversion, find the place on the graph then divide the number by 256.
    #Salty opinion: this is a pretty non-intuitive change and should have been mentioned in the plugin notes.
    s_curve = [0.0, 0.0, 0.25, 0.38, 0.5, 0.5, 0.75, 0.625, 1.0, 1.0]
    inverted_s_curve =  [0.0, 0.0, 0.38, 0.25, 0.5, 0.5, 0.625, 0.75, 1.0, 1.0]
    pdb.gimp_drawable_curves_spline(drawable, 1, num_points, s_curve)
    pdb.gimp_drawable_curves_spline(drawable, 2, num_points, s_curve)
    pdb.gimp_drawable_curves_spline(drawable, 3, num_points, inverted_s_curve)
    #add new layer & Set to 'overlay'
    opacity_100 = 100
    # variables are (image, width, height, layer type, layer name, opacity, mode)
    layer = pdb.gimp_layer_new(image, image.width, image.height, 0, "Overlay", opacity_100, 23)
    layer_position = 0
    pdb.gimp_image_insert_layer(image, layer, None, layer_position)
    # blend arguments and call to function
    blend_mode = 0
    paint_mode = 0
    gradient_type = 0
    offset = 0
    repeat = 0
    reverse = False
    supersample = False
    max_depth = 1
    threshold = 0
    dither = True
    x2 = layer.width / 2
    y2 = layer.height / 2
    #choice time
    if direction == 0: #North - layer.width/2, 0
        x1 = layer.width/2
        y1 = 0
    elif direction == 1: #NE - Layer.width, 0
        x1 = layer.width
        y1 = 0
    elif direction == 2: #E - Layer.width, layer.height/2
        x1 = layer.width
        y1 = layer.height/2
    elif direction == 3: #SE - Layer.width, layer.height
        x1 = layer.width
        y1 = layer.height
    elif direction == 4: #S - Layer.width/2, Layer.height
        x1 = layer.width/2
        y1 = layer.height
    elif direction == 5: #SW - 0m Layer.height
        x1 = 0
        y1 = layer.height
    elif direction == 6: #W - 0, Layer.height/2
        x1 = 0
        y1 = layer.height/2
    elif direction == 7:     #NW - 0, 0
        x1 = 0
        y1 = 0
    
    pdb.gimp_edit_blend(layer, blend_mode, paint_mode, gradient_type, opacity_100, offset, repeat, reverse, supersample, max_depth, threshold,  dither, x1, y1, x2, y2)
    #merge all layers
    layer = pdb.gimp_image_merge_visible_layers(image, 0)
    #pdb.gimp_displays_flush()


register(
    "python-fu-lomotute8",
    "Lomo effect",
    "Creates a lomo effect on a given image",
    "Victoria Pleavin", "Victoria Pleavin", "2018",
    "Lomo choice",
    "RGB", # type of image it works on (*, RGB, RGB*, RGBA etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_OPTION, "direction", "Direction: ", 0,
            (
                ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
            )
        )
    ],
    [],
    lomoChoice, menu="<Image>/Filters")  # second item is menu location

main()
