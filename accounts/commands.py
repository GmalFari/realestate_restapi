
import requests
import json
from django.core.files.storage import FileSystemStorage
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models
from .models import Image

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Make the API request.
        response = requests.get("https://bayut.p.rapidapi.com/properties/list", headers={
            "X-RapidAPI-Key": "6cb10cae22mshe83ac21e4eb1de3p1897c1jsn0b3893d5488f",
	        "X-RapidAPI-Host": "bayut.p.rapidapi.com"
        })

        # Check the status code of the response.
        if response.status_code == 200:
            # The request was successful.
            print('success')
        else:
            # The request failed.
            self.stderr.write("The request failed with status code {}.".format(response.status_code))
            return

        # Decode the response body as JSON.
        json_data = response.json()

        # Get the list of images from the JSON data.
        images = json_data["data"]

        # Create a directory to store the images.
        directory = "/mediafiles/images"

        # Create a `FileSystemStorage` object for the directory.
        storage = FileSystemStorage(directory=directory)

        # Loop through the list of images and download each image.
        for image in images:
            url = image["image"]
            filename = image["id"] + ".jpg"

            # Download the image.
            response = requests.get(url)

            # Save the image to the directory.
            with open(filename, "wb") as f:
                f.write(response.content)

        # Create a user object.
        # user = User.objects.create_user("testuser", "test@example.com", "password")

        # Create a content type object for the image model.
        content_type = ContentType.objects.get_for_model(Image)

        # Loop through the list of images and save each image to the database.
        for image in images:
            file_name = image["id"] + ".jpg"
            image_file = storage.open(file_name)
            image_obj = Image.objects.create(
                content_type=content_type,
                file=image_file,
            )

        # The images have been successfully downloaded and saved to the database.
        self.stdout.write("The images have been successfully downloaded and saved to the database.")

