<template>
  <div id="exchangepage">
    <h1 style="margin-bottom: 20px;"><i class="bi bi-coin"></i> 환율 계산기</h1>
    <p>환율은 국제 경제, 여행, 외국인 투자 등에 영향을 미치며, 이를 이해하면 금융 행위에 더 나은 판단을 내릴 수 있어 경제적 안정에 도움이 됩니다.</p>
    <div class="calculator">
      <label for="mymoney"></label>
      <select v-model="myCountry">
        <option v-for="d in data" :value="d.deal_bas_r" :key="d.cur_nm">{{ d.cur_nm }}</option>
      </select>
      <input type="number" id="mymoney" v-model="myMoney" min="0">
      <i class="bi bi-arrow-right-square-fill"></i>
      <label for="changemoney"></label>
      <select v-model="changeCountry">
        <option v-for="d in data" :value="d.deal_bas_r" :key="d.cur_nm">{{ d.cur_nm }}</option>
      </select>
      <span>{{ changeMoney }}</span>
      <span v-show="check">{{ MoneyUnit }}</span>
    </div>
    <br>
    <table class="tg table table-hover" style="width: 50%;">
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
const check = ref(true)

onMounted(() => {
  createExchangeMoney();
});


watch([myMoney, myCountry, changeCountry, check], () => {
  updateChangeMoney();
  // console.log(changeMoney.value)
  // console.log(myCountry.value)
  // console.log(changeCountry.value)
  // console.log(changeMoney.value)

  MoneyUnit.value = data.value.find(d => d.deal_bas_r === changeCountry.value).cur_unit

  if (MoneyUnit.value === 'JPY(100)') {
    MoneyUnit.value = 'JPY'
  } else if ( MoneyUnit.value === 'IDR(100)') {
    MoneyUnit.value = 'IDR'
  }

  if (changeCountry.value === myCountry.value) {
    window.alert('error!!!!')
    changeMoney.value = '다른나라 화폐를 선택해주세요'
    check.value = false
  } else {
    check.value = true
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
      // console.log(res)
      data.value = res.data;
      myCountry.value = data.value[13].deal_bas_r; // 초기 선택값 설정
      changeCountry.value = data.value[22].deal_bas_r; // 초기 선택값 설정
      japanMoney.value = data.value[12].deal_bas_r
      indiaMoney.value = data.value[11].deal_bas_r
      MoneyUnit.value = data.value[22].cur_unit
    })
    .catch(err => {
      // console.error(err);
    });
};
</script>

<style scoped>
.tg { border-collapse: collapse; border-spacing: 0; }
.tg td { border-color: black; border-style: solid; border-width: 1px; font-family: Arial, sans-serif; font-size: 14px; overflow: hidden; padding: 10px 5px; word-break: normal; }
.tg th { border-color: black; border-style: solid; border-width: 1px; font-family: Arial, sans-serif; font-size: 14px; font-weight: normal; overflow: hidden; padding: 10px 5px; word-break: normal; }
.tg .tg-0lax { text-align: left; vertical-align: top; }

#exchangepage {
  width: 85%;
  margin: 0 auto;
}

#exchangepage {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 85%;
}

.calculator {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 20px;
}

.tg {
  margin: 0 auto;
}

.calculator {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 10px;
}

label {
  margin-right: 10px;
}

select {
  padding: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 10px;
}

input {
  padding: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 10px;
}

span {
  margin-left: 10px;
}

.bi-arrow-right-square-fill {
  color: black;
  font-size: 20px;
  margin: 0 10px;
}
</style>