# Development Guide

## Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/shuttlematch.git
   cd shuttlematch
   ```

2. **Install dependencies**:
   - Backend: Navigate to the `backend` directory and install Python dependencies:
     ```bash
     cd backend
     pip install -r requirements.txt
     ```
   - Frontend: Navigate to the `frontend` directory and install Node.js dependencies:
     ```bash
     cd ../frontend
     npm install
     ```

3. **Environment Variables**:
   - Copy the `.env.example` to `.env` and update the values as needed.

4. **Run the application**:
   - Start the backend:
     ```bash
     uvicorn main:app --reload
     ```
   - Start the frontend:
     ```bash
     npm run dev
     ```

## Running Tests

- **Backend Tests**:
  ```bash
  pytest
  ```

- **Frontend Tests**:
  ```bash
  npm run test
  ```

## Code Structure

- **Backend**:
  - `main.py`: Entry point of the FastAPI application.
  - `app/`: Contains all business logic and API endpoints.

- **Frontend**:
  - `pages/`: Next.js pages and components.
  - `components/`: Reusable UI components.

## Contributing Guide

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork and submit a pull request.