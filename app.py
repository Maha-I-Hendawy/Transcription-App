. venvfrom flask import Flask, render_template, url_for, request, redirect
import speech_recognition as sr

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')


@app.route('/', methods=['GET', 'POST'])
def home():
	transcript = ""
	if request.method == 'POST':
		
		if 'file' not in request.files:
			return redirect(request.url)

		file = request.files['file']
		if file.filename == "":
			return redirect(request.url)

		if file:
			recognizer = sr.Recognizer()
			audioFile = sr.AudioFile(file)
			with audioFile as source:
				data = recognizer.record(source)
			transcript = recognizer.recognize_google(data, key=None)
		
	return render_template('home.html', transcript=transcript)


if __name__ == '__main__':
	app.run()