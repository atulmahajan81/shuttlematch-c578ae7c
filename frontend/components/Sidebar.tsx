import React from 'react';
import { useRouter } from 'next/router';

const Sidebar: React.FC = () => {
  const router = useRouter();
  const menuItems = [
    { name: 'Dashboard', path: '/' },
    { name: 'Tournaments', path: '/tournaments' },
    { name: 'Players', path: '/players' },
    { name: 'Matches', path: '/matches' },
    { name: 'Scores', path: '/scores' },
  ];

  return (
    <div className="w-64 bg-blue-800 text-white flex-none">
      <div className="p-6 text-xl font-bold">ShuttleMatch</div>
      <ul className="space-y-2">
        {menuItems.map((item) => (
          <li
            key={item.name}
            className={`px-4 py-2 hover:bg-blue-700 cursor-pointer ${router.pathname === item.path && 'bg-blue-900'}`}
            onClick={() => router.push(item.path)}
          >
            {item.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;