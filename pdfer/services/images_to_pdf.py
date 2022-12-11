import img2pdf
import glob
from .. import utils
from .base_service import Action


class ImagesToPdf(Action):
    command = "img2pdf"
    doc = "Собираю картинки в PDF`ку, аргументы - файлы или папка"

    def run_action(self):
        with open(utils.OUTPUT_PATH / f"{utils.get_random_name()}.pdf", "wb") as pdf:
            if "pdf" in self.params[0]:
                pdf.write(img2pdf.convert(*self.params))
            else:
                pdf.write(img2pdf.convert(glob.glob(self.params[0] + "\\*.jpg")))
