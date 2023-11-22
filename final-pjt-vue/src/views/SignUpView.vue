<template>
<div class="text-center" id="signuppage">
  <div id="loginBoxTitle">Simplify SignUp</div>
    <form @submit.prevent="signUp" style="width: 50%;">
        <div class="form-group">
          <span for="exampleInputEmail1" class="form-label mt-4">아이디</span>
            <input type="text" class="form-control" id="exampleInputEmail1" v-model.trim="username">
        </div>
				<div class="form-group">
					<span class="form-label mt-4" for="inputValid">비밀번호</span>
					<input type="password" class="form-control" v-model.trim="password1">
				</div>

				<div class="form-group">
					<span class="form-label mt-4" for="inputInvalid">비밀번호 재확인</span> 
					<input type="password" class="form-control" v-model.trim="password2">
				</div>
          <div class="form-group">
            <span for="exampleInputEmail1" class="form-label mt-4">이름</span>
              <input type="text" class="form-control" id="exampleInputEmail1" v-model.trim="realname">
          </div>
          <div class="form-group">
            <span for="exampleInputEmail1" class="form-label mt-4">나이</span>
              <input type="number" class="form-control" id="exampleInputEmail1"  v-model.trim="age">
          </div>
			    <div class="form-group">
			      <span for="exampleSelect1" class="form-label mt-4">성별</span>
			      <select class="form-select" id="exampleSelect1"  v-model.trim="gender">
			        <option>남자</option>
			        <option>여자</option>
			      </select> 
			    </div>
          <div class="form-group">
            <span for="exampleInputEmail1" class="form-label mt-4">연봉</span>
              <input type="number" class="form-control" id="exampleInputEmail1"  v-model.trim="salary">
          </div>   
          <div class="form-group">
            <span for="exampleInputEmail1" class="form-label mt-4">재산</span>
              <input type="number" class="form-control" id="exampleInputEmail1"  v-model.trim="money">
          </div>              
          <div class="form-group">
            <span for="exampleSelect1" class="form-label mt-4">주 거래 은행</span>
            <select class="form-select" id="exampleSelect1" v-model="bank">
              <option v-for="b in banks" :value="b">{{ b }}</option>
            </select>
          </div>
				<div class="d-grid gap-2" style="margin-top: 20px; background-color: #E6E6FA; border: none;">
            <button class="btn btn-primary btn-lg" type="submit" style="background-color: #E6E6FA; border: none;">가입하기</button>
        </div>

      </form>
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const realname = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)
const gender = ref(null)
const bank = ref(null)

const signUp = function () {
const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    realname: realname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    gender: gender.value,
    bank: bank.value,
}
store.signUp(payload)
}

const genders = ['남자', '여자']

const banks = ["은행선택","국민은행","우리은행","신한은행","KEB하나은행","한국스탠다드차타드은행","외한은행","한국시티은행","경남은행","광주은행","대구은행","부산은행","전북은행","제주은행","기업은행","농협","수협","한국산업은행","한국수출입은행"]
</script>

<style scoped>
#signuppage {
  width: 85%;
  margin: 0 auto;
}

form {
  margin: 0 auto;
  width: 50%;
  margin-bottom: 100px;
}

#loginBoxTitle {
  color:#000000;
  font-weight: bold;
  font-size: 32px;
  text-transform: uppercase;
  padding: 5px;
  margin-bottom: 20px;
  background: linear-gradient(to right, #270a09, #8ca6ce);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
