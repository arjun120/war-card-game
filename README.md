<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#testing">Testing</a></li>
      </ul>
    </li>
    <li><a href="#potential-improvements">Potential Improvements</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Screen Shot][product-1]
![Product Screen Shot][product-2]

War is a card game with it's simplest version played between two players. The rules for this implementation can be found [here](https://bicyclecards.com/how-to-play/war/). You can read up more about the game [here](https://en.wikipedia.org/wiki/War_(card_game)).




### Built With

The major frameworks/libraries used in this project are as listed below:

* [![Flask][Flask-framework]][Flask-url]
* [![React][React.js]][React-url]
* [![MySQL][MySQL-DB]][MySQL-url]




<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
The backend flask server and mysql server are dockerized to run in two containers. Prior to setting up and running the backend and mysql server, make sure you have [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) installed and setup. The installation guide for the docker engine can be found [here](https://docs.docker.com/engine/install/). For docker-compose, you can visit [this](https://docs.docker.com/compose/install/) page. Follow the instructions on these pages carefully and verify the installation and the version at the end.

For the frontend, make sure Node and NPM are installed on your computer. You can download both at [this](nodejs.org) link (NPM is included in your Node installation).

### Installation

Once you have verified docker-compose and npm are installed and working correctly, you may first proceed to build and run the backend and database services.


1. Clone the repo
   ```sh
   git clone https://github.com/arjun120/war-card-game.git
   ```
2. ```sh
   cd war
   ```
3. Here, you can use `docker-compose` to build the images and start the containers for the backend and SQL db. 
   ```sh
   docker-compose up -d
   ```
4. The endpoint to your backend Flask server is exposed on port `4000`.
5. Now that your backend and db services are up and running, you can run the frontend React server. 
6. ```sh
   cd war-ui
   ```
7. Now, install NPM packages using
   ```sh
   npm install
   ```
8. Now, if your backend is running on `127.0.0.1` that is `localhost` if you ran your containers locally, you can start the react server using the following command:
    ```sh
   REACT_APP_BACKEND_IP=127.0.0.1 npm start
   ```
   Replace the `127.0.0.1` with the DNS of the container depending on where your backend service is running. 
9. Now, you have successfully installed and run the war game. You should be able to access the game at [http://localhost:3000/](http://localhost:3000/).

### Testing

The project is packaged with simple unit tests designed to test the sanity and functionality of the backend endpoints. Use the following instructions to run these tests (NOTE: If you are running these locally, you need to install the requirements locally outside of your container running the backend.):

1. If you need to install the requirements, you can run the following:
   ```sh
   pip install requirements.txt
   ```
2. Navigate to the directory containing the files for the backend.
   ```sh
   cd war/war-backend
   ```
3. Finally, run the tests using `pytest` as follows:
   ```sh
   pytest war-tests.py
   ```

<!-- CONTACT -->
## Contact

Arjun Manjunatha Rao | [LinkedIn](https://www.linkedin.com/in/arjun-manjunatha-rao-774817179/) | [email](arjunman@andrew.cmu.edu)

Project Link: [https://github.com/arjun120/war-card-game](https://github.com/arjun120/war-card-game)

<!-- POTENTIAL IMPROVEMENTS -->
## Potential Improvements / Alternative Design Choices
1. The backend for this project currently simulates the game between two players. This could be extended to accommodate more players by adapting to a different version of the game. Currently a variation of the regular version is implemented to handle and avoid infinite sessions of the game. The current fix includes declaring the game as a draw in case the number of cards in each players deck toggles between two fixed values for a threshold number of rounds. While this variation is a reasonable fix, alternate versions could be explored.
2. The backend and db for this game have been dockerized and packaged as a unit which can be brought up and down easily. The UI is a separate service, which runs independently. While this decoupling was a design choice, the three services could be dockerized and brought up finally exposing only the UI to the users. These services could also be deployed and orchestrated using tools such as Kubernetes on a cloud platform.
3. Finally, the UI could be improved to show the cards in play dynamically. However, observing the number of rounds these games typically last for, this may not be viable. Other improvements such as beautification of the UI could be potential directions to explore.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-1]: images/war-ui1.png
[product-2]: images/war-ui2.png
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Flask-framework]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[MySQL-DB]: https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://www.mysql.com/


