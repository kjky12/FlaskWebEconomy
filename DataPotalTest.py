# 1. 라이브러리 임포트 및 버전 확인하기
import PublicDataReader as pdr
import sqlite3
from datetime import datetime


global con

E_SAVE_TYPE_DB = 1
E_SAVE_TYPE_HTML = 2

#1: DB로 저장, 2HTML로 저장
nSaveType = E_SAVE_TYPE_DB

# DB 생성
now = datetime.now()

if nSaveType == E_SAVE_TYPE_DB :
    con = sqlite3.connect(now.strftime('%Y%m%d_%H%Mtest.db'))

#else : # nSaveType == 2:
    #strHtmlPath = now.strftime('%Y%m%d_%H%M_{0}test.html'.format(category))

def SaveData(df, category) :
    if nSaveType == E_SAVE_TYPE_DB :
        df.to_sql(category, con, if_exists="append", index=True)
    else :
        strHtmlPath = now.strftime('%Y%m%d_%H%M_{0}test.html'.format(category))
        df.to_html(strHtmlPath)



now = datetime.now()

print(pdr.__version__)


# 2. 공공 데이터 포털 OpenAPI 서비스 인증키 입력하기
serviceKey = 'sEkWhWER%2Fsn%2FgRDrtuBW2BHO%2BE65ORsVQQuDOqMnvZOa%2Fh6Ir0L6ppED3VIkx%2BqSEFdkhygEpOHsOQfQqzq56w%3D%3D'

# 3. 소상공인 상가업소 정보 조회 OpenAPI 인스턴스 생성하기
# debug: True이면 모든 메시지 출력, False이면 오류 메시지만 출력 (기본값: False)
si = pdr.StoreInfo(serviceKey, debug=True)

# 4. 데이터프레임으로 자료 조회하기

# 4-1. 지정상권
category = "지정상권"

key = "9174"

df = si.read_data(category=category, key=key)
SaveData(df, category)
SaveData(df, category)
print(category + "Fin")

# 4-2. 반경상권
category = "반경상권"

radius = 500
cx = 127.03641615737838
cy = 37.50059843782878

df = si.read_data(category=category, radius=radius, cx=cx, cy=cy)
SaveData(df, category)
print(category + "Fin")
# 4-3. 사각형상권
category = "사각형상권"

minx = 127.0327683531071
miny = 37.495967935149146
maxx = 127.04268179746694
maxy = 37.502402894207286

df = si.read_data(category=category, minx=minx, miny=miny, maxx=maxx, maxy=maxy)
SaveData(df, category)
print(category + "Fin")
# 4-4. 행정구역상권
category = "행정구역상권"

divId = 'adongCd'
key = '1168058000'

df = si.read_data(category=category,divId=divId, key=key)
SaveData(df, category)
print(category + "Fin")
# 4-5. 단일상가
category = "단일상가"

key = '11757465'

df = si.read_data(category=category, key=key)
SaveData(df, category)
print(category + "Fin")
# 4-6. 건물상가
category = "건물상가"

key = '1168011000104940000004966'

df = si.read_data(category=category, key=key)
SaveData(df, category)
print(category + "Fin")
# 4-7. 지번상가
category = "지번상가"

key = '1165010100108120002'
indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)
SaveData(df, category)
print(category + "Fin")
# 4-8. 행정동상가
category = "행정동상가"

divId = 'adongCd'
key = '1168064000'
indsLclsCd = 'Q'

df = si.read_data(category=category, divId=divId, key=key, indsLclsCd=indsLclsCd)
SaveData(df, category)
print(category + "Fin")
# 4-9. 상권상가
category = "상권상가"

key = '9368'
indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)
SaveData(df, category)
print(category + "Fin")
# 4-10. 반경상가
category = "반경상가"

radius = '500'
cx = 127.03641615737838
cy = 37.50059843782878
indsLclsCd = 'Q'

df = si.read_data(category=category, radius=radius, cx=cx, cy=cy, indsLclsCd=indsLclsCd)
SaveData(df, category)
print(category + "Fin")
# 4-11. 사각형상가
category = "사각형상가"

minx = 127.0327683531071
miny = 37.495967935149146
maxx = 127.04268179746694
maxy = 37.502402894207286
indsLclsCd = 'Q'

df = si.read_data(category=category, minx=minx, miny=miny, maxx=maxx, maxy=maxy, indsLclsCd=indsLclsCd)
SaveData(df, category)
print(category + "Fin")
# 4-12. 다각형상가
category = "다각형상가"

key = 'POLYGON((127.02355609555755 37.504264372557095, 127.02496157306963 37.50590702991155, 127.0270858825753 37.50486867039889, 127.02628121988377 37.503489842823114))'
indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)
SaveData(df, category)
print(category + "Fin")
# 4-13. 업종별상가
category = "업종별상가"

divId = 'indsLclsCd'
key = 'Q'

df = si.read_data(category=category, divId=divId, key=key)
SaveData(df, category)
print(category + "Fin")
# 4-14. 수정일자상가
category = "수정일자상가"

key = '20200101'
indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)
SaveData(df, category)
print(category + "Fin")
# 4-15. 업종대분류
category = "업종대분류"

df = si.read_data(category=category, key=key)
SaveData(df, category)
print(category + "Fin")
# 4-16. 업종중분류
category = "업종중분류"

indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)
SaveData(df, category)
print(category + "Fin")

# 4-17. 업종소분류
category = "업종소분류"

indsLclsCd = 'Q'
indsMclsCd = 'Q01'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd, indsMclsCd=indsMclsCd)
SaveData(df, category)
print(category + "Fin")


if nSaveType == E_SAVE_TYPE_DB :
    con.close()