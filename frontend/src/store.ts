import { defineStore } from 'pinia';
import axios from 'axios';
import type { Film, AppState, ChatMessage } from './interfaces.ts';
import { API_URL, API_KEY, CHAT_API_URL } from './interfaces';

export const useFilmStore = defineStore('filmStore', {
    state: () => ({
        films: [] as Film[],
        searchTerm: '',
        selectedFilm: null as Film | null,
        isModalOpen: false,
        wishlist: JSON.parse(localStorage.getItem('wishlist') || '[]') as Film[],
        showWishlist: false,
        isChatOpen: false,
        chatMessages: [] as ChatMessage[]
    } as AppState),

    actions: {
        openModal(film: Film): void {
            this.isModalOpen = true;
            getFilmDetails(film);
        },
        closeModal() :void {
            this.isModalOpen = false;
            this.selectedFilm = null;
        },
        toggleWishlist() : void {
            this.showWishlist = !this.showWishlist;
        },
        toggleWishlistItem(film: Film) : void{
            if (!this.wishlist.some(wishlistFilm => wishlistFilm.imdbID === film.imdbID)) {
                this.wishlist.push(film);
            } else {
                this.wishlist = this.wishlist.filter(wishlistFilm => wishlistFilm.imdbID !== film.imdbID);
            }

            localStorage.setItem('wishlist', JSON.stringify(this.wishlist));
        },
        isInWishlist(film: Film) : boolean{
            return this.wishlist.some(wishlistFilm => wishlistFilm.imdbID === film.imdbID);
        },
        openChat():void{
            this.isChatOpen = true;
        },
        closeChat():void {
            this.isChatOpen = false;
        },
        addMessage( newMessage : string ) : void {
            const message: ChatMessage = {
                id: this.chatMessages.length + 1,
                text: newMessage,
                sender: 'user',
                timestamp: new Date()
            };
            this.chatMessages.push(message);
        },
        sendChatMessage( newMessage : string, session_id : string ) : void {
            this.addMessage(newMessage);

            // try {
            //     const response = await axios.get(CHAT_API_URL+'filters/'+session_id+'?message='+newMessage);
            // }
        },
        //searchMovies( t: string, type: string = 'movie', y: string | undefined , ) : void {
    }
});

async function getFilmDetails( film: Film){
  try {
    const response = await axios.get<Film>(API_URL, {
      params: {
        apikey: API_KEY,
        i: film.imdbID
      }});
      const details = response.data;
      useFilmStore().selectedFilm = details;

  } catch (error) {
    console.error('Error fetching details movie:', error);
  }

}
