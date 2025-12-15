# ⚡ 빠른 시작 가이드

## 📦 필요한 것
- ✅ Notion API Key: `ntn_b24615144235nsq0gbVa7c2VxBKiddXFkkWpow0n9Txbiv`
- ✅ Database ID: `1ed092b7bab780c59e16cac9b108ab41`
- ⏳ Anthropic API Key: 아직 발급 안 됨

---

## 🚀 3단계 설정

### 1️⃣ GitHub Repository 만들기

1. https://github.com/new 접속
2. Repository 이름: `notion-url-automation`
3. Public 또는 Private 선택
4. **Create repository** 클릭

### 2️⃣ 파일 업로드

**쉬운 방법 (웹 사용):**

1. 생성된 Repository 페이지에서 **uploading an existing file** 클릭
2. 다운로드한 모든 파일을 드래그 앤 드롭:
   ```
   .github/workflows/notion-automation.yml
   notion_url_automation.py
   requirements.txt
   README.md
   ```
3. **Commit changes** 클릭

**주의**: `.github` 폴더는 숨김 폴더입니다. 
- Windows: 탐색기에서 "숨김 항목" 체크
- Mac: Finder에서 `Cmd + Shift + .` 누르기

### 3️⃣ Secrets 설정

Repository에서:

1. **Settings** 탭
2. **Secrets and variables** → **Actions**
3. **New repository secret** 클릭
4. 다음 3개 추가:

**Secret 1:**
- Name: `NOTION_API_KEY`
- Value: `ntn_b24615144235nsq0gbVa7c2VxBKiddXFkkWpow0n9Txbiv`

**Secret 2:**
- Name: `NOTION_DATABASE_ID`
- Value: `1ed092b7bab780c59e16cac9b108ab41`

**Secret 3:**
- Name: `ANTHROPIC_API_KEY`
- Value: (아래에서 발급)

---

## 🔑 Anthropic API Key 발급

### 방법 1: 기존 계정 있으면
1. https://console.anthropic.com/settings/keys 접속
2. **Create Key** 클릭
3. 이름 입력 (예: `notion-automation`)
4. Key 복사 (`sk-ant-api03-...` 형식)

### 방법 2: 신규 가입
1. https://console.anthropic.com/ 접속
2. **Sign Up** 클릭
3. 이메일로 가입
4. **API Keys** 메뉴에서 Key 생성

**무료 크레딧:**
- 신규 가입 시 $5 무료 제공
- 매일 3-5개 URL 분석하면 한 달 이상 무료 사용 가능

---

## ✅ 테스트하기

1. **Actions** 탭 클릭
2. **Notion URL Auto Analysis** 클릭
3. **Run workflow** 버튼 클릭
4. 실행 결과 확인

---

## 🎯 사용 방법

### 자동 실행
- 매일 오후 12:50에 자동으로 실행됨
- 분석 안 된 URL 자동 감지 및 업데이트

### 수동 실행
- GitHub Actions에서 언제든 수동 실행 가능
- URL 많이 추가했을 때 유용

---

## 📋 Notion DB 설정

Category와 Type 필드에 다음 옵션 추가:

**Category 옵션:**
- 개발
- 디자인
- 마케팅
- AI/ML
- 비즈니스
- 라이프스타일
- 기타

**Type 옵션:**
- YouTube
- Blog
- News
- Article

---

## 🆘 문제 해결

### "Secrets not found" 에러
→ 3️⃣ 단계에서 Secrets 이름을 정확히 입력했는지 확인

### "403 Forbidden" 에러
→ Notion Integration이 DB에 연결되었는지 확인

### "Invalid API Key" 에러
→ Anthropic API Key가 유효한지 확인

---

## 💰 비용

- **GitHub Actions**: 
  - Public repo: 완전 무료
  - Private repo: 월 2,000분 무료 (충분함)

- **Anthropic API**:
  - 신규 가입 시 $5 무료
  - 1개 URL 분석: 약 $0.001-0.002
  - 매일 5개씩 한 달: 약 $0.15-0.30

---

## 📞 도움이 필요하면

1. README.md 전체 문서 확인
2. GitHub Issues에 질문 등록
3. Actions 로그 확인

**성공했다면 축하합니다! 🎉**
이제 매일 자동으로 URL이 정리됩니다!
