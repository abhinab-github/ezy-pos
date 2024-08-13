import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, Tabs, Tab } from 'react-bootstrap';
import api from '../../axiosConfig'; // Assuming you have an axiosConfig file

const Home = () => {
  const [key, setKey] = useState('daily');
  const [dailyData, setDailyData] = useState({ purchases: 0, sales: 0, profit: 0 });
  const [monthlyData, setMonthlyData] = useState({ purchases: 0, sales: 0, profit: 0 });

  useEffect(() => {
    fetchData();
  }, [key]);

  const fetchData = async () => {
    try {
      const response = await api.get(`/dashboard/${key}`);
      if (key === 'daily') {
        setDailyData(response.data);
      } else {
        setMonthlyData(response.data);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const currentData = key === 'daily' ? dailyData : monthlyData;

  return (
    <Container fluid>
      <Tabs
        id="controlled-tab-example"
        activeKey={key}
        onSelect={(k) => setKey(k)}
        className="mb-4"
      >
        <Tab eventKey="daily" title="Daily Data">
          <Row>
            <Col md={4}>
              <Card className="text-center mb-4">
                <Card.Body>
                  <Card.Title>Total Purchases</Card.Title>
                  <Card.Text>${currentData.purchases}</Card.Text>
                </Card.Body>
              </Card>
            </Col>
            <Col md={4}>
              <Card className="text-center mb-4">
                <Card.Body>
                  <Card.Title>Total Sales</Card.Title>
                  <Card.Text>${currentData.sales}</Card.Text>
                </Card.Body>
              </Card>
            </Col>
            <Col md={4}>
              <Card className="text-center mb-4">
                <Card.Body>
                  <Card.Title>Profit</Card.Title>
                  <Card.Text>${currentData.profit}</Card.Text>
                </Card.Body>
              </Card>
            </Col>
          </Row>
        </Tab>
        <Tab eventKey="monthly" title="Monthly Data">
          <Row>
            <Col md={4}>
              <Card className="text-center mb-4">
                <Card.Body>
                  <Card.Title>Total Purchases</Card.Title>
                  <Card.Text>${currentData.purchases}</Card.Text>
                </Card.Body>
              </Card>
            </Col>
            <Col md={4}>
              <Card className="text-center mb-4">
                <Card.Body>
                  <Card.Title>Total Sales</Card.Title>
                  <Card.Text>${currentData.sales}</Card.Text>
                </Card.Body>
              </Card>
            </Col>
            <Col md={4}>
              <Card className="text-center mb-4">
                <Card.Body>
                  <Card.Title>Profit</Card.Title>
                  <Card.Text>${currentData.profit}</Card.Text>
                </Card.Body>
              </Card>
            </Col>
          </Row>
        </Tab>
      </Tabs>
    </Container>
  );
};

export default Home;
