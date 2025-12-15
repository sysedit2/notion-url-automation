#!/usr/bin/env python3
"""
Notion URL 자동 분석 스크립트
매일 자동으로 실행되어 Notion DB의 URL을 분석하고 업데이트합니다.
"""

import os
import sys
import json
import time
from datetime import datetime
from typing import Dict, List, Optional
import requests

# 환경 변수에서 설정 가져오기
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Notion API 설정
NOTION_VERSION = '2022-06-28'
NOTION_BASE_URL = 'https://api.notion.com/v1'


class NotionURLManager:
    """Notion URL 관리 클래스"""
    
    def __init__(self):
        self.notion_headers = {
            'Authorization': f'Bearer {NOTION_API_KEY}',
            'Notion-Version': NOTION_VERSION,
            'Content-Type': 'application/json'
        }
        
    def get_unprocessed_urls(self) -> List[Dict]:
        """분석되지 않은 URL 가져오기 (Title이 비어있거나 Notes가 없는 항목)"""
        url = f'{NOTION_BASE_URL}/databases/{NOTION_DATABASE_ID}/query'
        
        # Title이 비어있거나 Notes가 없는 항목 필터링
        payload = {
            "filter": {
                "or": [
                    {
                        "property": "Title",
                        "title": {
                            "is_empty": True
                        }
                    },
                    {
                        "property": "Notes",
                        "rich_text": {
                            "is_empty": True
                        }
                    }
                ]
            }
        }
        
        try:
            response = requests.post(url, headers=self.notion_headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get('results', [])
        except Exception as e:
            print(f"❌ Notion DB 조회 실패: {e}")
            return []
    
    def get_url_from_page(self, page: Dict) -> Optional[str]:
        """페이지에서 URL 추출"""
        try:
            url_property = page['properties'].get('URL', {})
            if url_property.get('type') == 'url':
                return url_property.get('url')
        except Exception as e:
            print(f"⚠️ URL 추출 실패: {e}")
        return None
    
    def update_page(self, page_id: str, title: str, category: str, 
                    content_type: str, notes: str) -> bool:
        """페이지 업데이트"""
        url = f'{NOTION_BASE_URL}/pages/{page_id}'
        
        payload = {
            "properties": {
                "Title": {
                    "title": [{"text": {"content": title}}]
                },
                "Category": {
                    "select": {"name": category}
                },
                "Type": {
                    "select": {"name": content_type}
                },
                "Notes": {
                    "rich_text": [{"text": {"content": notes}}]
                },
                "Date Added": {
                    "date": {"start": datetime.now().strftime('%Y-%m-%d')}
                }
            }
        }
        
        try:
            response = requests.patch(url, headers=self.notion_headers, json=payload)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"❌ 페이지 업데이트 실패: {e}")
            return False


class URLAnalyzer:
    """URL 분석 클래스"""
    
    def __init__(self):
        self.anthropic_url = 'https://api.anthropic.com/v1/messages'
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': ANTHROPIC_API_KEY,
            'anthropic-version': '2023-06-01'
        }
    
    def get_url_type(self, url: str) -> str:
        """URL 타입 감지"""
        url_lower = url.lower()
        if 'youtube.com' in url_lower or 'youtu.be' in url_lower:
            return 'YouTube'
        if 'news' in url_lower or 'naver.com/news' in url_lower:
            return 'News'
        if 'blog' in url_lower or 'medium.com' in url_lower or 'tistory' in url_lower:
            return 'Blog'
        return 'Article'
    
    def analyze_url(self, url: str) -> Dict[str, str]:
        """AI를 사용하여 URL 분석"""
        content_type = self.get_url_type(url)
        
        prompt = f"""다음 URL을 분석하여 JSON 형식으로 응답해주세요. 
반드시 JSON만 출력하고, 마크다운 코드 블록(```)이나 다른 설명은 절대 포함하지 마세요.

URL: {url}

응답 형식 (이 형식 그대로 JSON만 출력):
{{"title": "콘텐츠의 적절한 제목 (한국어, 50자 이내)", "category": "개발|디자인|마케팅|AI/ML|비즈니스|라이프스타일|기타 중 하나", "notes": "핵심 내용 요약 (2-3문장, 한국어, 150자 이내)"}}"""

        payload = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 1000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        try:
            response = requests.post(
                self.anthropic_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            
            # AI 응답 추출
            ai_response = ''
            for item in data.get('content', []):
                if item.get('type') == 'text':
                    ai_response += item.get('text', '')
            
            # JSON 파싱
            ai_response = ai_response.strip()
            # 코드 블록 제거
            ai_response = ai_response.replace('```json', '').replace('```', '').strip()
            
            parsed = json.loads(ai_response)
            
            return {
                'title': parsed.get('title', url.split('/')[-1] or 'Untitled')[:100],
                'category': parsed.get('category', '기타'),
                'type': content_type,
                'notes': parsed.get('notes', 'AI 분석을 완료하지 못했습니다.')[:500]
            }
            
        except json.JSONDecodeError as e:
            print(f"⚠️ JSON 파싱 실패: {e}")
            print(f"AI 응답: {ai_response[:200]}")
            return self._get_fallback_result(url, content_type)
        except Exception as e:
            print(f"⚠️ URL 분석 실패 ({url}): {e}")
            return self._get_fallback_result(url, content_type)
    
    def _get_fallback_result(self, url: str, content_type: str) -> Dict[str, str]:
        """분석 실패시 기본값 반환"""
        return {
            'title': url.split('/')[-1] or 'Untitled',
            'category': '기타',
            'type': content_type,
            'notes': '자동 분석을 완료하지 못했습니다. 수동으로 내용을 추가해주세요.'
        }


def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("🚀 Notion URL 자동 분석 시작")
    print("=" * 60)
    print(f"⏰ 실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 환경 변수 확인
    if not all([NOTION_API_KEY, NOTION_DATABASE_ID, ANTHROPIC_API_KEY]):
        print("❌ 환경 변수가 설정되지 않았습니다!")
        print("필요한 환경 변수:")
        print("  - NOTION_API_KEY")
        print("  - NOTION_DATABASE_ID")
        print("  - ANTHROPIC_API_KEY")
        sys.exit(1)
    
    # 초기화
    notion_manager = NotionURLManager()
    analyzer = URLAnalyzer()
    
    # 분석되지 않은 URL 가져오기
    print("📥 분석 대상 URL 조회 중...")
    unprocessed_pages = notion_manager.get_unprocessed_urls()
    
    if not unprocessed_pages:
        print("✅ 분석할 URL이 없습니다. 모든 항목이 최신 상태입니다!")
        return
    
    print(f"📊 총 {len(unprocessed_pages)}개의 URL을 발견했습니다.")
    print()
    
    # 각 URL 분석 및 업데이트
    success_count = 0
    fail_count = 0
    
    for idx, page in enumerate(unprocessed_pages, 1):
        page_id = page['id']
        url = notion_manager.get_url_from_page(page)
        
        if not url:
            print(f"⚠️ [{idx}/{len(unprocessed_pages)}] URL이 없는 페이지 건너뜀")
            fail_count += 1
            continue
        
        print(f"🔍 [{idx}/{len(unprocessed_pages)}] 분석 중: {url[:60]}...")
        
        # URL 분석
        result = analyzer.analyze_url(url)
        
        # Notion 업데이트
        if notion_manager.update_page(
            page_id,
            result['title'],
            result['category'],
            result['type'],
            result['notes']
        ):
            print(f"   ✅ 완료: {result['title'][:50]}")
            success_count += 1
        else:
            print(f"   ❌ 업데이트 실패")
            fail_count += 1
        
        # API 속도 제한 방지
        if idx < len(unprocessed_pages):
            time.sleep(1)
    
    # 결과 요약
    print()
    print("=" * 60)
    print("📈 작업 완료!")
    print("=" * 60)
    print(f"✅ 성공: {success_count}개")
    print(f"❌ 실패: {fail_count}개")
    print(f"📊 총 처리: {success_count + fail_count}개")
    print()
    print(f"⏰ 종료 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


if __name__ == '__main__':
    main()
