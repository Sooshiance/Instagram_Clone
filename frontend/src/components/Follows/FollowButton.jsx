// components/Client/FollowButton.jsx
import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import apiCall from '../../../services/apiCall';

const FollowButton = ({ userId }) => {
    const [isFollowing, setIsFollowing] = useState(false);
    const { accessToken } = useSelector((state) => state.auth);

    useEffect(() => {
        const checkFollowingStatus = async () => {
            try {
                const response = await apiCall.get(`/api/v1/following/${userId}/`, {
                    headers: { 'Authorization': `Bearer ${accessToken}` }
                });
                setIsFollowing(response.data.isFollowing);
            } catch (error) {
                console.error('Error checking following status:', error);
            }
        };

        checkFollowingStatus();
    }, [userId, accessToken]);

    const handleFollow = async () => {
        try {
            await apiCall.post('/api/v1/follow/', { following_id: userId }, {
                headers: { 'Authorization': `Bearer ${accessToken}` }
            });
            setIsFollowing(true);
        } catch (error) {
            console.error('Error following user:', error);
        }
    };

    const handleUnfollow = async () => {
        try {
            await apiCall.delete('/api/v1/follow/', {
                headers: { 'Authorization': `Bearer ${accessToken}` },
                data: { following_id: userId }
            });
            setIsFollowing(false);
        } catch (error) {
            console.error('Error unfollowing user:', error);
        }
    };

    return (
        <button onClick={isFollowing ? handleUnfollow : handleFollow}>
            {isFollowing ? 'Unfollow' : 'Follow'}
        </button>
    );
};

export default FollowButton;