#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkiot.request.v20180120.DeleteProductTagsRequest import DeleteProductTagsRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = DeleteProductTagsRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(response)
