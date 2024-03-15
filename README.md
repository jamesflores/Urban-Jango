# Urban Jango

Urban Jango is a Django-based web application that serves as a front-end for Urban Dictionary using the api provided by [Rapid API](https://rapidapi.com/community/api/urban-dictionary).

## Installation

1. Clone the repository: `git clone https://github.com/jamesflores/Urban-Jango.git`
2. Navigate to the project directory
3. Install the requirements: `pip install -r requirements.txt`
4. Configure your environment variables (create a Rapid API account and generate your own SECRET_KEY for Django):
```
export UJ_RAPID_API_KEY=
export UJ_RAPID_API_HOST=mashape-community-urban-dictionary.p.rapidapi.com
export UJ_RAPID_API_URL=https://mashape-community-urban-dictionary.p.rapidapi.com/define
export UJ_SECRET_KEY=
```
5. Run the server: `python manage.py runserver`

## Usage

Open your web browser and navigate to `http://localhost:8000` to start exploring urban slang.
Demo: https://slang.jamesf.xyz
