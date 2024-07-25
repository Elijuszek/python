import os
import aspose.words as aw

def convert_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    files = os.listdir(input_directory)
    saveOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)
    
    for filename in files:
        if filename.endswith('.png'):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.svg')
            doc = aw.Document()
            builder = aw.DocumentBuilder(doc)
            shape = builder.insert_image(input_path)
            shape.get_shape_renderer().save(output_path, saveOptions)

input_directory = './'
output_directory = './Converted'
convert_files(input_directory, output_directory)
