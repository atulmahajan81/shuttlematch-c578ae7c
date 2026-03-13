import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '@/context/AuthContext';
import { useTournaments } from '@/lib/hooks/useTournaments';

const Dashboard = () => {
  const { isAuthenticated } = useAuth();
  const router = useRouter();
  const { data: tournaments, isLoading, isError } = useTournaments();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push('/auth/login');
    }
  }, [isAuthenticated, router]);

  if (isLoading) return <div>Loading...</div>;
  if (isError) return <div>Error loading tournaments</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <ul>
        {tournaments?.map(tournament => (
          <li key={tournament.id} className="mb-2">
            <a href={`/tournaments/${tournament.id}`} className="text-blue-500">
              {tournament.name} - {tournament.location}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;