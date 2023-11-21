<template>
    <div>
        <div class="product">
            <img :src="`/bank/${deposit.kor_co_nm}.png`" alt="은행 로고" style="height: 100px; width: 300px;"><br>
            <p class="p1">{{ deposit.kor_co_nm }}</p>
            <p class="p1">{{ deposit.fin_prdt_nm }}</p>
            <p style="display: inline-block;" class="like">관심 상품 </p>
            <button @click="likeDeposit(deposit.fin_prdt_cd)" v-if="checkLikes(deposit)"><i class="bi bi-star-fill" style="font-size: 30px;"></i></button>
            <button @click="likeDeposit(deposit.fin_prdt_cd)" v-else style="font-size: 30px;"><i class="bi bi-star"></i></button>
        </div>
        <div class="depositcomponent">
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
        <div class="deposit-options-container">
            <DepositDetail
                v-for="deposit_option in deposit.deposit_options"
                :key="deposit_option.id"
                :deposit_option="deposit_option"
                @click="updateRealTimeValue(deposit_option)"
                class="deposit-option"
                :class="{ isHighlighted: deposit_option.highlighted }"
                @mouseover="highlightOption(deposit_option)"
                @mouseleave="resetPosition(deposit_option)"
            />
        </div>
        <div class="real-time-value d-flex justify-content-center">
            <p>{{ customAmount }}원 예금하면 총 세후 이자 : {{ formatNumber(realTimeValue) }}원</p>
        </div>
        </div>
        <div class="text-center">
            <b-button variant="outline-primary" class="custom-button">
                <RouterLink :to="{name: 'deposit_detail', params: {deposit_id: deposit.fin_prdt_cd}}">
                자세히보기
                </RouterLink>
            </b-button>
        </div>
        <hr>
    </div>
</template>

<script setup>
import DepositDetail from '@/components/DepositDetail.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { RouterLink, RouterView } from 'vue-router'

const store = useCounterStore()

defineProps({
    deposit: Object
})

const realTimeValue = ref('')
const customAmount = ref(10000000);

const updateRealTimeValue = (deposit_option) => {
    if (deposit_option.intr_rate_type_nm === "단리") {
        realTimeValue.value = Math.round(customAmount.value * deposit_option.intr_rate2 / 100 * deposit_option.save_trm / 12 * 0.846)
    } else {
        realTimeValue.value = Math.round((customAmount.value * (1 + deposit_option.intr_rate2 / 100 / 12) ** deposit_option.save_trm - customAmount.value)  * 0.846)
    }
}

const formatNumber = (number) => {
    return number.toLocaleString()
}

const buttonText = ref('즐겨찾기')

const likeDeposit = function (temp) {

// console.log(`${store.API_URL}/${temp}/likes/`)

axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/deposit/likes/${temp}/`,
    headers: {
    Authorization: `Token ${store.token}`
}
})
    .then((res) => {
        console.log(res)
        if (res.data.is_like_deposit) {
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

const checkLikes = function (deposit) {
    if (store.userInfo.like_deposit.some(item => item.fin_prdt_cd === deposit.fin_prdt_cd)) {
        return true
    } else {
        return false
    }
}

const goDetail = (data) => {
    router
}

const test = (temp) => {
    console.log(temp)
}

const highlightOption = (deposit_option) => {
  deposit_option.highlighted = true;
};

const resetPosition = (deposit_option) => {
    deposit_option.highlighted = false;
};

</script>

<style scoped>
.products > span{
    font-size: 24px;
    margin: 40px
}

.product > .p1 {
    font-size: 20px;
    margin: 0px 40px;
}
.deposit-options-container {
    display: flex;
    gap: 40px;
    margin: 0 10%;
    justify-content: center;
    text-align: center;
    margin-top: 20px;
}

.deposit-option {
    background-color: #E6E6FA;
    border-radius: 8%;
    margin-right: 10px;
    transition: transform 0.5s, font-weight 0.5s, width 0.5s, height 0.5s, font-size 0.5s;
}

.real-time-value {
    margin-top: 10px;
}

.deposit-option.isHighlighted {
    transform: translateY(-5px); /* 마우스 호버 시 변경할 스타일 지정 */
    /* font-weight: bold; */
    /* width: 150px; 마우스 호버 시 변경할 너비 지정 */
    /* height: 200px; 마우스 호버 시 변경할 높이 지정 */
    /* font-size: 30px; 마우스 호버 시 변경할 폰트 크기 지정 */
    background-color: #8AC3E5;
    color: white;  
}

#customAmount {
    border: 1px solid black;
}

.like {
    font-size: 30px;
    margin-right: 10px;
    margin-left: 40px
}
a {
  text-decoration: none; /* 밑줄 없애기 */
  color: black; /* 마우스를 올렸을 때의 글자 색상 */
}

a:hover {
    color: white;
}

.custom-button:hover {
    background-color: #8AC3E5; /* 마우스를 올렸을 때의 배경 색상 */
    
}

.custom-button {
    border: none;
    background-color: #E6E6FA;
}

.p1 {
    font-size: 40px;
}


</style>