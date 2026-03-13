import React from 'react';

const Navbar: React.FC = () => {
  return (
    <div className="bg-white shadow-md h-16 flex items-center justify-between px-6">
      <div className="text-xl font-semibold">ShuttleMatch</div>
      <div className="flex items-center space-x-4">
        <div className="relative">
          <span className="text-gray-500">User</span>
        </div>
      </div>
    </div>
  );
};

export default Navbar;