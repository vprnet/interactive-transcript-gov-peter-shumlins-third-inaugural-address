# VPR Timeline: A Year Of 'Systemic Failure' At DCF

A page built using the [app-template](https://github.com/vprnet/app-template).

## Set Up

1. Install [virtualenv](https://pypi.python.org/pypi/virtualenv)
2. Clone the repository

        $ git clone git@github.com:vprnet/timeline-dcf-systemic-failure.git

3. Create Virtual Environment in project

        $ cd timeline-dcf-systemic-failure
        $ virtualenv venv

4. Enter virtual environment

        $ source venv/bin/activate

5. Install requirements

        $ pip install -r requirements.txt

6. Copy `_config.py` as `config.py`

        $ cp main/_config.py main/config.py

  These settings can be configured later (see "Deploy" below)

7. Install grunt modules ([read this](http://24ways.org/2013/grunt-is-not-weird-and-hard/) if getting started with Grunt)

        $ cd main/static
        $ npm install

##Develop

To get grunt running in the background:

        $ cd main/static
        $ grunt

To run local server, get back to project root and run:

        $ python runserver.py

The project will be viewable at http://127.0.0.1:5000/

## Deploy

1. In config, set the `AWS_DIRECTORY` to either `sandbox/timeline-dcf-systemic-failure/` or `apps/timeline-dcf-systemic-failure/`

2. Configure AWS settings in `config.py`

4. Freeze files and push to S3

        $ python runserver.py freeze

## Author
[Matt Parrilla](http://twitter.com/mattparrilla)

##Copyright and License

Copyright 2013 Vermont Public Radio

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License.
You may obtain a copy of the License in the LICENSE file, or at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language
governing permissions under the License.

