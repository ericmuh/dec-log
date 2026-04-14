import os
import uuid
from io import BytesIO

from PIL import Image, ImageOps


ALLOWED_IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "webp"}


def is_allowed_image(filename: str) -> bool:
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS
    )


def _normalize_image(image: Image.Image) -> Image.Image:
    if image.mode in ("RGBA", "LA"):
        background = Image.new("RGB", image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[-1])
        return background
    return image.convert("RGB")


def save_profile_picture(file_storage, upload_folder: str) -> str:
    os.makedirs(upload_folder, exist_ok=True)

    filename = f"{uuid.uuid4().hex}.jpg"
    output_path = os.path.join(upload_folder, filename)

    image = Image.open(BytesIO(file_storage.read()))
    image = _normalize_image(image)
    image = ImageOps.fit(image, (300, 300), method=Image.Resampling.LANCZOS)
    image.save(output_path, format="JPEG", quality=90, optimize=True)

    return os.path.join("uploads", filename)


def remove_file_if_exists(file_path: str, base_folder: str) -> None:
    if not file_path:
        return

    absolute_path = os.path.join(base_folder, file_path)
    if os.path.exists(absolute_path):
        os.remove(absolute_path)
