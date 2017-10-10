import os
from flask import Flask,request,render_template

music_dir = os.path.join(os.getcwd(),'static','music')
image_dir = os.path.join(os.getcwd(),'static','image')
video_dir = os.path.join(os.getcwd(),'static','video')

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
	music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
	music_files_number = len(music_files)
	return render_template("index.html",title='Home',music_files_number = music_files_number, music_files = music_files)

if __name__=='__main__':
	app.run(host = '0.0.0.0', debug=True)
