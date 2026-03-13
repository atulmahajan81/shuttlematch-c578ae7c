import React from 'react';

interface TournamentCardProps {
  title: string;
  date: string;
  location: string;
}

const TournamentCard: React.FC<TournamentCardProps> = ({ title, date, location }) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-4">
      <h2 className="text-xl font-bold mb-2">{title}</h2>
      <p className="text-gray-600">Date: {date}</p>
      <p className="text-gray-600">Location: {location}</p>
    </div>
  );
};

export default TournamentCard;