# 실행 전 필요 설정

## 1. Gmail API 인증서 설정

1. Google Cloud Console 접속: Google 계정으로 Google Cloud Console에 로그인합니다.

2. 새 프로젝트 생성: 상단의 프로젝트 선택 드롭다운에서 '새 프로젝트'를 클릭하여 새로운 프로젝트를 만듭니다 (예: My Airflow Project).

3. Gmail API 활성화:

    - 좌측 메뉴에서 **'API 및 서비스' > '라이브러리'**로 이동합니다.

    - 검색창에 "Gmail API"를 검색하고 선택한 뒤, '사용 설정' 버튼을 클릭합니다.

4. OAuth 동의 화면 구성:

    - 좌측 메뉴에서 **'API 및 서비스' > 'OAuth 동의 화면'**으로 이동합니다.

    - **'User Type'**은 **'외부'**를 선택하고 '만들기'를 클릭합니다.

    - 앱 이름(예: Airflow Mailer), 사용자 지원 이메일, 개발자 연락처 정보만 입력하고 다른 항목은 비워둔 채 맨 아래로 스크롤하여 **'저장 후 계속'**을 누릅니다.

    - '범위' 단계는 그냥 '저장 후 계속'을 누릅니다.

    - '테스트 사용자' 단계에서 '+ ADD USERS' 버튼을 클릭하고, 사용자님의 Gmail 주소를 추가한 뒤 '저장 후 계속'을 누릅니다.

5. 사용자 인증 정보 만들기:
    - 좌측 메뉴에서 **'API 및 서비스' > '사용자 인증 정보'**로 이동합니다.

    - 상단의 **'+ 사용자 인증 정보 만들기' > 'OAuth 클라이언트 ID'**를 선택합니다.

    - **'애플리케이션 유형'**으로 **'데스크톱 앱'**을 선택합니다.

    - 이름을 입력하고 '만들기'를 클릭하면 클라이언트 ID가 생성됩니다.

    - 생성된 클라이언트 ID 목록에서 방금 만든 항목 오른쪽의 **다운로드 아이콘(JSON 다운로드)**을 클릭합니다.

6. 파일 이름 변경 및 이동:

    - 다운로드된 JSON 파일의 이름을 **credentials.json**으로 변경합니다.

    - 이 파일을 Airflow 프로젝트의 dags 폴더 또는 이전에 생성한 config 폴더 안으로 이동시킵니다. 

    - config 파일이 없다면 생성해서 json 파일을 추가합니다.
    

## 2. MySQL 설정
- 현재 사용자의 정보를 얻기 위해 MySQL을 사용하고 있습니다

- 이용하기 위해서는 .env 파일에 MySQL 설정을 해야합니다.

```
MYSQL_SERVER="Your server IP or Address"
MYSQL_DB="Your Database Schema name"
MYSQL_USER="Your user name"
MYSQL_PASSWORD="Your user password"
```