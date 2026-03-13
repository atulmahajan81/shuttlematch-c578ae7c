import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../lib/context/auth';

export default function HomePage() {
  const { isAuthenticated } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push('/auth/login');
    }
  }, [isAuthenticated, router]);

  return (
    <div className="max-w-7xl mx-auto p-4">
      <h1 className="text-3xl font-bold">Welcome to ShuttleMatch Dashboard</h1>
      <p className="mt-4">Your hub for managing tournaments and matches.</p>
    </div>
  );
}