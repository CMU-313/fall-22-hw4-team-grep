# HW4 Starter Code and Instructions

Please consult the [homework assignment](https://cmu-313.github.io//assignments/hw4) for additional context and instructions for this code.

## Feature: Student Quality Prediction
In order to assist the CMU decisions committee in filtering applicants, we have created a microservice that predicts the quality of the student (defined as G3 grade >15) with a random forest clasifier on 5 features. These features include weekly hours studied, number of absences, number of failures, and their G1 and G2 grades. 

We chose our features based on results of data analysis against G3 scores. Of the 5 features, studytime, G1, and G2 scores are directly correlated to high G3 scores. Failures are inversely correlated with G3 scores. Lastly, students with >15 absences are very unlikely to get high G3 scores. On 394 samples, our model achieved an accuracy of 96.8%. This is a >40% improvement over the older model.  

When a GET request is made to the `/predict/` endpoint with the necessary fields listed above, the microservice responds with a 200 response and a binary value AdmissionStatus. If the parameters are invalid, a 404 error is thrown.

## Reasoning for the features
As mentioned above, the features were chosen based on strong correlations to G3 scores. This section will present a more detailed analysis with graphs generated via pandas. First, it comes as no surprise that G1 and G2 scores are both directly correlated with a higher G3 score, as seen in the following two scatterplots.The only exception are several outlier students who have a 0 as their G3 grade, presumably because they failed to finish the school year.

Next, we analyzed the effects of failures and time spent studying (recorded as studytime) on a student’s performance. Due to the quantified nature of these two attributes, we used bar plots of the median G3 score for comparison. It is clear that the number of failures is inversely correlated to the student’s G3 score. Increasing the study time is more nuanced: from 1 to 3 hours a week, the student’s score is increased, but beyond 3 hours, there is no significant difference in a student’s grade. This hints that if a student is spending a lot of time on a class, they are not necessarily more successful but could be instead struggling in that subject.

Moving on, we also sought to compare the number of absences to the G3 score. Here we found no immediate strong correlation. However, it seems that most students who achieve a G3 grade have no more than 15 absences over the school year. Thus despite the correlation being fairly weak, we still chose to include it in our model.

Finally, we analyzed various other fields that showed little to no correlation, such as the parent’s education level, as demonstrated below.



## pipenv

[pipenv](https://pipenv.pypa.io/en/latest) is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and the good old requirements.txt.

### Installation

#### Prereqs

- The version of Python you and your team will be using (version greater than 3.8)
- pip package manager is updated to latest version
- For additional resources, check out [this link](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

#### Mac OS

To install pipenv from the command line, execute the following:

```terminal
sudo -H pip install -U pipenv
```

#### Windows OS

The same instructions for Mac OS **should** work for windows, but if it doesn't, follow the instructions [here](https://www.pythontutorial.net/python-basics/install-pipenv-windows).

### Usage

#### Downloading Packages

The repository contains `Pipfile` that declares which packages are necessary to run the `model_build.ipnyb`.
To install packages declared by the Pipfile, run `pipenv install` in the command line from the root directory.

You might want to use additional packages throughout the assignment.
To do so, run `pipenv install [PACKAGE_NAME]`, as you would install python packages using pip.
This should also update `Pipfile` and add the downloaded package under `[packages]`.
Note that `Pipfile.lock` will also be updated with the specific versions of the dependencies that were installed.
Any changes to `Pipfile.lock` should also be committed to your Git repository to ensure that all of your team is using the same dependency versions.

#### Virtual Environment

Working in teams can be a hassle since different team members might be using different versions of Python.
To avoid this issue, you can create a python virtual environment, so you and your team will be working with the same version of Python and PyPi packages.
Run `pipenv shell` in your command line to activate this project's virtual environment.
If you have more than one version of Python installed on your machine, you can use pipenv's `--python` option to specify which version of Python should be used to create the virtual environment.
If you want to learn more about virtual environments, read [this article](https://docs.python-guide.org/dev/virtualenvs/#using-installed-packages).
You can also specify which version of python you and your team should use under the `[requires]` section in `Pipfile`.

## Jupyter Notebook

You should run your notebook in the virtual environment from pipenv.
To do, you should run the following command from the root of your repository:

```terminal
pipenv run jupyter notebook
```

## API Endpoints

You should also use pipenv to run your Flask API server.
To do so, execute the following commands from the `app` directory in the pip venv shell.


Set an environment variable for FLASK_APP.
For Mac and Linux:
```terminal
export FLASK_APP=app.py
```

For Windows:
```terminal
set FLASK_APP=app
```

To run:
```terminal
pipenv run flask run
```

Or if you're in the pipenv shell, run:
```terminal
flask run
```

You can alter the port number that is used by the Flask server by changing the following line in `app/app.py`:

```python
app.run(host="0.0.0.0", debug=True, port=80)
```

## Testing

To run tests, execute the following command from the `app` directory:

```terminal
pytest
```

If you're not in the Pipenv shell, then execute the following command from the `app` directory:

```terminal
pipenv run pytest
```
