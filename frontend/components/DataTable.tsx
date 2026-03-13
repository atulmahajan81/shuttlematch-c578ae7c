import React from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import LoadingSpinner from './LoadingSpinner';

interface DataTableProps {
  endpoint: string;
}

const DataTable: React.FC<DataTableProps> = ({ endpoint }) => {
  const { data, error, isLoading } = useQuery(['data', endpoint], () => axios.get(endpoint).then(res => res.data));

  if (isLoading) return <LoadingSpinner />;
  if (error) return <div className="text-red-500">Error loading data</div>;
  if (!data || data.length === 0) return <div>No data available</div>;

  return (
    <table className="min-w-full bg-white">
      <thead>
        <tr>
          {Object.keys(data[0]).map((key) => (
            <th key={key} className="py-2 px-4 bg-gray-200 text-left">{key}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row: any, index: number) => (
          <tr key={index} className="border-t">
            {Object.values(row).map((value, i) => (
              <td key={i} className="py-2 px-4">{value}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default DataTable;