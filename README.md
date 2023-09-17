# Learn French

Learn French is my streamlit project to create a language tool focused on speaking. Most language apps do not focus enough on speaking, therefore my goal is to create a solution which solves this problem.

Currently, the application consists of two pages: 
1. "Home - Why Learn French"
This page explains the benefits of learning French and displays some maps which show in which countries the language is spoken.

2. "Practice Speaking"
Currently, you can practice your vocabulary by saying the corresponding French words. You should see an image with the English word below it and then need to say the French translation of that word. If you say the word (with the corresponding article) you should see a success message. After this you can click on "Next Card" to go to the next vocabulary card and repeat the process. This is a demo to demonstrate the text2speech model. 

In the future, I would like to use the speech2text model in combination with a LLM and a text2speech model to create a sophisticated chatbot, with which you can have conversations and which corrects mistakes. 

## Table of Contents

- [Installation](#installation)
- [Data](#data)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

The required packages are listed in the requirements.txt file. Alternatively, you can use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages listed in requirements.txt

## Data
Even though my data file is very small it is not good practice to upload data to GitHub. To get access to the df_french.csv follow the link: https://hecparis-my.sharepoint.com/:x:/g/personal/thomas_schneider_hec_edu/EXHZv9VF2RhDmRLe1iHV2koBtclNcXAZaB8PPZbTdmeHPQ?e=odq9zN
The access expires Friday, September 22nd 2023, but can be prolonged if need be. Make sure to download the .csv file before running the docker. 

## Usage

### Running the Application with Docker

This project can be easily run using Docker, a platform that simplifies application deployment by encapsulating it in containers. If you're not familiar with Docker, here's a brief guide to get you started:

#### 1. Install Docker

If you don't already have Docker installed on your system, you can download and install it from the official Docker website: [Docker Installation](https://docs.docker.com/get-docker/).

#### 2. Build the Docker Image

After installing Docker, navigate to the project's root directory in your terminal. You should see a `Dockerfile` in this directory. The `Dockerfile` contains instructions for building a Docker image of your application.

To build the Docker image, use the following command:

```bash
docker build -t streamlit_v11 .
```

- docker build is the command to build a Docker image.

- -t streamlit_v11 assigns a tag (or name) to the image. You can use any name you prefer.


### 3. Run the Docker Container
Once the image is built, you can run it as a Docker container using the following command:

```bash
docker run -p 8501:8501 streamlit_v11
```

- docker run starts a new container instance from the specified image.

- -p 8501:8501 maps port 8501 inside the container to port 8501 on your local machine. This is the default port that Streamlit applications use.

### 4. Access the Application

With the Docker container running, open your web browser and navigate to http://localhost:8501. You should see your "Learn French" application up and running.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
