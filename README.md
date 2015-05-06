# OBS Build Trigger System for GitHub Repositories
Since the OBS service support on GitHub is not yet perfect, I needed a script which looks every 5 seconds into a specific repository branch on GitHub and triggers a build request through the OBS API if the last commit hash has changed.

This script is totally different than the implementation from GitHub. GitHub sends a build request every time if you do something in your repository. (Creating/Deleting a branch etc.) This script takes care of only 1 branch and triggers a build only if you push new commits into your branch.

## Installation
Before you can use the script, you have to do some GitHub and OBS stuff.

  **Create an API Token for your OBS Project**

```
$ osc token --create [PROJECT] [PACKAGE]
```
Adjust the config.conf file and fill out the OBS part.

  **Create a service file for your OBS project**

Sorry, I can't really help you there because I'm not an OBS profi. Search in Google for "OBS Service Files _service" or something like that. You can also have a look into my setup for our docmanager project.

Docmanager OBS Project: https://build.opensuse.org/package/show/Documentation:Tools:Develop/docmanager (have a look into the _service file)

  **Create a GitHub API token**

You can create a new access token here: https://github.com/settings/tokens/new
You don't need to provide access rights to this token. You can just remove all choices.

Now you can adjust the GitHub part in your config.conf file.

Example configuraiton of the GitHub part:
```
GITHUB_API=api.github.com
GITHUB_REPO_OWNER=mschnitzer
GITHUB_REPO_NAME=obs-build-trigger
GITHUB_REPO_BRANCH=master
GITHUB_USER=mschnitzer
GITHUB_AUTH_TOKEN=b1e89d8e92c1fb6c5f4f42e5f05091ffb17ec79b
```

The auth token is the token which you created here: https://github.com/settings/tokens/new

  **Running the script**

The script is now properly (hopefully) configured. You can run the script (you need python3 btw) with ./trigger.py and the script will check every 5 seconds if there is a new commit in the given branch. If so, the script will tigger a new build request through the OBS API.

## Support
If you really need support, you can just write me an E-Mail: mschnitzer@suse.de

## Contribution
Feel free to contribute.

1. Just fork this project

2. Create a new branch

3. Make your changes

4. Make a pull request
