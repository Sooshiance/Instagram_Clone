// src/context/post/postSlice.js
import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    caption: '',
    location: '',
    images: [],
};

const postSlice = createSlice({
    name: 'post',
    initialState,
    reducers: {
        setCaption(state, action) {
            state.caption = action.payload;
            localStorage.setItem('caption', action.payload);
        },
        setLocation(state, action) {
            state.location = action.payload;
            localStorage.setItem('location', action.payload);
        },
        clearPostState(state) {
            state.caption = '';
            state.location = '';
            state.images = [];
            localStorage.removeItem('caption');
            localStorage.removeItem('location');
        },
    },
});

export const { setCaption, setLocation, clearPostState } = postSlice.actions;
export default postSlice.reducer;