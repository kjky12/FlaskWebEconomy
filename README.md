# FlaskWebEconomy

#Runtime : Python 3.10.5

python.exe -m pip install --upgrade pip
pip install Flask
pip install importlib
pip install --upgrade PublicDataReader


pip freeze > requirements.txt

pythonanywhere 환경구축
1. bash에 들어간다.
2. 가상환경을 만든다
- mkvirtualenv --python=python3.10 venvFlaskWebEconomy
3. 가상환경을 실행한다.
- workon venvFlaskWebEconomy
4. 깃을 가져온다.
- git clone https://github.com/kjky12/FlaskWebEconomy.git
5. 경로를 이동하고 Git update를 수행한다.
- cd FlaskWebEconomy
- git pull
6. 파이썬 패키지를 설치한다.
- pip install -r requirements.txt
 
###Reference
Struct : https://github.com/jainamoswal/Flask-Example/tree/main/modules
git clone : https://github.com/jainamoswal/Flask-Example.git

pythonanywhere 참고
https://wings2pc.tistory.com/entry/%EC%9B%B9-%EC%95%B1%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-Python-Flask-Pythonanywhere-%EB%B0%B0%ED%8F%AC-%ED%95%98%EA%B8%B0

#NaverMap관련
사용량
https://console.ncloud.com/naver-service/application
공식Doc
https://guide.ncloud-docs.com/docs/ko/naveropenapiv3-maps-web-sdk-v3-start
참고 Git
https://github.com/navermaps/maps.js.ncp/tree/master/examples/map

####
HTML 참고
버거메뉴 및 여러 참고 HTML참고
https://github.com/you-dont-need/You-Dont-Need-JavaScript#quick-links