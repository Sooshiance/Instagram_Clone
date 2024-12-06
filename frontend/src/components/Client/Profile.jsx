import React, { useEffect, useState } from 'react';
import Header from '../Header';
import Footer from '../Footer';
import apiCall from '../../services/apiCall';
import { useNavigate } from 'react-router';

const Profile = () => {

    const [profile, setProfile] = useState(null);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProfile = async () => {
            const token = localStorage.getItem('accessToken');
            if (!token) {
                navigate('/login');
            }
            try {
                const response = await apiCall.get("user/profile/", {
                    headers: { Authorization: `Bearer ${token}` }
                })
                if (response) {
                    setProfile(response.data);
                    console.log(response.data);
                } else {
                    console.log(response.error);
                    setError(error);
                }
            } catch (error) {
                setError(error);
            }
        };

        fetchProfile();

    }, []);

    if (error) return (
        <>
            <Header />
            {error.message}
            <Footer />
        </>
    )

    return (
        <>
            <Header />
            {profile ? (
                <h1>{profile.username}</h1>
            ) : (
                <p>Loading...</p>
            )}
            <Footer />
        </>
    )
}

export default Profile