import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

interface Tournament {
  id: string;
  name: string;
  location: string;
  date: string;
  matches: Array<{ id: string; player1_id: string; player2_id: string; scheduled_time: string; }>;
}

const fetchTournaments = async (): Promise<Tournament[]> => {
  const { data } = await axios.get('/api/v1/tournaments');
  return data;
};

const fetchTournamentById = async (id: string): Promise<Tournament> => {
  const { data } = await axios.get(`/api/v1/tournaments/${id}`);
  return data;
};

export const useTournaments = () => {
  return useQuery(['tournaments'], fetchTournaments);
};

export const useTournament = (id: string) => {
  return useQuery(['tournament', id], () => fetchTournamentById(id), {
    enabled: !!id
  });
};