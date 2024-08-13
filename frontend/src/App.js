import React, { useState } from 'react';
import Sidebar from './components/Dashboard/Sidebar';
import TopNav from './components/Dashboard/TopNav';
import Home from './components/Dashboard/Home';
import Inventory from './components/Dashboard/Inventory';
import Customers from './components/Dashboard/Customers';
import Sales from './components/Dashboard/Sales';
import Buy from './components/Dashboard/Buy';
import Signup from './components/Auth/Signup';
import Login from './components/Auth/Login';

function App() {
  const [currentPage, setCurrentPage] = useState('login'); // Set initial page to login
  const [isAuthenticated, setIsAuthenticated] = useState(false); // Track authentication state

  const handleLogin = () => {
    setIsAuthenticated(true);
    setCurrentPage('home'); // Redirect to home after successful login
  };

  const renderPage = () => {
    if (!isAuthenticated) {
      return <Login onLogin={handleLogin} />; // Show login page if not authenticated
    }

    switch (currentPage) {
      case 'home':
        return <Home />;
      case 'inventory':
        return <Inventory />;
      case 'customers':
        return <Customers />;
      case 'sales':
        return <Sales />;
      case 'buy':
        return <Buy />;
      default:
        return <Home />;
    }
  };

  return (
    <div className="d-flex">
      {isAuthenticated && <Sidebar setCurrentPage={setCurrentPage} />}
      <div className="w-100">
        {isAuthenticated && <TopNav />}
        {renderPage()}
      </div>
    </div>
  );
}

export default App;
