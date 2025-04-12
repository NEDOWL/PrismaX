from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Handle the redirect logic here
    # For example, you can retrieve query parameters
    code = request.args.get('code')
    state = request.args.get('state')
    
    # Process the code and state as needed
    return f"Received code: {code}, state: {state}"

if __name__ == '__main__':
    app.run(host='194.87.95.213', port=8000)