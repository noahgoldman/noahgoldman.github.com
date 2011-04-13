import os
import string

for root, dirs, files in os.walk('/home/noah/projects/noahgoldman.github.com/_site'):
	for file in files:
		if file.find('.html') != -1:
			os.chdir(root)
			os.system('java -jar $HOME/libs/compressors/htmlcompressor.jar --compress-js --type html -o ' + file + ' ' + file)
		elif file.find('.css') != -1:
			os.chdir(root)
			os.system('java -jar $HOME/libs/compressors/yuicompressor-2.4.2.jar --type css --line-break 1000 -o ' + file + ' ' + file)
