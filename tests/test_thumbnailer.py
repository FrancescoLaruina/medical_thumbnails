import tempfile
import SimpleITK as sitk
import numpy as np
import PIL.Image
from medical_thumbnails import thumbnailer


def test_build_parser():
    parser = thumbnailer.build_parser()
    input_list = ['in_fname', 'out_fname', '25']
    args = parser.parse_args(input_list)
    assert args.inp == input_list[0]
    assert args.out == input_list[1]
    assert args.size == int(input_list[2])

def test_convert_to_8bit():
    img_16bit = np.random.randint(0, 65536, size=(50,50))
    img_8bit = thumbnailer.convert_to_8bit(img_16bit)
    assert img_8bit.min() == 0
    assert img_8bit.max() == 255

def test_load_image():
    img_array = np.random.randint(0, 256, size=(40,50))
    sitk_img = sitk.GetImageFromArray(img_array)
    with tempfile.NamedTemporaryFile(suffix='.nii') as out_fname:
        sitk.WriteImage(sitk_img, out_fname.name)
        reloaded_img = np.asarray(thumbnailer.load_image(out_fname.name))
    assert reloaded_img.shape == img_array.shape
    # assert np.all(reloaded_img == sitk.GetArrayFromImage(sitk_img))
           
def test_save_thumbnail():
    img_array = np.random.randint(0, 256, size=(50,50), dtype='uint8')
    img = PIL.Image.fromarray(img_array)
    with tempfile.NamedTemporaryFile(suffix='.png') as out_fname:
        thumbnailer.save_thumbnail(img, out_fname.name, 50)
        reloaded_img = np.asarray(PIL.Image.open(out_fname.name))
    assert reloaded_img.shape == img_array.shape
    assert np.all(reloaded_img == img_array)
