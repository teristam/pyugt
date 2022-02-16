#%%
from googletrans import Translator
translator = Translator()
s = translator.translate('このまま、 続けたら・ ・ ・・何を言われるか・ ・ ・ ・怖いんだ。',src='ja', dest='zh-tw')
print(s.text)
# %%
from mss import mss

with mss() as sct:
    sct.shot(mon=2)
# %%
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


img = Image.open('debugtranslatepreproc.png')
img
#%%
ocrtext = pytesseract.image_to_string(img, lang='jpn',config='--oem 0')
ocrtext
# %%
