<template>
  <header>
    <!-- bootstrap3 -->
    <!-- <div>
      <b-button>Button</b-button>
      <b-button variant="danger">Button</b-button>
      <b-button variant="success">Button</b-button>
      <b-button variant="outline-primary">Button</b-button>
    </div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col>1 of 3</b-col>
        <b-col>2 of 3</b-col>
        <b-col>3 of 3</b-col>
      </b-row>
    </b-container> -->

    <!-- vuetify -->
    <!-- <v-card title="Card title" subtitle="Subtitle" text="...">
      <v-card-actions>
        <v-btn>Click me</v-btn>
      </v-card-actions>
    </v-card>
    <v-list lines="one">
      <v-list-item
        v-for="n in 3"
        :key="n"
        :title="'Item ' + n"
        subtitle="Lorem ipsum dolor sit amet consectetur adipisicing elit"
      ></v-list-item>
    </v-list> -->

    <nav>
      <RouterLink :to="{ name: 'home' }">
        [Home]
      </RouterLink>
      <RouterLink :to="{ name: 'deposit' }">
        [Deposit]
      </RouterLink>
      <RouterLink :to="{ name: 'saving' }">
        [Saving]
      </RouterLink>
      <RouterLink :to="{ name: 'exchange' }">
        [Exchange]
      </RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
