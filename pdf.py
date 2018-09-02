# coding = utf-8

import os
import img2pdf

ld = os.listdir()
for d in ld:
	if os.path.isdir(d):
		try:
			with open(d + ".pdf", "wb") as f:
			    f.write(img2pdf.convert([(d  + '/' + i).encode() for i in os.listdir(d) if i.endswith((".png", ".jpg"))]))
		except:
			print(d)