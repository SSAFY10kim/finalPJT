<template>
    <div>
        <div class="product">
            <p>{{ saving.fin_prdt_nm }}</p>
            <button @click="likeSaving(saving.fin_prdt_cd)" v-if="checkLikes(saving)">즐겨찾기 제거</button>
            <button @click="likeSaving(saving.fin_prdt_cd)" v-else>즐겨찾기</button>
            <p>{{ saving.kor_co_nm }}</p>
        </div>
        <div>
            <label for="customAmount">적금 금액 :</label>
            <input v-model="customAmount" type="number" id="customAmount" />
        </div>
        <div class="saving-options-container">
            <SavingDetail
                v-for="saving_option in saving.saving_options"
                :key="saving_option.id"
                :saving_option="saving_option"
                @click="updateRealTimeValue(saving_option)"
                class="saving-option"
            />
        </div>
        <div v-if="save_type==='자유적립식'">
            <label for="dates">만기일까지 일수 :</label>
            <input v-model="dates" type="number" id="dates" />
        </div>
        <div class="real-time-value">
            <p v-show="save_type==='정액적립식'">월 {{ customAmount }}만원씩 {{ month }}개월 간 적금하면 총 세후 이자 : {{ formatNumber(realTimeValue) }}원</p>
            <p v-show="save_type==='자유적립식'">{{ customAmount }}만원 적금시 만기일 까지 총 세후 이자 : {{ formatNumber(realTimeValue) }}원</p>
        </div>
        <hr>
    </div>
</template>

<script setup>
import SavingDetail from '@/components/SavingDetail.vue'
import axios from 'axios';
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

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

</script>

<style scoped>
.product {
    font-size: 25px;
}
.saving-options-container {
    display: flex;
}

.saving-option {
    border: solid 1px blue;
    margin-right: 10px;
}

.real-time-value {
    margin-top: 10px;
}
</style>
  