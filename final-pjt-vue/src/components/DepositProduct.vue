<template>
    <div>
        <div class="product">
            <p>{{ deposit.fin_prdt_nm }}</p>
            <button @click="likeDeposit(deposit.fin_prdt_cd)" v-if="checkLikes(deposit)">즐겨찾기 제거</button>
            <button @click="likeDeposit(deposit.fin_prdt_cd)" v-else>즐겨찾기</button>
            <p>{{ deposit.kor_co_nm }}</p>
        </div>
        <div>
            <label for="customAmount">예금 금액 :</label>
            <input v-model="customAmount" type="number" id="customAmount" />
        </div>
        <div class="deposit-options-container">
            <DepositDetail
                v-for="deposit_option in deposit.deposit_options"
                :key="deposit_option.id"
                :deposit_option="deposit_option"
                @click="updateRealTimeValue(deposit_option)"
                class="deposit-option"
            />
        </div>
        <div class="real-time-value">
            <p>{{ customAmount }}만원 예금하면 총 세후 이자 : {{ formatNumber(realTimeValue) }}원</p>
        </div>
        <hr>
    </div>
</template>

<script setup>
import DepositDetail from '@/components/DepositDetail.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';

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

</script>

<style scoped>
.product {
    font-size: 25px;
}
.deposit-options-container {
    display: flex;
}

.deposit-option {
    border: solid 1px blue;
    margin-right: 10px;
}

.real-time-value {
    margin-top: 10px;
}
</style>