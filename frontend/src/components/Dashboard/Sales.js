import React, { useState, useEffect } from 'react';
import { Container, Card, Form, Button, Table } from 'react-bootstrap';
import Select from 'react-select';
import api from '../../axiosConfig';

const Sales = () => {
  const [sales, setSales] = useState([]);
  const [customers, setCustomers] = useState([]);
  const [inventory, setInventory] = useState([]);
  const [formData, setFormData] = useState({
    customer_id: '',
    inventory_id: '',
    discount_price: '',
    payment_method: 'cash',
    selling_price: '',
    total_price: ''
  });

  useEffect(() => {
    fetchSales();
    fetchCustomers();
    fetchInventory();
  }, []);

  const fetchSales = async () => {
    try {
      const response = await api.get('/sale');
      setSales(response.data);
    } catch (error) {
      console.error('Error fetching sales:', error);
    }
  };

  const fetchCustomers = async () => {
    try {
      const response = await api.get('/customer');
      setCustomers(response.data.map(customer => ({
        value: customer.id,
        label: customer.name
      })));
    } catch (error) {
      console.error('Error fetching customers:', error);
    }
  };

  const fetchInventory = async () => {
    try {
      const response = await api.get('/inventory');
      setInventory(response.data.map(item => ({
        value: item.id,
        label: item.name
      })));
    } catch (error) {
      console.error('Error fetching inventory:', error);
    }
  };

  const handleSelectChange = (selectedOption, { name }) => {
    setFormData({
      ...formData,
      [name]: selectedOption ? selectedOption.value : ''
    });
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    const updatedFormData = {
      ...formData,
      [name]: value,
    };

    // Automatically calculate total_price whenever selling_price or discount_price changes
    if (name === 'selling_price' || name === 'discount_price') {
      const sellingPrice = parseFloat(updatedFormData.selling_price) || 0;
      const discountPrice = parseFloat(updatedFormData.discount_price) || 0;
      updatedFormData.total_price = sellingPrice - discountPrice;
    }

    setFormData(updatedFormData);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/sale', formData);
      fetchSales();
      window.open(response.data.invoice_url, '_blank'); // Open the invoice in a new window
    } catch (error) {
      console.error('Error completing sale:', error);
    }
  };

  const handleInvoice = (url) => {
    window.open(url, '_blank'); // Open the invoice in a new window
  };

  return (
    <Container>
      <Card className="p-4 mb-4">
        <Card.Title>Sales Management</Card.Title>
        <Card.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="formCustomerId">
              <Form.Label>Customer</Form.Label>
              <Select
                name="customer_id"
                options={customers}
                value={customers.find(option => option.value === formData.customer_id)}
                onChange={handleSelectChange}
                placeholder="Select a customer"
              />
            </Form.Group>

            <Form.Group controlId="formInventoryId">
              <Form.Label>Inventory</Form.Label>
              <Select
                name="inventory_id"
                options={inventory}
                value={inventory.find(option => option.value === formData.inventory_id)}
                onChange={handleSelectChange}
                placeholder="Select an inventory item"
              />
            </Form.Group>

            <Form.Group controlId="formSellingPrice">
              <Form.Label>Selling Price</Form.Label>
              <Form.Control
                type="number"
                placeholder="Enter selling price"
                name="selling_price"
                value={formData.selling_price}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="formDiscountPrice">
              <Form.Label>Discount Price</Form.Label>
              <Form.Control
                type="number"
                placeholder="Enter discount price (if any)"
                name="discount_price"
                value={formData.discount_price}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="formTotalPrice">
              <Form.Label>Total Price</Form.Label>
              <Form.Control
                type="number"
                placeholder="Total price"
                name="total_price"
                value={formData.total_price}
                readOnly
              />
            </Form.Group>

            <Form.Group controlId="formPaymentMethod">
              <Form.Label>Payment Method</Form.Label>
              <Form.Control
                as="select"
                name="payment_method"
                value={formData.payment_method}
                onChange={handleChange}
              >
                <option value="cash">Cash</option>
                <option value="card">Card</option>
              </Form.Control>
            </Form.Group>

            <Button variant="primary" type="submit">
              Complete Sale
            </Button>
          </Form>
        </Card.Body>
      </Card>

      <Card>
        <Card.Body>
          <Card.Title>Sales History</Card.Title>
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Customer</th>
                <th>Inventory</th>
                <th>Selling Price</th>
                <th>Discount Price</th>
                <th>Total Price</th>
                <th>Payment Method</th>
                <th>Date</th>
                <th>Invoice</th>
              </tr>
            </thead>
            <tbody>
              {sales.map(sale => (
                <tr key={sale.id}>
                  <td>{sale.customer_name}</td>
                  <td>{sale.item_name}</td>
                  <td>${sale.selling_price}</td>
                  <td>${sale.discount_price}</td>
                  <td>${sale.total_price}</td>
                  <td>{sale.payment_method}</td>
                  <td>{new Date(sale.sale_date).toLocaleString()}</td>
                  <td>
                    <Button variant="info" onClick={() => handleInvoice(`/sale/invoice/${sale.id}`)}>
                      View Invoice
                    </Button>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default Sales;
