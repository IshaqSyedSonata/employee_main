from fastapi.testclient import TestClient

from main import app
# from routers.index import emp

client = TestClient(app)

def test_main_app():
    response  = client.get("")
    assert  response.status_code == 200
    assert response.json() == {"Message":"Hello"}
    
# clientemp = TestClient(emp)
# def test_e():
#     response = clientemp.get("/")
#     # print("s")
#     assert response.status_code == 200
#     # assert response.json() == {
#     #     "name": "Ishaq",
#     #     "email": "Ishaq.syed@sonata-software.com",
#     #     "is_active": "true",
#     #     "address": "address 2",
#     #     "id": 1
#     # }