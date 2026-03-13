import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../../lib/context/auth';
import { useTournaments } from '../../lib/hooks/useTournaments';

export default function TournamentsPage() {
  const { isAuthenticated } = useAuth();
  const router = useRouter();
  const { data, isLoading, error } = useTournaments();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push('/auth/login');
    }
  }, [isAuthenticated, router]);

  if (isLoading) return <div>Loading tournaments...</div>;
  if (error) return <div>Error loading tournaments: {error.message}</div>;

  return (
    <div className="max-w-7xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Tournaments</h1>
      {data?.length === 0 ? (
        <p>No tournaments available.</p>
      ) : (
        <ul className="space-y-4">
          {data.map(tournament => (
            <li key={tournament.id} className="bg-white p-4 rounded shadow">
              <h2 className="text-xl font-semibold">{tournament.name}</h2>
              <p>Location: {tournament.location}</p>
              <p>Date: {tournament.date}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}