from flask import Flask, request, render_template

 

app = Flask(__name__)

 

@app.route('/')

def index():

    return render_template('index.html')

 

@app.route('/process', methods=['POST'])

def process():

    input_data = request.form['input_field']

    processed_output = process_input(input_data)

    return render_template('result.html', output=processed_output)

 

def process_input(input_data):

    # Your processing logic here

    # Return the processed output

    return input_data.upper()

 

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80)
