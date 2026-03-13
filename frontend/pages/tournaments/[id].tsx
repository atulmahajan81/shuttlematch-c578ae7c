import { useRouter } from 'next/router';
import { useEffect } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTournament } from '@/lib/hooks/useTournaments';

const TournamentDetail = () => {
  const router = useRouter();
  const { id } = router.query;
  const { isAuthenticated } = useAuth();
  const { data: tournament, isLoading, isError } = useTournament(id as string);

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push('/auth/login');
    }
  }, [isAuthenticated, router]);

  if (isLoading) return <div>Loading...</div>;
  if (isError) return <div>Error loading tournament</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">{tournament?.name}</h1>
      <p>Location: {tournament?.location}</p>
      <p>Date: {tournament?.date}</p>
    </div>
  );
};

export default TournamentDetail;