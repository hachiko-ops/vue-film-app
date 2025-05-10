<template>
  <header>
    <div class="columns">
      <div class="column is-one-fifth is-size-4 has-text-left">Found a movie</div>
      <div class="column">
        <div class="field has-addons">
          <div class="control is-expanded">
            <input class="input" type="text" placeholder="Find a movie" v-model="inputSearch">
          </div>
          <div class="control">
            <button class="button is-info" @click="searchMovie" >
              Search
            </button>
          </div>
        </div>
      </div>
    </div>
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
                    <img
                      :src="film.Poster"
                      :alt="film.Title"
                    />
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
  </header>
</template>

<script setup>
import { ref, watch } from 'vue';
import { debounce } from 'lodash-es';
import axios from 'axios';

const API_URL = 'https://www.omdbapi.com/';
const API_KEY = 'ad38cdaa';
const inputSearch = ref('');

let films = ref([]);

async function searchMovie(){
  const response = await axios.get(API_URL, {
  params: {
    apikey: API_KEY,
    s: inputSearch.value
  }});

  if( response.data.totalResults > 0 ) {
    films.value = response.data.Search;
  }

  console.log(response.data.Search);
}
// Viene chiamata ogni volta che l'utente smette di scrivere per 300millisecondi
const updateDebounced = debounce(() => {
  searchMovie();
}, 300);

watch(inputSearch, (val) => {
  updateDebounced(val)
})


</script>

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
