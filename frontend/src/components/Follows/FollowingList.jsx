// components/Client/FollowingList.jsx
import React, { useEffect, useState } from 'react';
import apiCall from '../../services/apiCall';
import { useSelector } from 'react-redux';

const FollowingList = ({ userId }) => {
    const [following, setFollowing] = useState([]);
    const { accessToken } = useSelector((state) => state.auth);

    useEffect(() => {
        const fetchFollowing = async () => {
            try {
                // const token = localStorage.getItem("accessToken");
                const response = await apiCall.get(`/api/v1/following/${userId}/`, {
                    headers: { 'Authorization': `Bearer ${accessToken}` }
                });
                setFollowing(response.data);
            } catch (error) {
                console.error('Error fetching following:', error);
            }
        };

        fetchFollowing();
    }, [userId, accessToken]);

    return (
        <div>
            <h3>Following</h3>
            <ul>
                {following.map((user) => (
                    <li key={user.id}>{user.username}</li>
                ))}
            </ul>
        </div>
    );
};

export default FollowingList;