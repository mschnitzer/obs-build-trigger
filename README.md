# OBS Build Trigger System for GitHub Repositories
Since the OBS service support on GitHub is not yet perfect, I needed a script which looks every 5 seconds into a specific repository branch on GitHub and triggers a build request through the OBS API if the last commit hash has changed.

This script is totally different than the implementation from GitHub. GitHub sends a build request every time if you do something in your repository. (Creating/Deleting a branch etc.) This script takes care of only 1 branch and triggers a build only if you push new commits into your branch.
