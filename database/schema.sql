-- Create pgcrypto extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Create trigger function for updating 'updated_at' timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

-- Table: users
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'user')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
COMMENT ON TABLE users IS 'Represents a user in the system';

-- Table: tournaments
CREATE TABLE tournaments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT unique_name_date UNIQUE (name, date)
);
COMMENT ON TABLE tournaments IS 'Represents a badminton tournament';
CREATE INDEX ON tournaments (name);
CREATE INDEX ON tournaments (date);

-- Table: matches
CREATE TABLE matches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tournament_id UUID NOT NULL REFERENCES tournaments(id) ON DELETE CASCADE,
    player1_id UUID NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    player2_id UUID NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    scheduled_time TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
COMMENT ON TABLE matches IS 'Represents a match in a tournament';
CREATE INDEX ON matches (tournament_id);
CREATE INDEX ON matches (scheduled_time);

-- Table: scores
CREATE TABLE scores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    match_id UUID NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
    player1_score INTEGER NOT NULL CHECK (player1_score >= 0),
    player2_score INTEGER NOT NULL CHECK (player2_score >= 0),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
COMMENT ON TABLE scores IS 'Represents scores for a match';
CREATE INDEX ON scores (match_id);

-- Create trigger to update 'updated_at' column
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_tournaments_updated_at BEFORE UPDATE ON tournaments FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_matches_updated_at BEFORE UPDATE ON matches FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_scores_updated_at BEFORE UPDATE ON scores FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();