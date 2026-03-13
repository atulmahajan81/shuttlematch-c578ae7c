import { useState } from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';

export default function RegisterPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('player');
  const [error, setError] = useState('');
  const router = useRouter();

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      await axios.post('/api/v1/auth/register', { email, password, role });
      router.push('/auth/login');
    } catch (err) {
      setError('Registration failed');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-full max-w-md">
        <h1 className="text-2xl mb-6 text-center">Register</h1>
        {error && <div className="mb-4 text-red-600">{error}</div>}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full mt-1 p-2 border rounded focus:outline-none focus:ring focus:ring-indigo-200"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full mt-1 p-2 border rounded focus:outline-none focus:ring focus:ring-indigo-200"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Role</label>
            <select
              value={role}
              onChange={(e) => setRole(e.target.value)}
              className="w-full mt-1 p-2 border rounded focus:outline-none focus:ring focus:ring-indigo-200"
            >
              <option value="player">Player</option>
              <option value="organizer">Organizer</option>
            </select>
          </div>
          <button
            type="submit"
            className="w-full bg-indigo-500 text-white py-2 rounded hover:bg-indigo-600"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
}