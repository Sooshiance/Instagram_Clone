import './App.css';
import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './components/Home/Home';
import Login from './components/Auth/Login';
import Profile from './components/Client/Profile';
import UpdateProfile from './components/Client/UpdateProfile';
import Register from './components/Auth/Register';
import Logout from './components/Auth/Logout';
import OTPRequest from './components/Auth/OTPRequest';
import OTPVerify from './components/Auth/OTPVerify';
import PasswordReset from './components/Auth/PasswordReset';
import UserPost from './components/Post/UserPost';
import CreatePost from './components/Post/CreatePost';
import SinglePost from './components/Post/SinglePost';
import NoPage from './components/NoPage';
import PrivateRoute from './components/PrivateRoute';

function App() {
  return (
    <div className="App ">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/request-otp" element={<OTPRequest />} />
        <Route path="/verify-otp" element={<OTPVerify />} />
        <Route path="/password-reset" element={<PasswordReset />} />
        <Route path="/logout" element={
          <PrivateRoute>
            <Logout />
          </PrivateRoute>
        } />
        <Route path="/profile" element={
          <PrivateRoute>
            <Profile />
          </PrivateRoute>
        } />
        <Route path="/update-profile" element={
          <PrivateRoute>
            <UpdateProfile />
          </PrivateRoute>
        } />
        <Route path="/user-post" element={
          <PrivateRoute>
            <UserPost />
          </PrivateRoute>
        } />
        <Route path="/create/user-post" element={
          <PrivateRoute>
            <CreatePost />
          </PrivateRoute>
        } />
        <Route path="/user-post/:pk" element={
          <PrivateRoute>
            <SinglePost />
          </PrivateRoute>
        } />
        <Route path='*' element={<NoPage />} />
      </Routes>
    </div>
  );
}

export default App;
