-- Seed data for users
INSERT INTO users (id, email, password_hash, role, created_at, updated_at) VALUES
  (gen_random_uuid(), 'admin@example.com', 'hashed_password', 'admin', NOW() - INTERVAL '10 days', NOW() - INTERVAL '5 days'),
  (gen_random_uuid(), 'user1@example.com', 'hashed_password', 'user', NOW() - INTERVAL '20 days', NOW() - INTERVAL '15 days'),
  (gen_random_uuid(), 'user2@example.com', 'hashed_password', 'user', NOW() - INTERVAL '30 days', NOW() - INTERVAL '25 days');

-- Seed data for tournaments
INSERT INTO tournaments (id, name, location, date, created_at, updated_at) VALUES
  (gen_random_uuid(), 'Summer Open', 'New York', CURRENT_DATE - INTERVAL '5 days', NOW() - INTERVAL '10 days', NOW() - INTERVAL '5 days'),
  (gen_random_uuid(), 'Winter Cup', 'Los Angeles', CURRENT_DATE - INTERVAL '15 days', NOW() - INTERVAL '20 days', NOW() - INTERVAL '15 days');