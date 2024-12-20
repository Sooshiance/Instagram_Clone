import React, { useEffect, useState } from 'react';
import Header from '../Header';
import Footer from '../Footer';
import apiCall from '../../services/apiCall';
import { useNavigate, useParams } from 'react-router';

const SinglePost = () => {

    const [data, setData] = useState([]);
    const [error, setError] = useState({});

    const navigate = useNavigate();

    const pk = useParams();

    useEffect(() => {

        const token = localStorage.getItem("accessToken");

        if (!token) {
            navigate("/login");
        };

        const fetchData = async () => {
            try {
                const response = await apiCall.get(`post/view/post/${pk}/`, {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                });

                setData(response);
            } catch (error) {
                setError(error);
            }
        }
        fetchData();
    }, []);

    if (error) (<>
        <div>
            {error?.message}
        </div>
    </>)

    return (
        <>
            <Header />
            <div>
                {data.pk}
            </div>
            <Footer />
        </>
    )
}

export default SinglePost;