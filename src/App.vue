<script setup>
import { ref } from 'vue';
import SearchBarHeader from './components/SearchBarHeader.vue';

let films = ref([]);

</script>

<template>
  <SearchBarHeader @updateFilms="films = $event" />
  <div class="columns">
    <div class="column is-full">
      <div class="is-size-3">Film</div>
    </div>
  </div>
  <div class="fixed-grid has-4-cols" v-if="films.length > 0">
    <div class="grid">
      <div class="cell" v-for="film in films" :key="film.imdbID">
        <div class="card">
          <div class="card-image">
            <figure class="image is-4by3">
              <img :src="film.Poster" :alt="film.Title" />
            </figure>
          </div>
          <div class="card-content">

            <div class="content">
              <h3 class="is-size-4">{{ film.Title }}</h3>
              <br />
              <span class="is-uppercase is-size-6 has-text-grey">{{ film.Type }}</span> -
              <time datetime="{{ film.Year }}">{{ film.Year }}</time>
            </div>
          </div>
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
