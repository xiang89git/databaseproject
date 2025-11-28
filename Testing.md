# Step 1: 
# Using this script, we start MongoDB Docker: 

cd DATABASEPROJECT
docker-compose up -d

# Step 2: 
# Starting the Flask API using sever run "http://localhost:5000":

python app.py 

# Step 3:
# API Authentication by using a simple token system to return the user_id after logging in:

UserID: <user_id>

# Step 4:
# Full Endpoint Workflow with some examples such as Creating a user, logging in, etc.

# Creating user
POST /api/register

{
  "first_name": "Alice",
  "last_name": "Smith",
  "email": "alice@example.com",
  "password": "password123",
  "subscription_id": "<your_plan_id>"
}

# Login 
POST /api/login

{
  "email": "alice@example.com",
  "password": "password123"
}
# What it returns:
{
  "user_id": "...",
  "token": "..."
}

# Using tokens.
UserID: <token>

# Step 5:
# Admin API Workflow with some examples like creating subscription plans, adding content, etc.

# Creating subscription plans for users.
POST /api/admin/subscription_plans

{
  "plan_name": "Premium",
  "monthly_price": 19.99,
  "max_profiles": 5
}

# Addding content such as a movie.
POST /api/admin/content

{
  "title": "Inception",
  "description": "Mind-bending sci-fi",
  "type": "Movie",
  "genres": ["<genre_id>"]
}

# And lastly, add media file.
POST /api/admin/content/<content_id>/media_files

{
  "file_path": "/movies/inception-1080p.mp4",
  "resolution": "1080p",
  "language": "English",
  "file_size": 2048
}
