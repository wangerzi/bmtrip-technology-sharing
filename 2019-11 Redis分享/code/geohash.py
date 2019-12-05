import base64
import math

def encode(lng, lat):
    """传入经度和纬度，生成 geoHash"""
    print('计算经度Hash')
    lngStr = splitByRange(lng, -180, 180)
    print('计算纬度Hash')
    latStr = splitByRange(lat, -90, 90)
    print(lngStr, latStr)
    mergeStr = mergeLngLat(lngStr, latStr)
    print(mergeStr)
    return base32Encode(mergeStr)
def base32Encode(byteStr):
    base32Str = '0123456789bcdefghjkmnpqrstuvwxyz'
    code = ''
    for i in range(0, math.ceil(len(byteStr)/5)):
        code += base32Str[int(byteStr[i*5:(i+1)*5], 2)]
    return code
def base32Decode(code):
    base32Str = '0123456789bcdefghjkmnpqrstuvwxyz'
    base32Map = {}
    for i in range(0, len(base32Str)):
        print('Current:', i, 'bin:', bin(i))
        base32Map[base32Str[i]] = bin(i).strip('0b').zfill(5)
    print(base32Map)
    byteStr = ''
    for i in code:
        byteStr += base32Map[i]
    return byteStr
def splitByRange(originNumber, start, end, limit=11):
    """传入数字以及二分范围，返回二分区间编码二进制"""
    result = ''
    for i in range(0, limit):
        center = start + (end - start) / 2
        print('总区间：[{}, {}]，左区间：[{}, {})，右区间：[{}, {}]，结果：'.format(start, end, start, center, center,
            end), '0' if (originNumber<center) else '1')
        if originNumber < center:
            result += '0'
            end = center
        else:
            result += '1'
            start = center
    return result
def mergeLngLat(lngStr, latStr):
    """偶数位放经度，奇数位放纬度，合并新字符串，并转化为32进制"""
    result = ''
    for i in range(0, len(lngStr)):
        result += (lngStr[i] + latStr[i])
    return result

def decode(geohash):
    """传入geohash，返回经纬度"""
    lngStr, latStr = splitGeoHash(geohash)
    print(lngStr, latStr)
    lng = restoreByRange(lngStr, -180, 180)
    lat = restoreByRange(latStr, -90, 90)
    return lng, lat
def splitGeoHash(geohash):
    """解码geohash，从32进制解码为二进制，奇数位拼接是经度，偶数位拼接是纬度"""
    byteStr = base32Decode(geohash)
    print(byteStr)
    lngStr = ''
    latStr = ''
    for i in range(0, len(byteStr)):
        if i % 2:
            lngStr += byteStr[i]
        else:
            latStr += byteStr[i]
    return lngStr, latStr
def restoreByRange(dstStr, start, end):
    """根据目标字符串和二分范围解码目标字符串"""
    limit = len(dstStr)
    return 1

def main():
    geoHash = encode(116.3915044069,39.9011604105)
    # geoHash = encode(121.43960190000007,31.1932993)
    print(geoHash)
    lng, lat = decode('wx4f1')
    print(lng, lat)

main()
