<template>
  <div class="detailpage">
      <div class="product">
          <img :src="`/bank/${saving.kor_co_nm}.png`" alt="은행 로고" style="height: 100px; width: 300px;"><br>
          <p class="p1">{{ saving.kor_co_nm }}</p>
          <p class="p1">{{ saving.fin_prdt_nm }}</p>
          <p style="display: inline-block;" class="like">관심 상품 </p>
          <button @click="likeSaving(saving.fin_prdt_cd)" v-if="checkLikes(saving)"><i class="bi bi-star-fill" style="font-size: 30px;"></i></button>
          <button @click="likeSaving(saving.fin_prdt_cd)" v-else style="font-size: 30px;"><i class="bi bi-star"></i></button>
      </div>
      <div class="savingcomponent">
          <div>
              <label for="customAmount"></label>
              <div class="d-flex justify-content-center">
                  <b-input-group size="lg" style="width: 60%;">
                  <b-input-group-prepend>
                      <b-input-group-text>적립 금액</b-input-group-text>
                  </b-input-group-prepend>

                  <b-form-input v-model="customAmount"></b-form-input>

                  <b-input-group-append >
                      <b-input-group-text style="width: 85px;">원 (₩)</b-input-group-text>
                  </b-input-group-append>
                  </b-input-group>
              </div>
          </div>
              <div class="saving-options-container">
                  <SavingDetail
                      v-for="saving_option in saving.saving_options"
                      :key="saving_option.id"
                      :saving_option="saving_option"
                      @click="updateRealTimeValue(saving_option)"
                      class="saving-option"
                      :class="{ isHighlighted: saving_option.highlighted }"
                      @mouseover="highlightOption(saving_option)"
                      @mouseleave="resetPosition(saving_option)"
                  />
              </div>
          <div v-if="save_type==='자유적립식'">
              <div class="d-flex justify-content-center" style="margin-top: 10px;">
                  <b-input-group size="sm" style="width: 25%;">
                      <b-input-group-prepend>
                              <b-input-group-text>만기일까지?</b-input-group-text>
                              <b-form-input v-if="save_type==='자유적립식'" v-model="dates" type="number" id="dates"></b-form-input>
                              <b-input-group-append >
                                  <b-input-group-text style="width: 85px;">일</b-input-group-text>
                              </b-input-group-append>
                      </b-input-group-prepend>
                  </b-input-group>
              </div>
          </div>
          <div class="real-time-value d-flex justify-content-center">
              <p v-show="save_type==='정액적립식'">월 {{ customAmount }}원씩 {{ month }}개월 간 적금하면 총 세후 이자 : {{ formatNumber(realTimeValue) }}원</p>
              <p v-show="save_type==='자유적립식'">{{ customAmount }}원 적금시 만기일 까지 총 세후 이자 : {{ formatNumber(realTimeValue) }}원</p>
          </div>
      </div>
      <hr>
      <h2>상세정보</h2>
      <p>{{ saving.kor_co_nm }}</p>
      <p v-html="saving.spcl_cnd.replace(/\n/g, '<br>')"></p>
      <p v-html="saving.etc_note.replace(/\n/g, '<br>')"></p>
  </div>
</template>

<script setup>
import SavingDetail from '@/components/SavingDetail.vue'
import { RouterView, useRoute } from 'vue-router';
import axios from 'axios';
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const route = useRoute()
const store = useCounterStore()

const savingCd = route.params.saving_id
const saving = store.savings.find(saving => saving.fin_prdt_cd === savingCd);

console.log(saving)

defineProps({
  saving: Object
})

const realTimeValue = ref('')
const month = ref(null)
const dates = ref(0)
const save_type = ref("정액적립식")
const customAmount = ref(1000000)

const updateRealTimeValue = (saving_option) => { 
  month.value = saving_option.save_trm
  save_type.value = saving_option.rsrv_type_nm
  if (saving_option.rsrv_type_nm === "정액적립식") {
      if (saving_option.intr_rate_type_nm === "단리") {
          realTimeValue.value = Math.round(customAmount.value * saving_option.intr_rate2 / 100 / 12 * saving_option.save_trm * (saving_option.save_trm + 1) / 2 * 0.846)
      } else {
          realTimeValue.value = Math.round(customAmount.value * ((1 + saving_option.intr_rate2 / 100 / 12) * ((1 + saving_option.intr_rate2 / 100 / 12) ** saving_option.save_trm - 1) / ((1 + saving_option.intr_rate2 / 100 / 12) - 1) - saving_option.save_trm) * 0.846)
      }
  } else {
      if (saving_option.intr_rate_type_nm === "단리") {
          realTimeValue.value = Math.round(customAmount.value * saving_option.intr_rate2 / 100 / 365 * dates.value * 0.846)
      } else {
          realTimeValue.value = Math.round(customAmount.value * ((1 + saving_option.intr_rate2 / 100 / 365) ** dates.value - 1) * 0.846)
      }
  }
}

const formatNumber = (number) => {
  return number.toLocaleString()
}

const buttonText = ref('즐겨찾기')

const likeSaving = function (temp) {

  // console.log(`${store.API_URL}/${temp}/likes/`)

  axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/saving/likes/${temp}/`,
      headers: {
      Authorization: `Token ${store.token}`
  }
  })
  .then((res) => {
      console.log(res)
      if (res.data.is_like_saving) {
          alert('관심 목록에 추가되었습니다')
          buttonText.value = '즐겨찾기 제거'
      } else {
          alert('관심 목록에서 제거되었습니다.')
          buttonText.value = '즐겨찾기'
      }
      store.getUser()
  })
  .catch((err) => {
      console.log(err)
  })
}

const checkLikes = function (saving) {
  if (store.userInfo.like_saving.some(item => item.fin_prdt_cd === saving.fin_prdt_cd)) {
      return true
  } else {
      return false
  }
}

const highlightOption = (saving_option) => {
  saving_option.highlighted = true;
};

const resetPosition = (saving_option) => {
  saving_option.highlighted = false;
};  

</script>

<style scoped>
.detailpage {
  width: 85%;
  margin: 0 auto;
}

.products > span{
    font-size: 24px;
    margin: 40px
}

.product > .p1 {
    font-size: 20px;
    margin: 0px 40px;
}
.saving-options-container {
    display: flex;
    gap: 40px;
    margin: 0 10%;
    justify-content: center;
    text-align: center;
    margin-top: 20px;
}

.saving-option {
    background-color: #E6E6FA;
    border-radius: 8%;
    margin-right: 10px;
    transition: transform 0.5s, font-weight 0.5s, width 0.5s, height 0.5s, font-size 0.5s;
}

.real-time-value {
    margin-top: 10px;
}

.saving-option.isHighlighted {
    transform: translateY(-5px); /* 마우스 호버 시 변경할 스타일 지정 */
    /* font-weight: bold; */
    /* height: 200px; 마우스 호버 시 변경할 높이 지정 */
    /* font-size: 30px; 마우스 호버 시 변경할 폰트 크기 지정 */
    /* background-color: #8AC3E5; */
    color: white;  
    background-color: #8AC3E5;
}

#customAmount {
    border: 1px solid black;
}

.like {
    font-size: 30px;
    margin-right: 10px;
    margin-left: 40px
}

</style>
