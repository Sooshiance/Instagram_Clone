// src/utils/authService.js
import apiCall from './apiCall';
import { loginSuccess, logoutSuccess } from '../store/authSlice';
import { store } from '../store/store';

const authService = {
    login: async (credentials) => {
        try {
            const response = await apiCall.post('user/access/', credentials);
            const userData = response.data;

            // Save tokens to local storage
            localStorage.setItem('accessToken', userData.access);
            localStorage.setItem('refreshToken', userData.refresh);

            // Dispatch the loginSuccess action with the user data
            store.dispatch(loginSuccess(userData));

            return userData;
        } catch (error) {
            console.error("Login failed:", error);
            throw error;
        }
    },

    logout: () => {
        // Remove tokens from local storage
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        store.dispatch(logoutSuccess());
    },

    isAuthenticated: () => {
        // Check if tokens exist in local storage
        return !!localStorage.getItem('accessToken');
    }
};

export default authService;