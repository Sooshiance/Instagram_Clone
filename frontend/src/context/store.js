// src/context/store/store.js
import { configureStore } from '@reduxjs/toolkit';
import authReducer from './auth/authSlice';
import postSlice from './post/postSlice';

export const store = configureStore({
    reducer: {
        auth: authReducer,
        post: postSlice,
    },
});
