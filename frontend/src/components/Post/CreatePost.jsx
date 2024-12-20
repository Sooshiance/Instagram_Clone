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
    const [imageFiles, setImageFiles] = useState([]); // State for image files

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
            }
        }
    };

    return (
        <>
            <Header />
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="caption">Caption:</label>
                    <textarea id="caption" value={caption} onChange={handleCaptionChange} />
                </div>
                <div>
                    <label htmlFor="location">Location:</label>
                    <input type="text" id="location" value={location} onChange={handleLocationChange} />
                </div>
                <div>
                    <label htmlFor="images">Images:</label>
                    <input type="file" id="images" multiple onChange={handleImageChange} />
                </div>
                <button type="submit">Create Post</button>
            </form>
            <Footer />
        </>
    );
};

export default CreatePost;