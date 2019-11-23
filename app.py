from flask import Flask, request, jsonify
import serial
app = Flask(__name__)


@app.route('/data/', methods=['GET'])
def respond():

    data = {'left': 'nothing', 'right': 'nothing', 'center': 'nothing'}

    print('start')
    port = "/dev/tty.HC-05-SPPDev"
    #arr = []
    # Start communications with the bluetooth unit
    bluetooth = serial.Serial(port, 9600)
    print("Connected")
    # bluetooth.flushInput()  # This gives the bluetooth a little kick

    input_data = bluetooth.readline().decode("utf-8")

    #string_data = str(input_data)

    # print(type(input_data))

    index_arr = []

    for idx, val in enumerate(input_data):

        if val == ' ':

            index_arr.append(idx)

    #index = input_data.index(' ')
    print(input_data)

    if len(index_arr) == 1:

        left_side = input_data[0:index_arr[0]]
        right_side = input_data[index_arr[0]+1:len(input_data)-1]
        center = 0

    else:

        left_side = input_data[0:index_arr[0]]
        right_side = input_data[index_arr[0]+1:index_arr[1]]
        center = input_data[index_arr[1]+1:len(input_data)]

    data['left'] = left_side
    data['right'] = right_side
    data['center'] = center

    #data[0] = input_data

    print(input_data)

    return jsonify(data)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, port=3000)
