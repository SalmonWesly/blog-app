import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Signup from './components/Signup';
import Login from './components/Login';
import BlogList from './pages/BlogList';
import BlogForm from './components/BlogForm';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/blogs" element={<BlogList />} />
        <Route path="/blogs/create" element={<BlogForm />} />
        <Route path="/blogs/edit/:id" element={<BlogForm />} />
      </Routes>
    </Router>
  );
}

export default App;
