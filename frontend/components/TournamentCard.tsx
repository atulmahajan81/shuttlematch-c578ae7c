import React from 'react';

interface TournamentCardProps {
  name: string;
  date: string;
  location: string;
}

const TournamentCard: React.FC<TournamentCardProps> = ({ name, date, location }) => {
  return (
    <div className="border rounded-lg p-4 bg-white shadow-md">
      <h2 className="text-xl font-semibold">{name}</h2>
      <p className="text-gray-600">Date: {date}</p>
      <p className="text-gray-600">Location: {location}</p>
    </div>
  );
};

export default TournamentCard;