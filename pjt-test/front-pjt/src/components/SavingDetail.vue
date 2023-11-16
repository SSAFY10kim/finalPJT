<template>
  <div>
    <div v-if="saving_option" class="saving_option">
      <p>{{ saving_option.intr_rate_type_nm }}</p>
      <p>{{ saving_option.rsrv_type_nm }}</p>
      <p>금리 : {{ saving_option.intr_rate }}</p>
      <p>우대금리 : {{ saving_option.intr_rate2 }}</p>
      <p>기간 : {{ saving_option.save_trm }}개월</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  saving_option: Object
})

</script>

<style>
.saving_option{
  font-size: 13px;
}
</style>
  