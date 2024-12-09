# ros2-rag
A RAG System for ROS2 Robotics using Pytorch, TF, Keras, MongoDB, Qdrant and ClearML. We use docker containers for the environment setup, with different containers for MongoDB server, QDrant, ClearML and the App. The first step is the ETL Pipeline, where we scrape data from Youtube videos, GitHub repositories and Documentation Web pages. The scraped data is then stored in a MongoDB collection. The next step is Featurization. In this step, we first retrieve the scraped data from the MongoDB collection, clean the text, create embeddings using sentence transformers and store it in a different MongoDB collection. We then retrieve data from this collection and store the embeddings into QDrant Vector Database as well, with the data being the payload. For Inferencing, we first retrieve the query, create an embedding out of it and find top K similar documents using QDrant's Cosine similarity. We pass the original query along with the retrieved documents as context to the LLM which then gives us the output. We have also created a Gradio application, as the user interface. Answers are generated and displayed upon choosing the question from the dropdown.

## Milestones and Screenshots

### Environment and Tooling Milestone
Attaching below the screenshot of the docker containers, There is 1 container each for MongoDB, QDrant and the App. The remaining containers are for clearML, for fileserver, API server and web host.
![Docker Screenshot](Docker_Screenshot.png "This is the Docker Screenshot")
