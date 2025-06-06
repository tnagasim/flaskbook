from pathlib import Path

from PIL import Image

basedir = Path(__file__).parent.parent


def load_image(request, reshaped_size=(256, 256)):
    """画像の読み込み"""
    filename = request.json["filename"]
    dir_image = str(basedir / "data" / "original" / filename)
    image_obj = Image.open(dir_image).convert("RGB")
    image = image_obj.resize(reshaped_size)
    return image, filename
