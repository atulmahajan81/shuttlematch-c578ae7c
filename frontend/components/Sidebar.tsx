import React from 'react';
import { NavLink } from 'react-router-dom';

const Sidebar: React.FC = () => {
  const links = [
    { name: 'Dashboard', path: '/' },
    { name: 'Tournaments', path: '/tournaments' },
    { name: 'Players', path: '/players' },
    { name: 'Matches', path: '/matches' },
  ];

  return (
    <div className="w-64 bg-white shadow-md">
      <nav className="space-y-2 py-4">
        {links.map(link => (
          <NavLink
            key={link.name}
            to={link.path}
            className={({ isActive }) =>
              `block px-4 py-2 rounded-lg ${isActive ? 'bg-blue-500 text-white' : 'text-gray-700 hover:bg-gray-200'}`
            }
          >
            {link.name}
          </NavLink>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;