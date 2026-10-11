<script lang="ts" setup>
import {ref} from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faComment, faPaperPlane} from '@fortawesome/free-solid-svg-icons'
import { useFilmStore } from '../store';

const store = useFilmStore();
const newUserMessage = ref('');

// Generate a unique session ID for the user if it doesn't exist in localStorage
let storeSessionId = localStorage.getItem('session_id');
if( !storeSessionId ) {
    storeSessionId = crypto.randomUUID();
    localStorage.setItem('session_id', storeSessionId);
}

const sendMessage = () => {
    if (newUserMessage.value.trim() !== '') {
        // Send the message to the backend for processing 
        store.sendChatMessage(newUserMessage.value, storeSessionId);

        newUserMessage.value = '';
    }
}
</script>
<template>
    <button class="button is-primary is-rounded chat-trigger-btn"
        :class="{ 'is-hidden': store.isChatOpen }" @click="store.openChat()" aria-label="Open chat" >
        <span class="icon">
            <FontAwesomeIcon :icon="faComment" />
        </span>
    </button>

    <section class="chat-window" :class="{ 'is-hidden': !store.isChatOpen }" >
        <header class="chat-header">
            <div class="is-flex is-align-items-center">
                <span class="chat-avatar">
                    <FontAwesomeIcon :icon="faComment" />
                </span>

                <div>
                    <p class="has-text-weight-semibold">
                        Film Assistant
                    </p>
                    <p class="chat-status">Ask me about films</p>
                </div>
            </div>

            <button class="delete" aria-label="Close chat" @click="store.closeChat()"></button>
        </header>

        <div class="chat-body">
            <div v-for="message in store.chatMessages" :key="message.id" class="chat-row"
                :class="message.sender === 'user' ? 'chat-row-user' : 'chat-row-assistant'" >
                <div class="chat-bubble" :class="message.sender === 'user' ? 'chat-bubble-user' : 'chat-bubble-assistant'" >
                    {{ message.text }}
                </div>
            </div>

            <div v-if="store.isChatLoading" class="chat-row chat-row-assistant">
                <div class="chat-bubble chat-bubble-assistant">
                    Thinking...
                </div>
            </div>
        </div>

        <!-- Input -->
        <footer class="chat-footer">
            <form class="chat-form" @submit.prevent="sendMessage">
                <input
                    class="input chat-input"
                    type="text"
                    placeholder="Ask about a film..."
                    v-model="newUserMessage"
                    :disabled="store.isChatLoading"
                />

                <button
                    class="button is-primary chat-send-btn"
                    type="submit"
                    :disabled="store.isChatLoading || !newUserMessage.trim()"
                    aria-label="Send message"
                >
                    <span class="icon">
                        <FontAwesomeIcon :icon="faPaperPlane" />
                    </span>
                </button>
            </form>
        </footer>
    </section>
</template>