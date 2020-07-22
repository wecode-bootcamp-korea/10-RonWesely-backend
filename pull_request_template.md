>wecode PR message template 및 체크 리스트 입니다. 
아래 사항들을 전부 작성/체크 하시고 PR 해주세요!

## 수정 사항 간략한 한줄 요약
(여기에 수정 사항에 대한 간략한 한줄 요약/제목 작성해 주세요. 예: 로그인 엔드포인트 구현)       
- products App 모델링 리뷰 후, models.py 작성완료
- README.md 추가       
		 
## 수정 사항들 자세한 내용
(여기에 수정 사항에 대한 자세한 내용을 작성해 주세요)
- 7/22 모델링 리뷰 후, 수정사항 반영
- 제품에 대해 전체 카테고리 역할하는 Categories 테이블 생성
- 면도날 제품은 별도 속성이 없어, ManytoMany가 아니므로 단일로 생성(blade_products)
- 면도기(선물세트,면도기세트) 제품은 색상과 ManytoMany 관계이므로 colors 테이블과 ManytoMany로 생성(razor_products,razor_products_colors)
- 스킨제품(애프터쉐이브,쉐이빙젤) 제품은 사이즈와 ManytoMany 관계이므로 sizes 테이블과 ManytoMany로 생성(skin_products,skin_products_sizes)
- 장바구니 또는 결제내역에 담기는 사진은 order_images에 참조하는 테이블은 blade_products,razor_products_colors,skin_products_sizes

## 체크 리스트 (아래 사항들이 전부 체크되어야만 merge가 됩니다!)
- [x] 필요한 test들을 완료하였고 기능이 제대로 실행되는지 확인 하였습니다.
- [x] Wecode의 코드 스타일 가이드에 맞추어 코드를 작성 하였습니다.
- [x] 제가 의도한 파일들과 수정 사항들만 커밋이 된 것을 확인 하였습니다.
- [x] 본 수정 사항들을 팀원들과 사전에 상의하였고 팀원들 모두 해당 PR에 대하여 알고 있습니다.
