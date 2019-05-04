# SubScript
## A Python based SSA Subtitle translator
> Powered by Google Translate

## 1. About

SubScript is an easy to use console applicaton that can take SSA/ASS files and translate the text to a language of your choosing. It uses the Google Cloud platform to provide fast and cost-effective translations. SubScript has built in Menus and file dialogs, making it easy to use.

> This uses the Google Translate API `v3beta1` which has a 500,000 character/month free tier

## 2. I want to use it! How do I get started?

Firstly, you will need a credit/debit card, as this requires the use of the Google Cloud Paid Services (although a free trial works!). You will also need a Python environment with the requirements.txt file depenedencies met if you are cloning this repo.

You will need to sign up to [Google Cloud](https://cloud.google.com/free/) (which will get you some pretty cool stuff as well as some credit for a year to use)

After signing up, create a project and give it a memorable name, like `SubScript Container`
It will take a minute, then you can switch to it and enable the API.

### Enable the API

To enable the API, go to the menu (3 lines in the top left hand corner) and select APIs & Services. Click on `Enable APIs` and in the search box that appears, type `translate` and press enter. Select the Google Translate API and click `Enable`.

### Get the Service Account

To get the `.json` file used to access the API, hover over the left hand context menu and select `Credentials` from it. Click Create Credential and select `Service Account`. Create a new Service Account with the name `SubScript-App` and the role as `Cloud Translation API User`. Click create whilst leaving the format as `JSON`. A file should download to your computer, do not delete this or edit it's contents. Changing the filename is fine though.

### Use the app

Launch the app, it will give you multiple options, you will need to select option `1` and select the JSON file that was downloaded, then `2` if you want another output langauge. Finally `3` will translate the file. Whilst it's slow it does stop you from being ratelimited by Google, which will give you a soft ban.