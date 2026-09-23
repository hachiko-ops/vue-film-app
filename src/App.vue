<script setup lang="ts">
import SearchBarHeader from './components/SearchBarHeader.vue';
import FilmItem from './components/FilmItem.vue';
import { useFilmStore } from './store';
import FilmDetailsModal from './components/FilmDetailsModal.vue';
import { computed } from 'vue';

const store = useFilmStore();
</script>

<template>
  <SearchBarHeader />
  <div class="section mt-0 pt-0" v-if="! store.showWishlist">
    <div class="columns">
      <div class="column is-full has-text-left">
        <h2 class="subtitle is-5" v-if="store.films.length > 0">
          {{ store.films.length }} films found for "{{ store.searchTerm }}"
        </h2>
      </div>
    </div>
    <div class="fixed-grid has-4-cols" v-if="store.films.length > 0">
      <div class="grid">
        <div class="cell" v-for="film in store.films" :key="film.imdbID">
          <FilmItem :film="film" />
        </div>
      </div>
    </div>
  </div>

<div class="section mt-0 pt-0" v-if="store.showWishlist">
    <div class="columns">
      <div class="column is-full has-text-left">
        <h2 class="subtitle is-5" v-if="store.wishlist.length > 0">
          Films in your  wishlist: {{ store.wishlist.length }}
        </h2>
      </div>
    </div>
    <div class="fixed-grid has-4-cols" v-if="store.wishlist.length > 0">
      <div class="grid">
        <div class="cell" v-for="film in store.wishlist" :key="film.imdbID">
          <FilmItem :film="film" />
        </div>
      </div>
    </div>
  </div>  
  <FilmDetailsModal />
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
