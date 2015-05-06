# OBS Build Trigger System for GitHub Repositories
Since the OBS service support on GitHub is not yet perfect, I needed a script which looks every 5 seconds into a specific repository on GitHub and triggers a build request through the OBS API if the last commit hash has changed.

