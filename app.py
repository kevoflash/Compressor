from flask import Flask, request, render_template
import moviepy.editor as mp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        bitrate = int(request.form['bitrate'])
        clip = mp.VideoFileClip(file)
        compressed_clip = clip.resize(newsize=(clip.size[0]//2, clip.size[1]//2)).write_videofile('compressed_video.mp4', bitrate=f"{bitrate}k")
        return render_template('index.html', message="Video compressed successfully!")
    return render_template('index.html', message=None)

if __name__ == '__main__':
    app.run(debug=True)
