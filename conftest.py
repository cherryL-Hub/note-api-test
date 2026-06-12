import pytest
from pages.api_client import APICLIENT
import logging
import os

# 日志配置
logfile=os.path.join(os.path.dirname(__file__),'test.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s',
    filename=logfile,
    filemode='w',
    force=True
)

# 命令行环境参数配置(切环境)
def pytest_addoption(parser):
    parser.addoption("--env",action="store",default="prod",help="选择测试环境: prod (正式), test (测试), dev (本地开发)")

@pytest.fixture(scope="session")
def base_url(request):
    env=request.config.getoption("--env")
    urls={
        "prod": "https://practice.expandtesting.com/notes/api",
        "test": "https://test.practice.expandtesting.com/notes/api",
        "dev": "http://localhost:8080/notes/api"

    }
    return urls.get(env,urls["prod"])


# api_client fixture
@pytest.fixture(scope="session")
def api_client_fixture(base_url):
    client=APICLIENT(base_url)

    user_data={
        "email":"1921115270@qq.com",
        "password":"lx5755"
    }

    response=client.post("/users/login",data=user_data)

    assert response.status_code==200

    token=response.json()["data"]["token"]

    client.set_token(token)

    return client



