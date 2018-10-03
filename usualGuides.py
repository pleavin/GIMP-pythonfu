#!/usr/bin/env python

# Program by Victoria Pleavin
# A gift for myself: The feature I've wanted most from GIMP.
# Let's you with three clicks add horizontal and verticle guides at 50% of image size, or at 1/3 and 2/3 of image size. 

from gimpfu import *

def usualGuides (image, drawable, guideSel):
    #function code goes here...
    if guideSel == 0:
        guide = pdb.gimp_image_add_hguide(image, image.height/2)
        guide = pdb.gimp_image_add_vguide(image, image.width/2)
    elif guideSel == 1:
        guide = pdb.gimp_image_add_hguide(image, image.height/3)
        guide = pdb.gimp_image_add_hguide(image, image.height*2/3)
        guide = pdb.gimp_image_add_vguide(image, image.width/3)
        guide = pdb.gimp_image_add_vguide(image, image.width*2/3)
    elif guideSel == 2:
        guide = pdb.gimp_image_add_hguide(image, image.height/2)
        guide = pdb.gimp_image_add_vguide(image, image.width/2)
        guide = pdb.gimp_image_add_hguide(image, image.height/3)
        guide = pdb.gimp_image_add_hguide(image, image.height*2/3)
        guide = pdb.gimp_image_add_vguide(image, image.width/3)
        guide = pdb.gimp_image_add_vguide(image, image.width*2/3)


register(
    "python-fu-usualGuides",
    "Adds typically used guides",
    "Adds guides to indicate the centre of the image, or to break the image in thirds.",
    "Victoria Pleavin","Victoria Pleavin","2018",
    "Add typical guides",
    "*", #type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        #basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        #list of GUI/custom parameters.
        #(PF_INT, "int_var", "int", 50),
        #(PF_FLOAT, "float_var", "float", 3.14159),
        #(PF_STRING, "string_var", "string", "Awesomesauce!"),
        #(PF_VALUE, "value_var", "value", "Is this the same as above?!"),
        #(PF_TEXT, "text_var", "text", "This accepts a longer string of text"),
        #(PF_COLOR, "color_var", "color", (1.0, 1.0, 1.0)),
        #(PF_COLOUR, "colour_var", "colour UK sp. :)",(255.0, 255.0, 255.0)),
        #(PF_IMAGE, "image_var", "image", None),
        #(PF_LAYER, "layer_var", "layer", None),
        #(PF_CHANNEL, "channel_var", "channel", None),
        #(PF_DRAWABLE, "drawable_var", "drawable", None),
        #(PF_TOGGLE, "toggle_var", "toggle", 1),
        #(PF_BOOL,   "boolean_var", "Boolean", True),
        #(PF_RADIO, "radio_var", "radio", "radio1_value",
        #    (
        #        ("radio1_label", "radio1_value"),
        #        ("radio2_label", "radio2_value")
        #    )
        # ),
        (PF_OPTION, "guideSel", "option", 0,
            ("50%", "1/3rd and 2/3rds", "Both")
         ),
        #(PF_SPINNER, "spinner_var", "spinner", 10, (1, 10, 0.5)),
        #(PF_SLIDER, "slider_var",  "slider", 100, (0, 100, 1)),
        #(PF_ADJUSTMENT, "adjustment_var", "adjustment", 10, (1, 10, 1)),
        #(PF_FILE, "file_var", "file", ""),
        #(PF_DIRNAME, "dirname_var", "dirname", "/tmp"),
        #(PF_FONT, "font_var", "font", "Sans"),
        #(PF_BRUSH, "brush_var", "brush", None),
        #(PF_PATTERN, "pattern_var", "pattern", None),
        #(PF_GRADIENT, "gradient_var", "gradient", None),
        #(PF_PALETTE, "palette_var",  "palette", ""),
    ],
    [], #where "results" go. Never is used.
    usualGuides, menu="<Image>/Image") #second item is menu location

main()
