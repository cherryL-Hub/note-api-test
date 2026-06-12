import requests

class APICLIENT:
    def __init__(self,base_url):
        self.url=base_url
        self.session=requests.Session()

    def set_token(self,token):
        self.session.headers.update({"x-auth-token":token})


    def post(self,endpoint,data=None):
        url=f"{self.url}{endpoint}"
        return self.session.post(url,json=data)

    def get(self,endpoint):
        url=f"{self.url}{endpoint}"
        return self.session.get(url)

    def delete(self,endpoint):
        url=f"{self.url}{endpoint}"
        return self.session.delete(url)





