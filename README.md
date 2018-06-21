## SANBI/UWC Mozilla Science Study Group workspace

This repository contains work done as part of the [SANBI UWC Mozilla Science Study Group](https://sanbi-sa.github.io/studyGroup/). In general each session gets a directory.

As mentioned below we have got some support for automated testing. Test status: [![Build Status](https://travis-ci.org/SANBI-SA/studyGroupWork.svg?branch=master)](https://travis-ci.org/SANBI-SA/studyGroupWork)


### Support for testing of Python scripts

If a session has a directory in it called `test/`, then tests will be run using [Travis CI](https://travis-ci.org/) each time that the a commit is pushed to the repository. If the script has any module requirements (besides the standard Python modules and `pytest`) they should be listed in a file called `requirements.txt`, which is in `conda` format, i.e. it can be created using `conda list --export`.

#### TODO for testing

Right now all tests are run. A filter should be used to ensure that only directories where new
commits have been added should be tested.