-- Insert users
INSERT INTO users (email, password_hash, role, created_at, updated_at) VALUES
('admin@example.com', 'hashed_password1', 'admin', NOW() - INTERVAL '10 days', NOW() - INTERVAL '10 days'),
('user1@example.com', 'hashed_password2', 'user', NOW() - INTERVAL '9 days', NOW() - INTERVAL '9 days'),
('user2@example.com', 'hashed_password3', 'user', NOW() - INTERVAL '8 days', NOW() - INTERVAL '8 days');

-- Insert tournaments
INSERT INTO tournaments (name, location, date, created_at, updated_at) VALUES
('Spring Open', 'Sports Complex', '2023-11-01', NOW() - INTERVAL '7 days', NOW() - INTERVAL '7 days'),
('Summer Classic', 'City Arena', '2023-11-15', NOW() - INTERVAL '6 days', NOW() - INTERVAL '6 days');

-- Insert matches
INSERT INTO matches (tournament_id, player1_id, player2_id, scheduled_time, created_at, updated_at) VALUES
((SELECT id FROM tournaments WHERE name = 'Spring Open'), (SELECT id FROM users WHERE email = 'user1@example.com'), (SELECT id FROM users WHERE email = 'user2@example.com'), '2023-11-01 10:00:00', NOW() - INTERVAL '5 days', NOW() - INTERVAL '5 days'),
((SELECT id FROM tournaments WHERE name = 'Summer Classic'), (SELECT id FROM users WHERE email = 'user1@example.com'), (SELECT id FROM users WHERE email = 'user2@example.com'), '2023-11-15 12:00:00', NOW() - INTERVAL '4 days', NOW() - INTERVAL '4 days');

-- Insert scores
INSERT INTO scores (match_id, player1_score, player2_score, created_at, updated_at) VALUES
((SELECT id FROM matches WHERE scheduled_time = '2023-11-01 10:00:00'), 21, 15, NOW() - INTERVAL '3 days', NOW() - INTERVAL '3 days'),
((SELECT id FROM matches WHERE scheduled_time = '2023-11-15 12:00:00'), 18, 21, NOW() - INTERVAL '2 days', NOW() - INTERVAL '2 days');