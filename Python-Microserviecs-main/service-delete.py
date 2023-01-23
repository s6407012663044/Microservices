from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/delete', methods=['DELETE'])
def delete():
    # Get the user's login information from the request
    user = request.form.get('username')
        # passwd = request.form.get('password')
        # name = request.form.get('name')

    _user = us.find_username(user)
    data = [x for x in _user if x["user"]==user]
    # return jsonify(_user)
    #Get Data
    if data:
        us.user_delete(user)
        return jsonify({'message': 'Delete successfully.'}), 200
    else:
        return jsonify({'message': 'Cannott Delete.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1