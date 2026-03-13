import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

export const useTournaments = () => {
  return useQuery('tournaments', async () => {
    const { data } = await axios.get('/api/v1/tournaments');
    return data;
  });
};

export const useTournament = (id: string) => {
  return useQuery(['tournament', id], async () => {
    const { data } = await axios.get(`/api/v1/tournaments/${id}`);
    return data;
  }, {
    enabled: !!id
  });
};