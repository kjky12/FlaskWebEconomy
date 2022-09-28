# FlaskWebEconomy

python.exe -m pip install --upgrade pip
pip install Flask

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
- git pull- 
6. 파이썬 패키지를 설치한다.
- pip install -r requirements.txt
 