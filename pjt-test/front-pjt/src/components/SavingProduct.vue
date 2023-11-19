<template>
    <div>
        <div class="product">
            <p>{{ saving.fin_prdt_nm }}</p>
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
        <!-- 여기가 텍스트 변경한 부분 추가만 하면됨-->
        <div v-if="save_type==='자유적립식'">
            <label for="dates">만기일까지 일수 :</label>
            <input v-model="dates" type="number" id="dates" />
        </div>
        <!--  -->
        <div class="real-time-value">
            <p v-show="save_type==='정액적립식'">월 {{ customAmount }}만원씩 {{ month }}개월 간 적금하면 총 세후 이자 : {{ formatNumber(realTimeValue) }}원</p>
            <p v-show="save_type==='자유적립식'">{{ customAmount }}만원 적금시 만기일 까지 총 세후 이자 : {{ formatNumber(realTimeValue) }}원</p>
        </div>
        <hr>
    </div>
</template>

<script setup>
import SavingDetail from '@/components/SavingDetail.vue'
import { ref } from 'vue'

defineProps({
    saving: Object
})

const realTimeValue = ref('')
const month = ref(null)
// 날짜 변수 추가
const dates = ref(0)
// 
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
        // 자유적립식 계산 코드 수정해야 하는 부분
    } else {
        if (saving_option.intr_rate_type_nm === "단리") {
            realTimeValue.value = Math.round(customAmount.value * saving_option.intr_rate2 / 100 / 365 * dates.value * 0.846)
        } else {
            realTimeValue.value = Math.round(customAmount.value * ((1 + saving_option.intr_rate2 / 100 / 365) ** dates.value - 1) * 0.846)
        }
        // 
    }
}

const formatNumber = (number) => {
    return number.toLocaleString()
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
  