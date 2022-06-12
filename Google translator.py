print("=====================google translator =============================")
from googletrans import Translator
translator =Translator()
text = translator.translate("My name is shoaib",dest='ur')
print(text.text)
