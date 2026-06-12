import requests
import pytest
import time
import logging
from pytest import raises
from pages.api_client import APICLIENT


@pytest.mark.parametrize("category",["Home","Personal","Work"])
def test_create(api_client_fixture,category):
    logging.info(f"{category}类型测试开始")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    note_data={
        "title":f"第一次创建{category}{timestamp}笔记",
        "description":f"很开心嗯对，这是{category}{timestamp}笔记内容",
        "category":category,
        "completed":False

    }

    response_create=api_client_fixture.post("/notes",data=note_data)

    assert response_create.status_code==200

    note_id=response_create.json()["data"]["id"]

    assert note_id is not None

    logging.info(f"编号:({note_id})    {category}笔记，创建成功")

    response_delete=api_client_fixture.delete(f"/notes/{note_id}")

    assert response_delete.status_code==200

    get_response=api_client_fixture.get(f"/notes/{note_id}")

    assert get_response.status_code==404

    logging.info(f"{category}删除成功")

    response_delete2=api_client_fixture.delete(f"/notes/{note_id}")

    with raises(AssertionError):
        assert response_delete2.status_code==200
    logging.info(f"{note_id}已不存在，二次删除失败断言成功")









