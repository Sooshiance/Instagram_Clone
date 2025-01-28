import React, { useEffect, useState } from 'react';
import Header from '../Header';
import Footer from '../Footer';
import apiCall from '../../services/apiCall';
import { useNavigate } from 'react-router';
import UserPost from '../Post/UserPost';

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

    const updateUserProfile = () => {
        //
        navigate("/update-profile");
    }

    const createPost = () => {
        navigate("/create/user-post");
    }

    if (error) return (
        <>
            <Header />
            {error.message}
            <Footer />
        </>
    )

    return (
        <>
            {profile ? (
                <>
                    <Header />
                    <UserPost />
                    <h1 className="">
                        {profile.username}
                    </h1>
                    <button onClick={updateUserProfile}
                        type="button"
                        className="mb-2 block w-full rounded bg-primary px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] transition duration-150 ease-in-out hover:bg-primary-600 hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:bg-primary-600 focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] focus:outline-none focus:ring-0 active:bg-primary-700 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(59,113,202,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.2),0_4px_18px_0_rgba(59,113,202,0.1)]">
                        Update your Profile
                    </button>
                    <button onClick={createPost}>
                        Create Post
                    </button>
                    <Footer />
                </>
            ) : (
                <>
                    <Header />
                    <p>Loading...</p>
                    <Footer />
                </>
            )}
        </>
    )
}

export default Profile