# file_basic_properties

## 설명
 [바이러스 토탈](https://www.virustotal.com/)기준 파일의 기본 정보를 json 형태로 저장해주는 프로그램

## 사용법
1. [requirement](./requirement) 폴더에 있는 [file-5.03-setup.exe](./requirement/file-5.03-setup.exe)를 실행해서 설치해 주세요.
2. **C:\Program Files (x86)\GnuWin32\bin** 를 환경변수에 추가 해주세요.
3. [requirement](./requirement) 폴더에 있는 [ssdeep-2.14.1-win32-binary.zip](./requirement/ssdeep-2.14.1-win32-binary.zip)의 압축을 푸신 다음 안에 있는 **ssdeep.exe** 를 **C:\Windows** 에 넣어 주세요.

## 업데이트 로그

Version 1.0
* 파일의 md5, sha-1 구하는 함수 구현
* 파일의 magic 구하는 함수 구현
* 파일의 크기 구하는 함수 구현
* 파일의 ssdeep 구하는 함수 구현
