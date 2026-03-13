import { useRouter } from 'next/router';
import { useEffect } from 'react';
import { useAuth } from '../../lib/context/auth';
import { useTournament } from '../../lib/hooks/useTournaments';

export default function TournamentDetailPage() {
  const { isAuthenticated } = useAuth();
  const router = useRouter();
  const { id } = router.query;
  const { data, isLoading, error } = useTournament(id as string);

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push('/auth/login');
    }
  }, [isAuthenticated, router]);

  if (isLoading) return <div>Loading tournament details...</div>;
  if (error) return <div>Error loading tournament: {error.message}</div>;

  return (
    <div className="max-w-7xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">{data?.name}</h1>
      <p>Location: {data?.location}</p>
      <p>Date: {data?.date}</p>
      <h2 className="text-2xl mt-6 mb-2">Matches</h2>
      {data?.matches.length === 0 ? (
        <p>No matches available.</p>
      ) : (
        <ul className="space-y-4">
          {data?.matches.map(match => (
            <li key={match.id} className="bg-white p-4 rounded shadow">
              <p>Match ID: {match.id}</p>
              <p>Player 1: {match.player1_id}</p>
              <p>Player 2: {match.player2_id}</p>
              <p>Scheduled Time: {match.scheduled_time}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}