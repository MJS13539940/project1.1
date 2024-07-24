# **도서관 출납 서비스**
## 프로젝트 목표
+ **이용자 관리**: 도서관 이용자 정보를 조회하고, 새로운 이용자를 등록하거나 기존 이용자를 삭제할 수 있다.
+ **도서 관리**: 도서관의 도서 정보를 관리하며, 새로운 도서를 추가하거나 기존 도서를 제거할 수 있다.
+ **대여 및 반납 관리**: 이용자 정보와 도서 정보를 연계하여 도서 대여 및 반납에 관한 정보를 조회하고 편집할 수 있다.
  
## 시작

![개요](https://github.com/user-attachments/assets/37070c35-65c3-437c-9dc2-47bec53406d9)

도서관 출납 서비스는 다섯 가지 주요 카테고리로 나뉘어, 각 기능과 필요한 데이터 처리 방법을 구상한다.

## 진행 과정
+ 구상단계

개발에 익숙하지 않아 명확한 구상을 하는 데 어려움을 겪었다. 

터미널 기반의 콘솔로 기능을 확인하면 오히려 어려울 것 같았기에 GUI 구현을 목표로 설정했으나, 기능적인 설계가 부실하여 이후 모든 과정에서 문제를 일으켰다.

+ 코딩단계

만듦새는 좋지 않았지만 코딩 과정에서 이해도가 점차 나아지는 것을 느꼈다.

![버그](https://github.com/user-attachments/assets/e1be9449-f114-4d19-adee-6068585f1f0c)

예시 중 하나로 페이지 전환 시 위젯이 누적되는 현상이 있었다. 원인은 위젯 생성이 버튼 클릭 이벤트에 따라왔던 것으로,

각 페이지마다 카운트를 할당해서 위젯이 한 번만 생성되도록 하여 수정했다.

이후는 데이터처리 코드를 적용해야 했는데 GUI구현에 너무 매달리는 바람에 시간이 부족해졌다.

엉성한 설계를 바탕으로 UI를 구현하려니 자잘한 수정이 많아지고, 그 과정에서 코드에 대한 이해도가 떨어져 점점 손대기 힘들어졌다.

+ 결과

제대로 작동하는 UI는 페이지 전환, 새 창 팝업, 새로고침(엔트리 비우기) 뿐이고 그 외 나머지는 전부 구현하지 못했다.

데이터 처리쪽은 이용자나 도서 정보를 추가하기 전의 key만 존재하는 csv파일이 생성된 것은 확인 했지만, 데이터를 편집하는 기능은 구현하지 못했다.

## 마치며

반성할 점 밖에 남지 않은 프로젝트였다. 

### 반성할 점

+ 설계 단계에서 기능을 명확하게 구분해야 한다.

설계가 명확하지 않으니 모든 기능을 추가할 때마다 어떤 코드를 사용해야 하는지 일일이 찾게되었다.

코드 지식이 빈약했던 탓도 있겠지만 설계가 명확했다면 코드를 추가할수록 전체 구조가 파악하기 힘들어지는 일은 없었을 것이다.

+ 코드의 의미를 정확히 알아야 한다.

제대로 이해하지 않고 코드를 쓰니 클래스와 인스턴스를 다룰 때나 UI를 디자인하는 데 어려움을 겪었다.

프로젝트 기간 동안 대부분의 시간을 코드 서칭에 할애하느라 프로젝트를 완성하지 못했다.

+ 작업 과정을 단계별로 문서화해야한다.

정신없이 코드를 고치고 확인하기만 반복하다 보니 중간 과정을 기록하는 것을 잊었다.

어떤 부분에서 어떻게 수정을 시도했는지에 대한 기록이 거의 없다.

### 배운 점

+ 프로젝트 덕분에 현재 나의 위치와 크게 개선해야할 점이 보였다.

+ 코딩에 대한 것 외에도 프로젝트를 깃헙에 업로드하는 과정, 보고서를 작성하는 과정을 통해 효율적으로 작업을 문서화하는 방법을 배웠다.
          

