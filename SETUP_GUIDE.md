# 🚀 Notion URL 자동화 시스템 - 완전 설치 가이드

OpenAI GPT-4o-mini를 사용하여 Notion DB의 URL을 자동으로 분석하고 업데이트하는 시스템입니다.

## 📦 다운로드한 파일

```
📁 notion-url-automation/
├── 📄 notion_url_automation.py    (메인 Python 스크립트)
├── 📄 requirements.txt             (필요한 패키지 목록)
└── 📁 .github/
    └── 📁 workflows/
        └── 📄 notion-automation.yml (GitHub Actions 설정)
```

---

## ⚡ 빠른 시작 (3단계)

### 1단계: GitHub에 파일 업로드

#### 방법 A: 웹에서 업로드 (추천)

1. GitHub Repository 접속: https://github.com/sysedit2/notion-url-automation
2. **Code** 탭 클릭
3. 각 파일을 하나씩 생성:

**파일 1: notion_url_automation.py**
- **Add file** → **Create new file**
- 파일 이름: `notion_url_automation.py`
- 다운로드한 파일 내용 복사-붙여넣기
- **Commit new file** 클릭

**파일 2: requirements.txt**
- **Add file** → **Create new file**
- 파일 이름: `requirements.txt`
- 내용:
  ```
  requests==2.31.0
  ```
- **Commit new file** 클릭

**파일 3: .github/workflows/notion-automation.yml**
- **Add file** → **Create new file**
- 파일 이름: `.github/workflows/notion-automation.yml`
  - (슬래시를 입력하면 자동으로 폴더 생성!)
- 다운로드한 workflow 파일 내용 복사-붙여넣기
- **Commit new file** 클릭

#### 방법 B: Git 명령어 사용

```bash
cd notion-url-automation
git add .
git commit -m "Add OpenAI automation files"
git push origin main
```

---

### 2단계: GitHub Secrets 설정

https://github.com/sysedit2/notion-url-automation/settings/secrets/actions

**3개의 Secret 추가:**

| Name | Value | 설명 |
|------|-------|------|
| `NOTION_API_KEY` | `ntn_b24615144235nsq0gbVa7c2VxBKiddXFkkWpow0n9Txbiv` | Notion Integration Token |
| `NOTION_DATABASE_ID` | `1ed092b7bab780c59e16cac9b108ab41` | Notion Database ID |
| `OPENAI_API_KEY` | `sk-proj-...` | OpenAI API Key (새로 발급) |

**OpenAI API Key 발급:**
1. https://platform.openai.com/api-keys 접속
2. **+ Create new secret key** 클릭
3. Name: `notion-automation`
4. Key 복사 (`sk-proj-...` 형식)
5. ⚠️ **절대 공개하지 마세요!**

**결제 방법 등록 (필수):**
1. https://platform.openai.com/settings/organization/billing/overview
2. 카드 등록
3. 월 사용량 제한: $5-10 추천

---

### 3단계: 테스트 실행

1. **Actions** 탭 클릭
2. **Notion URL Auto Analysis** 선택
3. **Run workflow** 클릭
4. 실행 로그 확인
5. ✅ 성공하면 Notion DB 확인!

---

## 🎯 작동 방식

### 자동 실행
- **매일 오후 12:50** (한국시간) 자동 실행
- Notion DB에서 Title 또는 Notes가 비어있는 항목 자동 감지
- AI가 URL 분석 후 자동 업데이트

### 분석 내용
- **Title**: 콘텐츠의 적절한 제목 (한국어, 50자 이내)
- **Category**: 개발/디자인/마케팅/AI/ML/비즈니스/라이프스타일/기타
- **Type**: YouTube/Blog/News/Article 자동 감지
- **Notes**: 핵심 내용 2-3문장 요약 (한국어)
- **Date Added**: 오늘 날짜

---

## 💰 비용 안내

### OpenAI GPT-4o-mini
- URL 1개 분석: 약 **$0.0005** (0.05원)
- 매일 5개 × 30일: 약 **$0.08/월** (100원)

### 무료 크레딧
- 신규 가입 시 **$5 무료** (3개월간)
- 약 **10,000개 URL** 무료 분석 가능!

### GitHub Actions
- Public repository: **완전 무료**
- Private repository: 월 2,000분 무료 (충분함)

---

## 📊 Notion DB 설정

### Category 옵션 추가
Notion DB의 Category 필드에 다음 옵션 추가:
- 개발
- 디자인
- 마케팅
- AI/ML
- 비즈니스
- 라이프스타일
- 기타

### Type 옵션 추가
Type 필드에 다음 옵션 추가:
- YouTube
- Blog
- News
- Article

---

## 🔧 문제 해결

### "Invalid API Key" 에러
→ OpenAI API Key 확인
→ Secret 이름이 `OPENAI_API_KEY`인지 확인

### "403 Forbidden" 에러
→ Notion Integration이 DB에 연결되었는지 확인

### 분석이 안 되는 경우
→ Notion DB에 Title과 Notes가 비어있는지 확인
→ URL 필드에 유효한 URL이 있는지 확인

### Actions 실행 실패
→ Actions 탭에서 로그 확인
→ 에러 메시지 복사해서 질문

---

## 📝 사용 팁

1. **URL만 입력**: Title, Category, Type, Notes는 비워두면 자동 채워짐
2. **수동 실행**: Actions 탭에서 언제든 수동 실행 가능
3. **대량 처리**: 300개도 한 번에 처리 가능
4. **비용 절감**: 하루에 몰아서 실행하는 것보다 매일 조금씩이 효율적

---

## ✅ 완료 체크리스트

- [ ] GitHub에 3개 파일 업로드
  - [ ] notion_url_automation.py
  - [ ] requirements.txt
  - [ ] .github/workflows/notion-automation.yml
- [ ] OpenAI API Key 발급
- [ ] GitHub Secrets 3개 추가
  - [ ] NOTION_API_KEY
  - [ ] NOTION_DATABASE_ID
  - [ ] OPENAI_API_KEY
- [ ] Actions 테스트 실행
- [ ] Notion DB 결과 확인

---

## 🎉 완료!

모든 설정이 끝났습니다!

이제 매일 12:50에 자동으로:
1. Notion DB에서 새 URL 감지
2. AI가 분석
3. 자동으로 정보 업데이트

**더 이상 손쉽게 URL 관리할 수 없습니다!** 🚀

---

## 📞 도움이 필요하면

- GitHub Issues에 질문 등록
- Actions 로그 확인
- 에러 메시지 복사해서 문의

**Made with ❤️ using OpenAI GPT-4o-mini**
