## Use the oicial Python 3.9 image 
FROM python:3.9

## Ser up working DIR to /code

WORKDIR /code

## Copy the current dir contetnt in the container at /code
COPY ./requirements.txt /code/requirements.txt

## Install the requirments.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

## Set up a user named "user"
RUN useradd user

## Switch to the "user" user
USER user

## Set home to the user's home directory 
ENV HOME=/home/user\
    PATH=/home/user/.local/bin:$PATH

## set the working directory to the users home directory
WORKDIR $HOME/app

##copy the current directory content into the container at Home/app
COPY --chown=user . $HOME/app/

## Start the astAPI app on the port
CMD ["uvicorn", "app:app","--host","0.0.0.0", "--port"," 7860"]