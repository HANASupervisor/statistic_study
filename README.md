# statistic_study

### 이 레포지토리는 3명의 취업을 위한 취업 공부내용을 정리한 레포지토리입니다.

# Git/GitHub 초보 팀원을 위한 필수 명령어 정리 (치트시트)

> 목표: "로컬에서 작업 → 커밋 → 원격(GitHub)로 푸시" 흐름을 안전하게 반복하기  
> 원칙: **main(또는 master)에는 바로 작업하지 말고, 브랜치에서 작업하고 PR로 합치기**

---

## 0) Git 기본 개념 3줄 요약
- **Working Directory(작업 폴더)**: 파일을 수정하는 곳
- **Staging Area(스테이징)**: 커밋할 파일을 골라 담는 곳 (`git add`)
- **Repository(저장소)**: 커밋들이 쌓이는 곳 (`git commit`)

---

## 1) 처음 1회: Git 설정
```bash
git config --global user.name "홍길동"
git config --global user.email "hong@example.com"
git config --global -l
```
## 2) 레포지토리 받기/만들기
## A. GitHub 레포를 "처음부터 클론" (가장 쉬움)
```bash
git clone <레포URL>
cd <프로젝트폴더>
```

## B. 로컬 폴더를 Git 레포로 만들기
```bash
git init
```

## 3) 원격(remote) 연결 확인/추가/변경 
## 원격 연결 확인
```bash
git remote -v
```

## 원격 추가 (origin)
```bash
git remote add origin <레포URL>
git remote -v
```

## 원격 URL 변경 (HTTPS ↔ SSH 바꾸거나 레포 주소 바뀐 경우)
```bash
git remote set-url origin <새레포URL>
git remote -v
```

## 원격 제거
```bash
git remote remove origin
```

## 4) 브랜치 전략(초보 추천)

main: 배포/최종본(직접 커밋 금지 권장)

feature/기능명: 기능 개발 브랜치

fix/버그명: 버그 수정 브랜치

## 5) 브랜치 생성/이동/확인
## 현재 브랜치 확인
```bash
git branch
git status
```

### 브랜치 생성 + 이동 (추천)
```bash
git switch -c feature/login
```

### 브랜치 이동
```bash
git switch main
git switch feature/login
```

### 브랜치 목록(원격 포함)
```bash
git branch -a
```

### 원격 브랜치 가져오기(최신 목록 업데이트)
```bash
git fetch
```

## 6) 작업 → add → commit (가장 중요)
### 변경 사항 확인
```bash
git status
git diff
```

### 스테이징(add)
```bash
git add .

# 또는 특정 파일만
git add src/app.js
```

### 커밋
```bash
git commit -m "feat: 로그인 UI 추가"
```

### 커밋 메시지 추천 규칙(간단 버전)
```
feat: 기능 추가

fix: 버그 수정

docs: 문서 변경

refactor: 리팩토링

chore: 잡일(설정/패키지 등)
```

## 7) 원격으로 올리기(push) & 받아오기(pull)
### push (처음 올릴 때 -u 붙이면 다음부터 편함)
```bash
git push -u origin feature/login

# 이후부터는
git push
```

### 최신 변경 받아오기(가장 안전한 습관)
```bash
git pull
```


# 주의: 작업 시작 전/PR 전에는 git pull을 습관처럼 해주세요.

## 8) 브랜치 삭제
### 로컬 브랜치 삭제
```bash
git branch -d feature/login
# 강제 삭제(주의)
git branch -D feature/login
```

### 원격 브랜치 삭제
```bash
git push origin --delete feature/login
```

## 9) stash: "작업 임시 보관" (브랜치 이동/급한 pull 때)
### 임시 저장
```bash
git stash
```

### 메시지 붙이기
```bash
git stash push -m "WIP: 작업중 임시저장"

stash 목록
git stash list

stash 복원(적용만 하고 stash는 남김)
git stash apply

stash 복원(적용 후 stash에서 제거)
git stash pop

특정 stash 적용
git stash apply stash@{0}

stash 삭제
git stash drop stash@{0}

stash 전체 삭제(주의)
git stash clear
```

## 10) 실수했을 때 되돌리기 (중요)
### 10-1) add를 잘못했어요 (스테이징 취소)
```bash
전체 스테이징 취소
git restore --staged .

특정 파일만 스테이징 취소
git restore --staged src/app.js

10-2) 파일 내용을 되돌리고 싶어요 (작업 내용 롤백)
특정 파일을 마지막 커밋 상태로 되돌림(주의: 수정 내용 사라짐)
git restore src/app.js

전체 파일 되돌림(주의)
git restore .

10-3) 커밋 메시지를 잘못 썼어요 (최근 커밋 수정)
git commit --amend -m "feat: 로그인 UI 및 검증 추가"


주의: 이미 push한 커밋을 amend하면 히스토리가 바뀜 → 초보 팀에서는 되도록 피하거나, 꼭 필요하면 팀에 공유 후 진행

10-4) "방금 커밋"을 취소하고 싶어요
A. 커밋만 취소하고 파일 변경은 남기기(추천)
git reset --soft HEAD~1

B. 커밋 취소 + 스테이징도 풀기 (변경은 남김)
git reset HEAD~1

C. 커밋 취소 + 변경도 날리기(매우 주의)
git reset --hard HEAD~1

10-5) push까지 해버렸어요(원격에 올라감)
A. 안전하게 되돌리기(추천): "되돌리는 커밋" 만들기
git revert <커밋해시>
git push

B. 강제로 과거로 돌리기(위험): 협업 중이면 거의 금지
git reset --hard <되돌릴커밋해시>
git push --force

10-6) merge 충돌(conflict)이 났어요

충돌 난 파일을 열면 <<<<<<<, =======, >>>>>>> 표시가 있음

원하는 코드 형태로 정리하고 저장

아래 실행:

git add .
git commit -m "fix: merge conflict 해결"
```

## 11) 원격 브랜치 기반으로 로컬 브랜치 만들기
### 예: 원격에 feature/login이 있는데 로컬에 없을 때
```bash
git fetch
git switch -c feature/login origin/feature/login
```
## 12) 자주 쓰는 상태/로그 확인
```bash
git status
git log --oneline --graph --decorate --all
```
## 13) 초보 팀원에게 추천하는 "매 작업 루틴"
### 작업 시작 전
```bash
git switch master
git pull
```

### 브랜치 만들기
```bash
git switch -c feature/작업명
```

### 작업 후
```bash
git status
git add .
git commit -m "feat: 작업내용"
git push -u origin feature/작업명---
```