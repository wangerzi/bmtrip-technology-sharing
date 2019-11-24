def encode(lng, lat):
    """传入经度和纬度，生成 geoHash"""
    lngStr = splitByRange(lng, -180, 180)
    latStr = splitByRange(lat, -90, 90)
    return mergeLngLat(lngStr, latStr)
def splitByRange(originNumber, start, end, limit=11):
    """传入数字以及二分范围，返回二分区间编码二进制"""
    pass
def mergeLngLat(lngStr, latStr):
    """偶数位放经度，奇数位放纬度，合并新字符串，并转化为32进制"""
    pass

def decode(geohash):
    """传入geohash，返回经纬度"""
    lngStr, latStr = splitGeoHash(geohash)
    lng = restoreByRange(lngStr, -180, 180)
    lat = restoreByRange(latStr, -90, 90)
    return lng, lat
def splitGeoHash(geohash):
    """解码geohash，从32进制解码为二进制，奇数位拼接是经度，偶数位拼接是纬度"""
    pass
def restoreByRange(dstStr, start, end):
    """根据目标字符串和二分范围解码目标字符串"""
    limit = len(dstStr)
    pass
