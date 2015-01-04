
from wand.api import library
import wand.color
import wand.image

svg_file = file('test.svg');
output_file_name = 'test_out.png';

with wand.image.Image() as image:
    with wand.color.Color('transparent') as background_color:
        library.MagickSetBackgroundColor(image.wand, 
                                         background_color.resource) 
    image.read(blob=svg_file.read(), "svg")
    png_image = image.make_blob("png32")

with open(output_filename, "wb") as out:
    out.write(png_image)

