//스테이지 변수 설정
var stage = 1;

// 그림, 문제, 정답 선택 번호
//문제, 그림 선택 인덱스
var quesIndex = Math.floor(Math.random() * 4 + 1);
var imagesrc = "./image/lev" + stage + "/" + quesIndex;

//정답 위치 선택 인덱스
var answerSelectIndex = Math.floor(Math.random() * 2);

//정답 주파수
var answerHz;
if (answerSelectIndex === 0) {
  answerHz = "7hz";
} else {
  answerHz = "13hz";
}

//목숨 값
var life = 3;
