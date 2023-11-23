<template>
  <div class="cardpage text-center">
    <h1>신용카드? 체크카드?</h1>
    <div>
    <table class="tg" style="margin: 30px auto;">
<thead>
  <tr>
    <th width="40%" class="tg-4fps" style="text-align: center;">체크카드</th>
    <th width="" class="tg-kftd" style="text-align: center;">특징</th>
    <th width="40%" class="tg-kftd" style="text-align: center;">신용카드</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-gvcd" style="text-align: center;">통장 잔고 내에서만 결제 가능</td>
    <td class="tg-kftd" style="text-align: center;">결제 가능 여부</td>
    <td class="tg-0lax" style="text-align: center;">통장 잔고 없이도 결제 가능</td>
  </tr>
  <tr>
    <td class="tg-gvcd" style="text-align: center;">소득공제 혜택이 있어 안전한 소비가 가능</td>
    <td class="tg-kftd" style="text-align: center;">안전한 소비</td>
    <td class="tg-0lax" style="text-align: center;">큰 결제금액이 필요한 경우 계획적인 소비 가능</td>
  </tr>
  <tr>
    <td class="tg-0lax" style="text-align: center;">통장 잔액과 결제 한도에 따라 결제 가능</td>
    <td class="tg-kftd" style="text-align: center;">한도 조정</td>
    <td class="tg-0lax" style="text-align: center;">신용카드 한도는 신용도에 따라 동적으로 조정 가능</td>
  </tr>
  <tr>
    <td class="tg-0lax" style="text-align: center;">통장 잔액과 소득으로 인한 평가</td>
    <td class="tg-kftd" style="text-align: center;">신용평가</td>
    <td class="tg-0lax" style="text-align: center;">신용도, 소득, 금융거래 실적 등으로 평가</td>
  </tr>
  <tr>
    <td class="tg-0lax" style="text-align: center;">소비에 제한이 있어 소비 패턴을 관리 가능</td>
    <td class="tg-kftd" style="text-align: center;">유동적 소비</td>
    <td class="tg-0lax" style="text-align: center;">유동적으로 큰 결제금액을 나누어 낼 수 있음</td>
  </tr>
  <tr>
    <td class="tg-0lax" style="text-align: center;">혜택이 있지만 신용카드보다는 적음</td>
    <td class="tg-kftd" style="text-align: center;">혜택 및 포인트 적립</td>
    <td class="tg-b6oq" style="text-align: center;">혜택이 풍부하고 포인트를 쌓아 현금처럼 사용 가능</td>
  </tr>
</tbody>
</table>
</div>
      <div class="description text-center">
        <h2><i class="bi bi-question-circle-fill"></i>왜 신용카드와 체크카드를 구분해야 하나요?</h2>
        <p v-html="description.replace(/\n/g, '<br>')"></p>
      </div>
  </div>
</template>

<script setup>
const description = '체크카드와 신용카드는 지출 관리와 소비 습관에 따라 선택해야 합니다.<br> 체크카드는 통장 잔고 내에서만 결제 가능하여 안전한 소비가 가능하며, 소득공제 혜택이 있습니다.<br> 반면, 신용카드는 통장 잔고 없이도 결제가 가능하며 큰 결제금액을 나눠 낼 수 있어 계획적인 소비에 용이합니다.<br> 또한, 신용카드는 혜택이 풍부하고 포인트를 쌓아 현금처럼 사용할 수 있습니다.'
</script>

<style scoped>
.cardpage {
  width: 85%;
  margin: 0 auto;
}

.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal; text-align: center; vertical-align: middle; }
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal; text-align: center; vertical-align: middle; }
.tg .tg-4fps{background-color:#efefef;border-color:#000000;color:#000000;text-align:center;vertical-align:middle}
.tg .tg-gvcd{background-color:#ffffff;border-color:#000000;color:#000000;text-align:center;vertical-align:middle}
.tg .tg-kftd{background-color:#efefef;text-align:center;vertical-align:middle}
.tg .tg-0lax{text-align:center;vertical-align:middle}
.tg .tg-b6oq{color:#374151;text-align:center;vertical-align:middle}
</style>
