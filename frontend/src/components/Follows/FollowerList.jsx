// components/Client/FollowersList.jsx
import React, { useEffect, useState } from 'react';
import apiCall from '../../../services/apiCall';
import { useSelector } from 'react-redux';

const FollowersList = ({ userId }) => {
    const [followers, setFollowers] = useState([]);
    const { accessToken } = useSelector((state) => state.auth);

    useEffect(() => {
        const fetchFollowers = async () => {
            try {
                const response = await apiCall.get(`/api/v1/followers/${userId}/`, {
                    headers: { 'Authorization': `Bearer ${accessToken}` }
                });
                setFollowers(response.data);
            } catch (error) {
                console.error('Error fetching followers:', error);
            }
        };

        fetchFollowers();
    }, [userId, accessToken]);

    return (
        <div>
            <h3>Followers</h3>
            <ul>
                {followers.map((follower) => (
                    <li key={follower.id}>{follower.username}</li>
                ))}
            </ul>
        </div>
    );
};

export default FollowersList;