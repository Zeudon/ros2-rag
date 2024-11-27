# ros2-rag
A RAG System for ROS2 Robotics using Pytorch, TF, Keras, MongoDB, Qdrant and ClearML

# Setup
Create a file called localsecrets.yml in the app folder. Paste the content below and replace with the api key generated from google developer console:  
api_keys:    
&nbsp;&nbsp;youtube: your_api_key    

To run the docker containers, install docker-compose.
Execute "docker-compose build", and then "docker-compose up" in the main ros2-rag directory. To check the list of containers running, use "docker ps"
