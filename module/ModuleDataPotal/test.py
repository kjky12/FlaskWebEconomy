
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



serviceKey = 'sEkWhWER%2Fsn%2FgRDrtuBW2BHO%2BE65ORsVQQuDOqMnvZOa%2Fh6Ir0L6ppED3VIkx%2BqSEFdkhygEpOHsOQfQqzq56w%3D%3D'

si = pdr.StoreInfo(serviceKey, debug=True)


# # 4-15. 업종대분류
# category = "업종대분류"
# key = "xml"
# key = '20200101'
#
# df = si.read_data(category=category)
# SaveData(df, category)
# print(category + "Fin")

# # 4-4. 행정구역상권
# category = "행정구역상권"
#
# divId = 'ctprvnCd'
# key = '30'
#
# df = si.read_data(category=category,divId=divId, key=key)
# SaveData(df, category)
# print(category + "Fin")


# 4-10. 반경상가
category = "반경상가"

radius = '2000'
cx = 127.3671313
cy = 36.3583832
indsLclsCd = 'Q'

adf = []
nPageNum = 1
while True :
    try :
        df = si.read_data(category=category, pageNo=nPageNum, radius=radius, cx=cx, cy=cy, indsLclsCd=indsLclsCd)
        #df = si.read_data(category=category, radius=radius, cx=cx, cy=cy, indsLclsCd=indsLclsCd, type="xml", pageNo=nPageNum)

        if type(df).__name__ != 'string' :
            adf.append(df)
            print(category + "Fin{0}\t{1}}\n".format(nPageNum, len(df)))
        else :
            print(category + "Fail{0}\n".format(nPageNum))

    except Exception as e :
        print(e)
        break
    nPageNum += 1



if nSaveType == E_SAVE_TYPE_DB :
    for df in adf:
        try:
            SaveData(df, category)

        except Exception as e:
            print(e)



    con.close()