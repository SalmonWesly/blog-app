import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const BlogList = () => {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/blogs/')
      .then(res => setBlogs(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>All Blogs</h2>
      {blogs.length === 0 && <p>No blogs found</p>}
      <ul>
        {blogs.map(blog => (
          <li key={blog.id}>
            <Link to={`/blogs/${blog.id}`}>{blog.title}</Link> by {blog.author}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BlogList;
