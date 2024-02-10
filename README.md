# dice-game-win-probability

This FastAPI project calculates and delivers the probabilities of Bob winning a turn-based dice game against Alice. The competition involves alternately rolling a fair k-sided die, where the first player to roll a value equal to k wins. The API is designed to assess these probabilities for `k`-sided dice, ranging from `6` to `99`, considering Alice always gets the initial roll.

The API is versatile, allowing users to specify the `k` parameter through an optional header `K`. When this header is included, the endpoint responds with the probability for the specified `k`. If the header is omitted, the endpoint defaults to returning a comprehensive list of probabilities for the entire range of `6` to `99`.

## Requirements

* Brew
* Python 3.10
* Go-Task

### Install Brew

Please visit official Homebrew [site](https://brew.sh/) for detailed guide to install Brew.

### Install Python

Use Brew to install the specific version of Python required for this project:

```shell
brew install python@3.10
```

### Install Go-Task

Go-Task is used for task automation within the project. Install it using Brew:

```shell
brew install go-task
```

## Development 

Follow these steps to set up your development environment:

### Install project and dev dependencies

This command installs all necessary dependencies for both development and the project itself:

```shell
task install-dependencies
```

### Run linter

Ensure code quality and consistency by running the linter:

```shell
task lint
```

### Run project tests

Execute the project's test suite to verify everything is functioning correctly:

```shell
task test
```

## Run project

To start the FastAPI server and interact with the API locally:

```shell
task run
```

This command launches the FastAPI application, making it accessible via http://localhost:8000. You can explore the API routes using FastAPI's interactive API documentation at http://localhost:8000/docs.