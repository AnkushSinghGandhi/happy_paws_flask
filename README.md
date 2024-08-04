<a href="https://warriorwhocodes.com"><img src="repo_images/header.jpg"></a>

<p align="center">
  <a href="https://ankushsinghgandhi.github.io">
    <img src="https://img.shields.io/badge/Website-3b5998?style=flat-square&logo=google-chrome&logoColor=white" />
  </a>
  <a href="http://twitter.com/ankushsgandhi">
    <img src="https://img.shields.io/badge/-Twitter-blue?style=flat-square&logo=twitter&logoColor=white" />
  </a>
   <a href="https://www.linkedin.com/in/ankush-singh-gandhi-2487771aa/">
    <img src="https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white" />
  </a>
  <a href="https://dev.to/@ankushsinghgandhi">
    <img src="https://img.shields.io/badge/-Dev.to-grey?style=flat-square&logo=dev.to&logoColor=white"/>
  </a>
  <a href="https://stackoverflow.com/users/13790266/ankush-singh">
    <img src="https://img.shields.io/badge/-Stackoverflow-orange?style=flat-square&logo=stackoverflow&logoColor=white"/>
  </a>
  <a href="https://leetcode.com/ankushsinghgandhi/">
    <img src="https://img.shields.io/badge/-Leetcode-yellow?style=flat-square&logo=Leetcode&logoColor=white"/>
  </a>
    <a href="https://www.hackerrank.com/ankushsgandhi">
    <img src="https://img.shields.io/badge/-HackerRank-green?style=flat-square&logo=Hackerrank&logoColor=white"/>
  </a>
    <a href="https://www.hackerearth.com/@bhanusinghank">
    <img src="https://img.shields.io/badge/-Hackerearth-purple?style=flat-square&logo=Hackerearth&logoColor=white"/>
  </a>
</p>


# Happy Paws Backend

This repository contains the backend code for the Happy Paws app, developed using Flask. The Happy Paws app is designed to provide a comprehensive platform for pet owners, local NGOs, pet hospitals, and the community. The backend supports various features and functionalities to ensure a seamless user experience.

## Features

1. **User Authentication and Authorization**
   - Secure login and signup processes for users and admins.
   - Admin-specific login template to restrict access to administrative functionalities.

2. **Feeds**
   - Real-time feeds for users to stay updated with the latest news and updates related to pets.

3. **Dog Registration**
   - Easy registration process for users to register their pets.
   - Maintain and manage pet profiles with essential details.

4. **Local NGOs and Pet Hospitals**
   - Integration with local NGOs and pet hospitals to provide users with essential services.
   - Information and contact details of nearby NGOs and hospitals.

5. **Lost Pets and Reporting**
   - Feature to report lost pets and help in finding them.
   - Users can report lost pets and view reported pets in their area.

6. **Rewards System (Paws Wallet)**
   - Implemented a rewards system to encourage user engagement.
   - Users can earn and redeem points through the Paws Wallet.

## Technologies Used

- **Flask**: The main framework for backend development.
- **SQLAlchemy**: For database management and ORM.
- **JWT**: For secure authentication.
- **Celery**: For handling asynchronous tasks.
- **Docker**: To containerize the application for ease of deployment.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Docker (for containerization)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ankushsinghgandhi/happy_paws_flask.git
   cd happy-paws-backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

### Docker

To run the application using Docker:

1. Build the Docker image:
   ```bash
   docker build -t happy_paws_flask .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 happy_paws_flask
   ```

## Contributing

We welcome contributions to the Happy Paws backend. Please fork the repository and submit pull requests for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
