// src/context/auth/authUtils
import apiCall from '../../services/apiCall';

export const fetchWithAuth = async (endpoint, navigate) => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
        navigate('/login');
    }
    try {
        const response = await apiCall.get(endpoint, {
            headers: { Authorization: `Bearer ${token}` }
        });
        return response.data;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            navigate('/login');
            console.error("Failed to fetch data:", error);
        }
        throw error;
    }
};

export const sendWithAuth = async (endpoint, navigate, data) => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
        navigate('/login');
    }
    try {
        const response = await apiCall.post(endpoint, data, {
            headers: { Authorization: `Bearer ${token}`, }
        });
        return response.data;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            navigate('/login');
            console.error("Failed to send data:", error);
        }
        throw error;
    }
};

