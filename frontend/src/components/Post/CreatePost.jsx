import { setCaption, setLocation, clearPostState } from '../../context/post/postSlice';
import React, { useState } from 'react';
import Header from '../Header';
import Footer from '../Footer';
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import apiCall from '../../services/apiCall';

const CreatePost = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { caption, location } = useSelector((state) => state.post);
    const [imageFiles, setImageFiles] = useState([]);
    const [error, setError] = useState(null);

    const handleCaptionChange = (e) => {
        dispatch(setCaption(e.target.value));
    };

    const handleLocationChange = (e) => {
        dispatch(setLocation(e.target.value));
    };

    const handleImageChange = (e) => {
        const files = Array.from(e.target.files);
        setImageFiles(files);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('caption', caption);
        formData.append('location', location);
        imageFiles.forEach((file) => {
            formData.append('images', file);
        });

        try {
            const token = localStorage.getItem('accessToken');
            if (!token) {
                console.error('No access token found');
                navigate('/login');
                return;
            }

            const response = await apiCall.post('post/create/post/', formData, {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'multipart/form-data',
                },
            });

            console.log('Post created:', response.data);
            dispatch(clearPostState());

            if (response.status === 201) {
                navigate('/');
            }

        } catch (error) {
            console.error('Error creating post:', error);
            if (error.response) {
                console.error("Error response:", error.response.data);
                setError(error);
            }
        }
    };

    return (
        <>
            <Header />
            <form onSubmit={handleSubmit}>
                <h2 className="text-xl font-semibold mb-4">Create a Post</h2>
                <input
                    type="text"
                    placeholder="Caption"
                    value={caption}
                    onChange={handleCaptionChange}
                    className="w-full p-2 mb-4 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <input
                    type="text"
                    placeholder="Location"
                    value={location}
                    onChange={handleLocationChange}
                    className="w-full p-2 mb-4 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <input
                    type="file"
                    multiple
                    onChange={handleImageChange}
                    className="mb-4"
                />
                <button
                    type="submit"
                    className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition"
                >
                    Create Post
                </button>
                {error && <p className="text-red-500 mt-4">{error}</p>}
            </form>
            <Footer />
        </>
    );
};

export default CreatePost;