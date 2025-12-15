# 🚀 Notion URL 자동 분석 시스템

매일 자동으로 Notion DB의 URL을 분석하여 제목, 카테고리, 요약을 생성하는 시스템입니다.

## ⚙️ 설정 방법

### 1. GitHub Repository 생성

1. GitHub에 로그인
2. 새 Repository 생성 (public 또는 private)
   - Repository 이름: `notion-url-automation` (원하는 이름)
3. 생성된 Repository로 이동

### 2. 파일 업로드

다음 파일들을 Repository에 업로드하세요:

```
notion-url-automation/
├── .github/
│   └── workflows/
│       └── notion-automation.yml
├── notion_url_automation.py
├── requirements.txt
└── README.md
```

**업로드 방법:**

#### 방법 A: 웹 인터페이스 사용
1. GitHub Repository 페이지에서 **Add file** → **Upload files** 클릭
2. 모든 파일을 드래그 앤 드롭
3. **Commit changes** 클릭

#### 방법 B: Git 명령어 사용 (추천)
```bash
# Repository 클론
git clone https://github.com/YOUR_USERNAME/notion-url-automation.git
cd notion-url-automation

# 파일 복사 (다운로드한 파일들을 여기로 복사)
# .github/workflows 폴더 생성 필요
mkdir -p .github/workflows

# 파일 추가 및 커밋
git add .
git commit -m "Initial setup: Add Notion URL automation"
git push origin main
```

### 3. GitHub Secrets 설정

Repository에서:

1. **Settings** 탭 클릭
2. 왼쪽 메뉴에서 **Secrets and variables** → **Actions** 클릭
3. **New repository secret** 클릭
4. 다음 3개의 Secret 추가:

| Name | Value |
|------|-------|
| `NOTION_API_KEY` | `ntn_b24615144235nsq0gbVa7c2VxBKiddXFkkWpow0n9Txbiv` |
| `NOTION_DATABASE_ID` | `1ed092b7bab780c59e16cac9b108ab41` |
| `ANTHROPIC_API_KEY` | 본인의 Claude API Key |

**Anthropic API Key 발급 방법:**
1. https://console.anthropic.com/ 접속
2. 로그인 후 **API Keys** 메뉴
3. **Create Key** 클릭
4. 생성된 Key 복사 (`sk-ant-api03-...`)

### 4. Actions 활성화

1. Repository의 **Actions** 탭 클릭
2. "I understand my workflows, go ahead and enable them" 클릭
3. 왼쪽 사이드바에서 **Notion URL Auto Analysis** 확인

### 5. 테스트 실행

수동으로 먼저 테스트해보세요:

1. **Actions** 탭 → **Notion URL Auto Analysis** 클릭
2. 오른쪽 **Run workflow** 클릭
3. **Run workflow** 버튼 클릭 (초록색)
4. 실행 결과 확인

## 📅 자동 실행 일정

- **실행 시간**: 매일 오후 12:50 (한국시간)
- **UTC 시간**: 03:50 (GitHub Actions는 UTC 기준)

## 🔍 작동 방식

1. **URL 감지**: Notion DB에서 Title이 비어있거나 Notes가 없는 항목 찾기
2. **AI 분석**: Claude AI가 각 URL을 분석하여:
   - 적절한 제목 생성
   - 카테고리 자동 분류 (개발, 디자인, 마케팅, AI/ML, 비즈니스, 라이프스타일, 기타)
   - 콘텐츠 타입 감지 (YouTube, Blog, News, Article)
   - 핵심 내용 요약 (2-3문장)
3. **자동 업데이트**: 분석 결과를 Notion DB에 자동 저장
4. **Date Added**: 오늘 날짜로 자동 설정

## 📊 Notion DB 구조

| 필드 | 타입 | 설명 |
|------|------|------|
| Title | Title | 콘텐츠 제목 (자동 생성) |
| URL | URL | 원본 URL |
| Category | Select | 카테고리 (자동 분류) |
| Type | Select | 콘텐츠 타입 (자동 감지) |
| Notes | Text | 요약 (자동 생성) |
| Date Added | Date | 추가 날짜 (자동) |

**Category 옵션 추가 방법:**
Notion DB에서 Category 필드를 클릭하고 다음 옵션 추가:
- 개발
- 디자인
- 마케팅
- AI/ML
- 비즈니스
- 라이프스타일
- 기타

**Type 옵션 추가 방법:**
Type 필드를 클릭하고 다음 옵션 추가:
- YouTube
- Blog
- News
- Article

## 🎯 사용 방법

1. Notion DB에 URL만 추가 (다른 필드는 비워둠)
2. 매일 12:50에 자동으로 분석 및 업데이트
3. 또는 GitHub Actions에서 수동 실행 가능

## 🔧 문제 해결

### Actions 실행 실패 시

1. **Actions** 탭에서 실패한 workflow 클릭
2. 에러 로그 확인
3. 주요 체크 포인트:
   - Secrets가 올바르게 설정되었는지
   - Notion Integration이 DB에 연결되었는지
   - API Key가 유효한지

### 분석이 안 되는 경우

- Notion DB에 Title과 Notes가 모두 비어있는지 확인
- URL 필드에 유효한 URL이 입력되었는지 확인
- Notion Integration에 DB 접근 권한이 있는지 확인

## 📝 로그 확인

GitHub Actions의 **Artifacts** 섹션에서 실행 로그를 다운로드할 수 있습니다 (7일간 보관).

## 💡 팁

- **대량 처리**: 300개의 URL도 한 번에 처리 가능
- **수동 실행**: 급하게 분석이 필요하면 Actions에서 수동 실행
- **비용**: GitHub Actions는 Public Repository는 무료, Private는 월 2,000분 무료
- **Claude API**: 사용량에 따라 비용 발생 (소량이면 거의 무료)

## 🚨 주의사항

1. **API Key 보안**: 절대 코드에 직접 입력하지 말 것 (Secrets 사용)
2. **Notion Integration**: DB 연결을 꼭 확인
3. **Rate Limit**: API 호출 제한이 있으므로 한 번에 너무 많은 URL 처리 시 실패 가능

## 📞 문의

문제가 생기면 GitHub Issues에 등록하거나 로그를 확인하세요!

---

**Made with ❤️ by Claude**
