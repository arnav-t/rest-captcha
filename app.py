from flask import Flask, request, render_template
from captcha import getCaptchaText
import random, string, os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20*1024	# 20 kB

def randName(size):
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))

def checkExtension(fileName):
	return fileName.split('.')[1].lower() == 'jpeg'

@app.route('/', methods=['GET', 'POST'])
def solve():
	if request.method == 'GET':
		return render_template('home.html')
	elif request.method == 'POST':
		if 'image' not in request.files:
			return 'Invalid request'
		file = request.files['image']
		if file and checkExtension(file.filename):
			fileName = randName(6) + '.jpeg'
			file.save(fileName)
			captchaText = getCaptchaText(fileName)
			os.remove(fileName)
			return captchaText

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)