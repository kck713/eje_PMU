# e.je PMU 랜딩페이지 — 인수인계

반영구(PMU) 스튜디오 **e.je PMU**(대표 이제 원장)의 원페이지 랜딩페이지입니다.
빌드 도구 없는 정적 사이트로, `index.html`을 브라우저로 열면 바로 동작합니다.
사용자(사장님 측)는 비개발자이며 한국어로 요청합니다. 답변도 한국어로, 짧고 쉽게.

## 저장소 · 브랜치

- 저장소: `kck713/eje_PMU` (2026-10 `Daniel-Kim`에서 이름 변경)
- 작업 브랜치: `claude/confident-lovelace-h25338` → PR [kck713/eje_PMU#1](https://github.com/kck713/eje_PMU/pull/1) (base: `main`, 아직 미병합)
- `main`은 빈 초기 커밋만 있음. GitHub 기본 브랜치가 아직 작업 브랜치로 되어 있을 수 있음(설정 → Default branch를 `main`으로 바꾸도록 안내함)
- 수정할 때마다 커밋 → 같은 브랜치에 푸시 → PR에 자동 반영되는 흐름으로 진행해 왔음

## 파일 구조

```
index.html              페이지 전체 마크업 (섹션 순서는 아래 참고)
assets/css/style.css    스타일. 맨 위 :root 토큰 + 섹션별 블록 + 반응형(1520/1180/960/600px)
assets/js/main.js       헤더 스크롤, 모바일 메뉴, 시술 탭, 전후 비교 슬라이더, 카운트업, 스크롤 등장, 예약 폼 검증
assets/img/*.webp       모든 이미지 (사용자가 보내준 원본을 잘라/압축해 webp로 저장)
tools/build-preview.py  Artifact 미리보기용 단일 HTML 생성 스크립트
```

## 섹션 순서 (index.html)

1. 헤더: 2단(윗줄 로고+영문 태그라인 / 아랫줄 소개·메뉴·상담예약). 스크롤하면 한 줄로 축소. 960px 이하 햄버거 메뉴
2. 히어로: "Minimal Touch, Captivating Allure." / "우아함 속에 숨겨진 매혹적인 감각" + `hero-silk.webp`(오른쪽 절반, 왼쪽 마스크 페이드)
3. 브랜드 스토리 `#philosophy`: "아름다움이라는 여정을 껴안다" + `story-model.webp` + Embrace / Journey 키워드
4. 원장 소개 `#director`: `director.webp`(밝은 크림 배경, 그림자). 경력은 빼기로 함, 자격 1줄만 **빈칸**
5. 시술 안내 `#services`: 탭 3개 BROWS 눈썹 / LIP BLUSH 입술 / EYE LASH 속눈썹. 이미지 3:4 고정
6. 시술 과정(4단계)
7. 전후 비교 `#gallery`: 드래그 슬라이더 3개 (**사진 없음, 플레이스홀더**)
8. 후기 `#reviews` (**예시 문구**)
9. 가격 `#price`: 메뉴판 형식 (아래 가격 참고)
10. FAQ `#faq`
11. 상담 예약 `#reserve`: 폼은 검증만 하고 실제 전송 없음
12. 오시는 길 `#location`: 정보 + `location-guide.webp`(원본 그대로) + `building.webp` + Google Map 버튼
13. 푸터, 오른쪽 빠른 문의 패널(데스크톱), 모바일 하단 바(카카오톡 | 무료 상담 예약)

## 확정된 실제 정보

- 상호: e.je PMU (인스타 표기 e.je_pmu) / 원장: 이제 / 대표자(푸터): 손은정
- 주소: 서울특별시 강남구 삼성로116길 5, 3층 (1층 Allveau 헤어살롱 건물)
- 지하철: 9호선 삼성중앙역 3번 출구 도보 4분 / 7호선 청담역 6번 출구 도보 7분
- 주차: 삼성로 620 (스시히로바) 발렛, 도보 1분, 발렛비 5,000원
- 전화: 070-4848-1170
- 카카오톡: https://pf.kakao.com/_xlqxcxjX (사용자가 `/chat` 없이 이 주소로 요청)
- 인스타그램: https://www.instagram.com/e.je_pmu/
- 네이버 플레이스: https://map.naver.com/p/entry/place/2083666376
- 가격(모두 리터치 1회 포함): Hairstroke 400,000 / Shadow 250,000 / Combo 300,000 / Lip Blush 350,000. 속눈썹은 "상담 후 안내"
- 리터치: 시술 후 4~8주 이내, 방문일 2주 전까지 예약

## 아직 임시값 / 남은 일

- 원장 자격·수료 내용 (`index.html`의 `[자격·수료 입력]`). 경력은 사용자 요청으로 뺌
- 영업시간: 평일 10–20, 토 10–17, 일·공휴일 휴무 — 사용자가 "그대로 유지"라고 함
- 사업자등록번호: 예비창업자라 아직 없음 → 푸터에서 뺌. 등록 후 다시 넣기
- EYE LASH 가격, 세부 메뉴(래쉬 리프트/틴팅/영양 케어는 Claude가 일반적인 구성으로 채운 것 — 확인 필요)
- 전후 비교 사진, 실제 후기
- 예약 폼 실제 접수 연동 (`main.js` TODO)
- 모델 사진 사용 권한 확인(사용자에게 안내함)
- SEO/AEO/GEO(메타 태그 정리, LocalBusiness·FAQPage JSON-LD, sitemap/robots, 서치콘솔 등록): 사용자가 "나중에" 하기로 함. 실제 정보가 다 채워진 뒤 진행 권장
- 호스팅: GitHub Pages로 공개하기로 함(2026-10). 사용자가 Settings → Pages에서 Source를 `Deploy from a branch` / `claude/confident-lovelace-h25338` / `/(root)`로 지정. 주소: https://kck713.github.io/eje_PMU/ . `.nojekyll`로 Jekyll 처리 끔. 이 클라우드 환경에서는 github.io 접속이 막혀 직접 확인 불가

## 사용자 취향 · 지켜온 결정

- 톤: 에스프레소 다크(#221d1a) + 샌드 베이지 포인트 + 브랜드 크림(밝은 섹션). 헤드라인은 굵은 고딕, 브랜드/영문은 세리프(Cormorant Garamond). 버튼은 각진 모양
- **간결하게.** 브랜드 자료를 "막 다 넣지 말라"고 함 → 3대 전략, Embrace/Journey 카드 등은 일부러 뺌
- **안 하는 시술은 언급 금지:** 아이라인, 헤어라인, 잔흔 제거/레이저. 시술은 BROWS · LIP BLUSH · EYE LASH 세 가지만
- 시술 안내에 시술시간·유지기간 표시하지 않음(사용자가 빼달라고 함)
- "4가지 안심 약속" 섹션은 사용자가 삭제 요청함
- **이미지 자르기 지시를 정확히 따를 것.** "자르지 말고 그대로"라고 하면 원본 그대로. 원장 사진은 사용자가 준 예시와 같은 구도(손이 안 보이게, 얼굴이 너무 크지 않게)로 맞춤
- 지어낸 경력·수치·후기를 실제처럼 넣지 않음(예전 통계 숫자도 삭제함). 모르면 빈칸/플레이스홀더로 두고 사용자에게 물어볼 것
- 외부 링크는 `target="_blank" rel="noopener"`

## 작업 시 주의(겪었던 문제)

- `.reveal` 요소는 처음에 투명 → 스크롤 시 나타남. 스크린샷 검증 땐 `.reveal{opacity:1!important;transform:none!important}`를 주입해서 볼 것
- `<img>`에 width/height 속성을 넣었으면 CSS에서 비율을 고정할 때 반드시 `height:auto`도 함께(안 그러면 height 속성값이 그대로 적용돼 이미지가 길게 늘어남)
- Playwright는 `executablePath: '/opt/pw-browsers/chromium'`으로 실행. 스크린샷 경로를 상대경로로 주면 저장소에 png가 생기니 스크래치 폴더에 저장할 것
- Pretendard 폰트는 jsdelivr에서 로드(실사이트용). Artifact 미리보기에서는 막혀서 Noto Sans KR로 대체됨
- 이 클라우드 환경에서 mikclinic.com, pf.kakao.com, Google 지도 iframe 등 일부 외부 사이트는 접속이 막혀 있었음

## 미리보기(Artifact)

- 기존 미리보기: https://claude.ai/artifact/LXymuYA3aseG8ZDaBcEZWy — **이전 계정 소유**라 새 계정에서는 수정할 수 없을 수 있음. 새 계정에서는 새 Artifact로 발행하면 됨
- 만드는 법: `python3 tools/build-preview.py <스크래치>/eje-pmu.html` → Artifact로 발행하면서 `files`에 `assets/img/*.webp`를 같은 경로로 함께 올림
