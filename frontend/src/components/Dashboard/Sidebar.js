import React from 'react';
import { Nav } from 'react-bootstrap';

const Sidebar = ({ setCurrentPage }) => {
  return (
    <div className="d-flex flex-column vh-100 bg-dark text-white">
      <div className="p-3">
        <h2>EZYBUYSELL</h2>
      </div>
      <Nav className="flex-column p-3">
        <Nav.Link onClick={() => setCurrentPage('home')} className="text-white">Dashboard</Nav.Link>
        <Nav.Link onClick={() => setCurrentPage('inventory')} className="text-white">Inventory</Nav.Link>
        <Nav.Link onClick={() => setCurrentPage('customers')} className="text-white">Customers</Nav.Link>
        <Nav.Link onClick={() => setCurrentPage('sales')} className="text-white">Sales</Nav.Link>
        <Nav.Link onClick={() => setCurrentPage('buy')} className="text-white">Buy</Nav.Link>
        {/* <Nav.Link onClick={() => setCurrentPage('signup')} className="text-white">Signup</Nav.Link>
        <Nav.Link onClick={() => setCurrentPage('login')} className="text-white">Login</Nav.Link> */}
      </Nav>
    </div>
  );
};

export default Sidebar;
