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
    request_data_1 = {'G1': 20, 'G2': 20, 'failures' : 0, 'studytime' : 4, 'absences' : 1}
    response_1 = client.get(url, query_string= request_data_1)

    # returns 200 response with succesful admission status (1) 
    assert response_1.status_code == 200
    assert response_1.get_data() == b'{"AdmissionStatus":1,"G1":20,"G2":20,"absences":1,"failures":0,"studytime":4}\n'


    # returns 200 response with failure admission status (0)     
    request_data_2 = {'G1': 3, 'G2': 3, 'failures' : 4, 'studytime' : 1, 'absences' : 7}
    response_2 = client.get(url, query_string= request_data_2)

    assert response_2.status_code == 200
    assert response_2.get_data() == b'{"AdmissionStatus":0,"G1":3,"G2":3,"absences":7,"failures":4,"studytime":1}\n'


def test_invalid_argument_type():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url1 = '/predict?G1=0&G2=hello&failures=0&studytime=4&absences=0'

    response1 = client.get(url1)

    # returns 400 response with invalid argument type
    assert response1.status_code == 400
    assert response1.get_data() == b'{"Error":"Missing inputs or inputs invalid!"}\n'


    # returns 400 response with invalid argument type
    url2 = '/predict?G1=0&G2=2&failures=asdf&studytime=asdf&absences=0'
    response2 = client.get(url2)
    assert response2.status_code == 400
    assert response2.get_data() == b'{"Error":"Missing inputs or inputs invalid!"}\n'


def test_missing_inputs():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?G1=0&G2=hello&failures=0&studytime=4'

    response = client.get(url)

    # returns 400 response with missing inputs
    assert response.status_code == 400
    assert response.get_data() == b'{"Error":"Missing inputs or inputs invalid!"}\n'


def test_improperly_formatted_inputs():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=0&G1=0&G2=hello&studytime=4&absences=0'

    response = client.get(url)

    # returns 400 response with improperly formatted inputs
    assert response.status_code == 400
    assert response.get_data() == b'{"Error":"Missing inputs or inputs invalid!"}\n'

    
