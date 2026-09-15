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
  </header>
</template>

<script setup>
import { ref, watch } from 'vue';
import { debounce } from 'lodash-es';
import axios from 'axios';

const API_URL = 'https://www.omdbapi.com/';
const API_KEY = 'ad38cdaa';
  
const inputSearch = ref('');

const emit = defineEmits(['updateFilms'])

// Viene chiamata ogni volta che l'utente smette di scrivere per 300millisecondi
const updateDebounced = debounce(() => {
  searchMovie();
}, 300);

watch(inputSearch, (val) => {
  updateDebounced(val)
})

async function searchMovie(){
  const response = await axios.get(API_URL, {
  params: {
    apikey: API_KEY,
    s: inputSearch.value
  }});

  if( response.data.totalResults > 0 ) {
    emit('updateFilms', response.data.Search);
  }
}
</script>