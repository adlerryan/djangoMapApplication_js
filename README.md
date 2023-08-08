# Map Application with Django and Google Maps API
This is a Django project for a Map Application that utilizes the Google Maps API to display locations on a map and allows users to view location details in a modal. The project includes front-end code written in HTML, CSS, and JavaScript, as well as a Django backend for managing location data.

# Update
- Stopped development on this because I wanted to start using the same setup but have a front end that uses React.js. Please see other projects.
## Front-end
The front-end of the application is built using HTML, CSS, and JavaScript. Here are the key components:

**index.html:** The main HTML file that renders the map, navigation bar, menu, and modal for displaying location details.

**styles.css:** The CSS file that styles the navigation bar, menu, map container, and the modal.

**modal.css:** The CSS file that styles the modal for displaying location details.

**JavaScript:** The JavaScript code handles map initialization, marker creation, and the modal functionality. It interacts with the Django backend to fetch location data and populate the map markers and the location modal with relevant information.

## Backend
The backend for this Django project is managed through the **models.py** file. It includes a model for locations with fields like **lat, lng, name, rating, address, and images**. These fields are used to represent location data, and the backend provides this data to the front-end through API endpoints.

The **views.py** file contains the necessary views to handle requests for location data. In this example, we have a view called get_locations, which retrieves all locations from the database, serializes them into JSON format, and returns them as the API response.

## Instructions to Run
To run this project, follow these steps:

1. Clone the repository to your local machine.

2. Make sure you have Python and Django installed.

3. Obtain a new API key from Google Maps by creating a project in the Google Cloud Console and enabling the Maps JavaScript API.

4. Replace the existing Google Maps API key (AIzaSyC-JoFtnudmVWsWiYHuDoY5B_GFyqDO3uQ) in index.html with your new API key. This won't work.

5. Set up the Django backend by defining the models and views to provide location data for the front-end.

6. Start the Django development server to run the project. **python manage.py runserver**
