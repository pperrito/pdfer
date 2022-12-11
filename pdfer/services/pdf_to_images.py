import pdf2image
from .. import utils
from .base_service import Action


class PdfToImages(Action):
    command = "pdf2img"
    doc = "Перевожу pdf в картинки, аргументы - файлы"

    def run_action(self):
        for file in self.params:
            output = utils.OUTPUT_PATH / utils.get_random_name()
            output.mkdir()
            pdf2image.pdf2image.convert_from_path(
                file, output_folder=output, fmt="jpeg"
            )
