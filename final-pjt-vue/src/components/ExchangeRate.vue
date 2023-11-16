<template>
  <div>
    <div class="calculator">
      <label for="mymoney">기준 화폐 : </label>
      <select v-model="myCountry">
        <option v-for="d in data" :value="d.deal_bas_r" :key="d.cur_nm">{{ d.cur_nm }}</option>
      </select>
      <input type="number" id="mymoney" v-model="myMoney" min="0">
      <br>
      <label for="changemoney">환전 금액 : </label>
      <select v-model="changeCountry">
        <option v-for="d in data" :value="d.deal_bas_r" :key="d.cur_nm">{{ d.cur_nm }}</option>
      </select>
      <span>{{ changeMoney }}</span>
      <span>{{ MoneyUnit }}</span>
    </div>
    <br>
    <table class="tg">
      <thead>
        <tr>
          <th class="tg-0lax">국가</th>
          <th class="tg-0lax">화폐단위</th>
          <th class="tg-0lax">매매 기준율</th>
          <th class="tg-0lax">송금받을때</th>
          <th class="tg-0lax">송금보낼때</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="d in data" :key="d.cur_nm">
          <td class="tg-0lax">{{ d.cur_nm }}</td>
          <td class="tg-0lax">{{ d.cur_unit }}</td>
          <td class="tg-0lax">{{ d.deal_bas_r }}</td>
          <td class="tg-0lax">{{ d.ttb }}</td>
          <td class="tg-0lax">{{ d.tts }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import axios from 'axios';

const API_URL = `http://127.0.0.1:8000/api/v1/create_data/`;

const data = ref([]);
const myMoney = ref(0);
const changeMoney = ref(0);
const myCountry = ref(0);
const changeCountry = ref(0);

const japanMoney = ref(0)
const indiaMoney = ref(0)

const MoneyUnit = ref('')

onMounted(() => {
  createExchangeMoney();
});


watch([myMoney, myCountry, changeCountry], () => {
  updateChangeMoney();
  console.log(changeMoney.value)
  console.log(myCountry.value)
  console.log(changeCountry.value)
  console.log(changeMoney.value)

  MoneyUnit.value = data.value.find(d => d.deal_bas_r === changeCountry.value).cur_unit

  if (MoneyUnit.value === 'JPY(100)') {
    MoneyUnit.value = 'JPY'
  } else if ( MoneyUnit.value === 'IDR(100)') {
    MoneyUnit.value = 'IDR'
  }

  if (changeCountry.value === myCountry.value) {
    window.alert('error!!!!')
    changeMoney.value = '다른나라 화폐를 선택해주세요'
  }
});

const exchangeRate = computed(() => {
  let sourceValue = parseFloat(myCountry.value.replace(/,/g,''));
  let targetValue = parseFloat(changeCountry.value.replace(/,/g,''));

  if (myCountry.value === indiaMoney.value || myCountry.value === japanMoney.value) {
    sourceValue = myCountry.value / 100;
  } else if (changeCountry.value === indiaMoney.value || changeCountry.value === japanMoney.value) {
    targetValue = changeCountry.value / 100;
  }

  return sourceValue / targetValue;
});

const updateChangeMoney = () => {
  changeMoney.value = parseFloat((myMoney.value * exchangeRate.value).toFixed(3));
};

const createExchangeMoney = () => {
  axios
    .get(API_URL)
    .then(res => {
      console.log(res)
      data.value = res.data;
      myCountry.value = data.value[13].deal_bas_r; // 초기 선택값 설정
      changeCountry.value = data.value[22].deal_bas_r; // 초기 선택값 설정
      japanMoney.value = data.value[12].deal_bas_r
      indiaMoney.value = data.value[11].deal_bas_r
      MoneyUnit.value = data.value[22].cur_unit
    })
    .catch(err => {
      console.error(err);
    });
};
</script>

<style scoped>
.tg { border-collapse: collapse; border-spacing: 0; }
.tg td { border-color: black; border-style: solid; border-width: 1px; font-family: Arial, sans-serif; font-size: 14px; overflow: hidden; padding: 10px 5px; word-break: normal; }
.tg th { border-color: black; border-style: solid; border-width: 1px; font-family: Arial, sans-serif; font-size: 14px; font-weight: normal; overflow: hidden; padding: 10px 5px; word-break: normal; }
.tg .tg-0lax { text-align: left; vertical-align: top; }
</style>