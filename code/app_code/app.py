from flask import Flask
from flask import Flask, render_template, Response, request, jsonify
from combine_file import predict_all
from utils import gen
from Modules.voice_model import record_voice

app = Flask(__name__)


@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_label_text', methods=['POST'])
def get_label_text():

    # Get the value of the input field from the JSON request
    data = request.get_json()
    inputValue = data['inputValue']

    res = predict_all(inputValue)

    print('Final result: ', res)
    print('-------------------------------------------------------------------------------------------------------------')
    return res


@app.route('/record_voice', methods=['POST'])
def predict_emotion():
    record_voice.record_audio()
    #print('done')

    #return render_template('index.html')



@app.route('/', methods=['GET', 'POST'])
def index():
    global capture_images

    if request.method == 'POST':
        if request.form.get('start'):
            capture_images = True
            print('start')
        elif request.form.get('stop'):
            capture_images = False


    return render_template('index.html')

def start_capture():
    global capture_images
    capture_images = True

def stop_capture():
    global capture_images
    capture_images = False

if __name__ == "__main__":
  app.run()
