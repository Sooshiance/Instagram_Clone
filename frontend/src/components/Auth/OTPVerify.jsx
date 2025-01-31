import React, { useState } from 'react'
import Header from '../Header';
import Footer from '../Footer';
import { useNavigate } from 'react-router-dom';
import apiCall from '../../services/apiCall';

const OTPVerify = () => {

    const [username, setUsername] = useState("");
    const [otp, setOTP] = useState("");
    const navigate = useNavigate();
    const [error, setError] = useState(null);

    const handleOTPRequest = async (e) => {
        e.preventDefault();

        try {
            const response = await apiCall.post("user/verify-otp/", { username, otp });
            if (response.status === 200) {
                navigate("/password-reset");
            } else {
                navigate("/verify-otp");
            }
        } catch (error) {
            setError(error);
        }
    }

    return (
        <>
            <Header />
            <section className="bg-gray-50 dark:bg-gray-900">
                <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                    <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                        <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                            <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                                Verify OTP
                            </h1>
                            <form className="space-y-4 md:space-y-6" onSubmit={handleOTPRequest}>
                                <div className="space-y-4 md:space-y-6">
                                    <label for="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Username</label>
                                    <input value={username} onChange={(e) => setUsername(e.target.value)}
                                        className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                                </div>
                                <div className="space-y-4 md:space-y-6">
                                    <label for="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">OTP</label>
                                    <input value={otp} onChange={(e) => setOTP(e.target.value)}
                                        className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                                </div>
                                <div className="flex items-center justify-between">
                                    <button className='border-gray-300 text-gray-900 rounded-lg'>
                                        Verify OTP
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </section>
            <Footer />
        </>
    )
}

export default OTPVerify