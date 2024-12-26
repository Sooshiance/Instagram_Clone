import React, { useEffect, useState } from 'react';
import Header from '../Header';
import Footer from '../Footer';
import apiCall from '../../services/apiCall';
import { useNavigate } from 'react-router';
import ProfileData from '../../utils/ProfileData';

const AllPost = () => {
    // See most rated & visited Posts

    const [posts, setPosts] = useState([]);
    const [error, setError] = useState(null);

    const navigate = useNavigate();

    useEffect(() => {
        //
        const fetchPost = async () => {
            const token = localStorage.getItem("");
            if (!token) {
                navigate('/login');
            }
            try {
                const response = await apiCall.get("explorer/",
                    { headers: { 'Authorization': `Bearer ${token}` } }
                );

                if (response.status === 200) {
                    setPosts(response);
                }
            } catch (error) {
                setError(error);
            }
        }

        fetchPost();
    }, [])

    const seeProfile = (pk) => {
        ProfileData(pk);
    }

    if (error) return (<> {error} </>);

    return (
        <>
            <Header />
            <div>
                {posts.map((post) => {
                    <h1>
                        {post.pk}
                        <div>
                            <button onSubmit={seeProfile(post.user.pk)}>
                                {post.user.pk}
                            </button>
                        </div>
                    </h1>
                })}
            </div>
            <Footer />
        </>
    )
};

export default AllPost;