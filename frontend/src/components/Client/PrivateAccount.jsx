import React, { useState } from 'react';
import Header from '../Header';
import Footer from '../Footer';
import apiCall from '../../services/apiCall';
import { useNavigate, useParams } from 'react-router';

const PrivateAccount = () => {
    // 

    const pk = useParams();
    const navigate = useNavigate();
    const [error, setError] = useState(null);

    const sendFollowingRequest = async () => {
        //

        const token = localStorage.getItem("accessToken");
        if (!token) {
            navigate('/login');
        }

        try {
            const response = await apiCall.post(`follow/send/notification/`, { 'pk': pk }, {
                headers: { 'Authorization': `Bearer ${token}` }
            })
            if (response.status === 200) {
                navigate('/profile');
            }
        } catch (error) {
            setError(error);
        }
    }

    if (error) return (<>{error}</>)

    return (
        <>
            <Header />
            <div>
                This user has private account 
            </div>
            <div>
                You can send following request to this user 
            </div>
            <button onSubmit={sendFollowingRequest}>
                Send Follow Notification 
            </button>
            <Footer />
        </>
    )
}

export default PrivateAccount;