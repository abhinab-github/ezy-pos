import React from 'react';
import { Navbar, Nav, Form, FormControl, Button } from 'react-bootstrap';

const TopNav = () => {
  return (
    <Navbar bg="light" expand="lg" className="mb-4">
      <Navbar.Brand href="#" style={{marginLeft:"2em"}}>Dashboard</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      {/* <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="#">Home</Nav.Link>
        </Nav>
        <Form inline>
          <FormControl type="text" placeholder="Search" className="mr-sm-2" />
          <Button variant="outline-success">Search</Button>
        </Form>
      </Navbar.Collapse> */}
    </Navbar>
  );
};

export default TopNav;
