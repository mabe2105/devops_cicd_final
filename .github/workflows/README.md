# Workflows

## DEV - Build and Unittest

File: [dev_build.yml](dev_build.yml)

Event: On **push** → any branch except **main**

Jobs:
* Build
* Unit Test with single version of Python → For faster testing results

Description:
This workflow will run for every commit on any branch except the **main** branch. It will build and then test the app with a single version of python.

## STAGE - CI/CD Pipeline

File: [stage_pipeline.yml](stage_pipeline.yml)

Event: On **Pull Request** → any branch into **main**

Jobs:
* Build
* Unit Test with matrix
* Deploy (?)

### Description:
This workflow will trigger for any pull request into **main**. It will build and then test the app with a test matrix. The results of this workflow are visible in the pull request. 