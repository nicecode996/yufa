# -*- coding: utf-8 -*-
# author:jiayanzi

from common.interface import InterFace

class DeviceActivate:

    def test_get_device_list(self):
        TestInterface=InterFace()
        url_path1="/bbox-service/api/device/page"
        TestInterface.set_url(url_path1)
        headers={"User-Agent":"bb-device","Content-Type":"application/json","param":'{"userId":1,"tenantId":1,'
                                                                                    '"appId":"test"}'}
        response=TestInterface.get(TestInterface.url,headers)
        return response.text

aaa=DeviceActivate()
bbb=aaa.test_get_device_list()
print(bbb)





