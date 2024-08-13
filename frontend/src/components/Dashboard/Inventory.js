import React, { useState, useEffect } from 'react';
import { Container, Card, Form, Button, Table } from 'react-bootstrap';
import api from '../../axiosConfig';

const Inventory = () => {
  const [inventory, setInventory] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    sku: '',
    buy_price: '',
    sale_price: '',
    image_url: '',
    in_stock: true,
  });

  useEffect(() => {
    fetchInventory();
  }, []);

  const fetchInventory = async () => {
    try {
      const response = await api.get('/inventory');
      setInventory(response.data);
    } catch (error) {
      console.error('Error fetching inventory:', error);
    }
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/inventory', formData);
      fetchInventory();
    } catch (error) {
      console.error('Error adding inventory:', error);
    }
  };

  return (
    <Container>
      <Card className="p-4 mb-4">
        <Card.Title>Inventory Management</Card.Title>
        <Card.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="formName">
              <Form.Label>Name</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter item name"
                name="name"
                value={formData.name}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="formDescription">
              <Form.Label>Description</Form.Label>
              <Form.Control
                as="textarea"
                rows={3}
                name="description"
                value={formData.description}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="formSku">
              <Form.Label>SKU</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter SKU"
                name="sku"
                value={formData.sku}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="formBuyPrice">
              <Form.Label>Buy Price</Form.Label>
              <Form.Control
                type="number"
                placeholder="Enter buy price"
                name="buy_price"
                value={formData.buy_price}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="formSalePrice">
              <Form.Label>Sale Price</Form.Label>
              <Form.Control
                type="number"
                placeholder="Enter sale price"
                name="sale_price"
                value={formData.sale_price}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="formImageUrl">
              <Form.Label>Image URL</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter image URL"
                name="image_url"
                value={formData.image_url}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="formInStock">
              <Form.Check
                type="checkbox"
                label="In Stock"
                name="in_stock"
                checked={formData.in_stock}
                onChange={handleChange}
              />
            </Form.Group>

            <Button variant="primary" type="submit">
              Add Item
            </Button>
          </Form>
        </Card.Body>
      </Card>

      <Card>
        <Card.Body>
          <Card.Title>Inventory List</Card.Title>
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Name</th>
                <th>SKU</th>
                <th>Buy Price</th>
                <th>Sale Price</th>
                <th>In Stock</th>
              </tr>
            </thead>
            <tbody>
              {inventory.map(item => (
                <tr key={item.id}>
                  <td>{item.name}</td>
                  <td>{item.sku}</td>
                  <td>{item.buy_price}</td>
                  <td>{item.sale_price}</td>
                  <td>{item.stock ? 'Yes' : 'No'}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default Inventory;
