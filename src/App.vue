<script setup lang="ts">
import { ref } from 'vue';
import SearchBarHeader from './components/SearchBarHeader.vue';
import FilmItem from './components/FilmItem.vue';
import type { Film } from './interfaces';

let films = ref<Film[]>([]);
let searchTerm = ref<string>('');

const emit = defineEmits<{
  updateFilms: [films: Film[]],
  inputSearch: [searchTerm: string]
}>();

</script>

<template>
  <SearchBarHeader @updateFilms="films = $event" @inputSearch="searchTerm = $event"/>
  <div class="section mt-0 pt-0">
  <div class="columns">
    <div class="column is-full has-text-left">
      <h2 class="subtitle is-5" v-if="films.length > 0" >
        {{ films.length }} films found for "{{ searchTerm }}"
      </h2>
    </div>
  </div>
  <div class="fixed-grid has-4-cols" v-if="films.length > 0">
    <div class="grid">
      <div class="cell" v-for="film in films" :key="film.imdbID">
        <FilmItem :film="film" />
      </div>
    </div>
  </div>
</div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
