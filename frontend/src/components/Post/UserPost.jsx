import React from 'react';
import Header from '../Header';
import Footer from '../Footer';
import { useQuery } from '@tanstack/react-query';
import apiCall from '../../services/apiCall';
import { useNavigate, Link } from 'react-router-dom';

const UserPost = () => {
    const navigate = useNavigate();

    const fetchUserPosts = async () => {
        const token = localStorage.getItem('accessToken');
        if (!token) {
            throw new Error('No access token found');
        }

        const response = await apiCall.get('post/view/post/', {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        return response.data;
    };

    const { data: posts, error, isLoading } = useQuery({
        queryKey: ['userPosts'],
        queryFn: fetchUserPosts,
        onError: (error) => {
            if (error.message === 'No access token found') {
                navigate('/login');
            }
        }
    });

    if (isLoading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    return (
        <>
            <Header />
            {posts.map((post) => (
                <div key={post.pk}>
                    <h3>{post.user.username}</h3>
                    <p>{post.caption}</p>
                    <p>Likes: {post.likes}</p>
                    <Link to={`/user-post/${post.pk}`}>See this Post</Link>
                </div>
            ))}
            <Footer />
        </>
    );
};

export default UserPost;
