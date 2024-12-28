// frontend/src/services/api.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

export const generateStory = async (input) => {
    try {
        const response = await axios.post(`${API_URL}/generate`, input);
        return response.data;
    } catch (error) {
        console.error(error);
        throw error;
    }
};
