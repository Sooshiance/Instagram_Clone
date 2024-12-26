import { useNavigate } from 'react-router';
import apiCall from '../services/apiCall';

const getProfileData = ({ pk }) => {
    const navigate = useNavigate();

    const token = localStorage.getItem("accessToken");

    // missing the access token unexpectedly
    if (!token) {
        navigate('/login');
    }
    const fetchData = async () => {
        const response = await apiCall.get(`follow/profile/status/${pk}`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (response.status == 200) {
            navigate(`/visit/profile/${pk}`);
        }
        else {
            navigate(`private/profile/${pk}`);
        }
    }

    fetchData();
}

export default getProfileData;