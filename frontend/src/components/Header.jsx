// /src/components/Header.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import authService from '../services/authService';

const Header = () => {
    const isAuthenticated = authService.isAuthenticated();

    return (
        <nav className="bg-white shadow-md">
            <div className="container mx-auto flex flex-wrap justify-between items-center p-4">
                <div className="flex items-center space-x-2">
                    <Link to="/" className="font-bold text-xl text-blue-600">Social Media</Link>
                    <span className="hidden md:block text-gray-400">|</span>
                    <Link to="/" className="text-gray-600 hover:text-blue-600">Explorer</Link>
                </div>

                <div className="flex items-center space-x-6">
                    {isAuthenticated ? (
                        <>
                            <Link to="/profile" className="text-gray-600 hover:text-blue-600">Profile</Link>
                            <Link to="/logout" className="text-gray-600 hover:text-blue-600">Logout</Link>
                        </>
                    ) : (
                        <>
                            <Link to="/login" className="text-gray-600 hover:text-blue-600">Login</Link>
                            <Link to="/register" className="text-gray-600 hover:text-blue-600">Register</Link>
                        </>
                    )}
                </div>
            </div>
        </nav>
    );
}

export default Header;