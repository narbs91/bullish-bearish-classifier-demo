# Base our app on the pytorch image so that we don't need to pull libraries through network calls
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

# Create a new user, set up a home directory, set the userid and set the name
RUN useradd -m -u 1000 user

# Change the working directory to /app
WORKDIR /app

# Copy over the requirements.txt file to the workding directory
COPY --chown=user ./requirements.txt requirements.txt

# install our dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy everything over to the working directory
COPY --chown=user . /app

# Run our script to download google/flan-t5-small to our container 
RUN python3 download_model.py

# Set a default statement if the user doesn't provide one during a run
ENV DEFAULT_STATEMENT="Lilypad is awesome"

# Tell our container how to start the app i.e. run inference.py
ENTRYPOINT ["python3", "inference.py"]

# set the STATEMENT ENV Variable to default to start
ENV STATEMENT="${DEFAULT_STATEMENT}"