from flask import Flask

from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_success_predict_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url ='/predict'
    request_data_1 = {'G1': 15, 'G2': 12, 'failures' : 0, 'studytime' : 4, 'absences' : 1}
    response_1 = client.get(url, query_string= request_data_1)

    # returns 200 response with succesful admission status (1) 
    assert response_1.status_code == 200
    assert response_1.get_data() == {b'1', b'15', b'12', b'0', b'4', b'1'}


    # returns 200 response with failure admission status (0)     
    request_data_2 = {'G1': 3, 'G2': 3, 'failures' : 4, 'studytime' : 1, 'absences' : 7}
    response_2 = client.get(url, query_string= request_data_2)

    assert response_2.status_code == 200
    assert response_2.get_data() == {b'0', b'3', b'3', b'4', b'1', b'7'}


def test_invalid_argument_type():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?age=18&absences=21&health=hello'

    response = client.get(url)

    # returns 400 response with invalid argument type
    assert response.status_code == 400

def test_missing_inputs():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?age=18'

    response = client.get(url)

    # returns 400 response with missing inputs
    assert response.status_code == 400

def test_improperly_formatted_inputs():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?age=18absences=6G1=3G2=5studytime=3'

    response = client.get(url)

    # returns 400 response with improperly formatted inputs
    assert response.status_code == 400
    
def test_400_2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/%predict?age=blah&absences=2&health=3'
    
    response = client.get(url)
    
    assert response.status_code == 400