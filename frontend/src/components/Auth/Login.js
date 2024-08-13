import React, { useState } from 'react';
import { Form, Button, Container, Card } from 'react-bootstrap';
import api from '../../axiosConfig';

const Login = ({ onLogin }) => { // Accept onLogin as a prop
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/auth/login', formData);
      localStorage.setItem('token', response.data.access_token);
      alert('Login successful!');
      onLogin(); // Call onLogin to update the app state and navigate to the home page
    } catch (error) {
      console.error('Error logging in:', error);
      alert('Invalid credentials!');
    }
  };

  return (
    <Container>
      <Card className="p-4 mt-4">
        <Card.Title>Login</Card.Title>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="formEmail">
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="email"
              placeholder="Enter email"
              name="email"
              value={formData.email}
              onChange={handleChange}
            />
          </Form.Group>

          <Form.Group controlId="formPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Enter password"
              name="password"
              value={formData.password}
              onChange={handleChange}
            />
          </Form.Group>

          <Button variant="primary" type="submit">
            Login
          </Button>
        </Form>
      </Card>
    </Container>
  );
};

export default Login;
