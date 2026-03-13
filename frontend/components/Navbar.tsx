import React from 'react';

const Navbar: React.FC = () => {
  return (
    <nav className="bg-white shadow-md flex items-center justify-between px-6 py-4">
      <div className="text-lg font-semibold">ShuttleMatch Dashboard</div>
      <div className="flex items-center">
        <div className="text-gray-600 mr-4">Welcome, User!</div>
        <button className="bg-blue-500 text-white px-4 py-2 rounded-md">Logout</button>
      </div>
    </nav>
  );
};

export default Navbar;