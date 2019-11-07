import requests

print(requests.get('http://www.bmtrip.com/api/v3/m1/product/list?platform=3&type=0&order_by=5&page=1&district_id[]=area_p_19&size=6').json())
