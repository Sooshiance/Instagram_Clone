import React, { useEffect, useState } from 'react'
import Header from '../Header';
import Footer from '../Footer';
import apiCall from '../../services/apiCall';
import { useNavigate, useParams } from 'react-router';

const OtherProfile = () => {
    const [user, setUser] = useState([]);
    const pk = useParams();
    const navigate = useNavigate();
    const [error, setError] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem("accessToken");
        if (!token) {
            navigate('/login');
        }
        const fetchUserProfile = async () => {
            try {
                const response = await apiCall.get(`follow/profile/status/${pk}`, {
                    headers: { 'Authorization': `Bearer ${token}` }
                });
                setUser(response);
            } catch (error) {
                setError(error);
            }
        }
        fetchUserProfile();
    }, [pk])

    if (error) return (<>{error}</>)

    return (
        <>
            <Header />
            <div>
                {user.pk}
            </div>
            <Footer />
        </>
    )
}

export default OtherProfile