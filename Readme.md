# Exoplanet Explorer

Project generated with ChatGPT o1.

![Build Status](https://github.com/sbugalski/egzoplanet-gpt-o1/actions/workflows/ci.yml/badge.svg)
![Coverage Status](https://coveralls.io/repos/github/sbugalski/egzoplanet-gpt-o1/badge.svg?branch=main)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Exoplanet Explorer** is a comprehensive demo project designed to visualize and explore exoplanet data from the NASA Exoplanet Archive. This application showcases best practices in software development, including robust testing, continuous integration, type checking, and automated documentation.

## Table of Contents

- [Exoplanet Explorer](#exoplanet-explorer)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Advantages](#advantages)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
    - [Code Quality](#code-quality)
  - [Bugs](#bugs)

## Features

- **Interactive Data Visualization:** Utilize Streamlit to create dynamic and interactive plots of exoplanet data.
- **Data Filtering:** Easily filter exoplanets based on mass, radius, discovery year, and other criteria.
- **Caching Mechanism:** Efficiently cache data to minimize redundant network requests and enhance performance.
- **Automated Documentation:** Generate comprehensive documentation using MkDocs and mkdocstrings.
- **Robust Testing:** Implement extensive unit tests with pytest to ensure code reliability.
- **Continuous Integration:** Automate testing, coverage reporting, and documentation deployment with GitHub Actions.
- **Type Checking:** Ensure code quality and maintainability with MyPy for static type analysis.
- **Code Linting and Formatting:** Maintain consistent code style using Flake8 and Black.

## Advantages

**Exoplanet Explorer** serves as a demonstration of integrating multiple best practices in a single project. Here's how it stands out:

- **Comprehensive Testing:** Achieves high test coverage (95% for exoplanet_data.py), ensuring that critical functionalities are reliable and bug-free.
- **Continuous Integration Pipeline:** Automatically runs tests, checks code quality, builds documentation, and deploys to GitHub Pages upon every commit, streamlining the development workflow.
- **Automated Documentation:** Keeps documentation up-to-date with code changes, enhancing maintainability and onboarding for new contributors.
- **Type Safety:** Leveraging type annotations and MyPy to catch potential bugs early in the development process.
- **Code Quality Tools:** Uses Flake8 for linting and Black for automatic code formatting, ensuring a clean and readable codebase.
- **Modular Architecture:** Organized project structure promotes scalability and ease of navigation, making it suitable for both small demos and larger applications.
- **Easy Deployment:** Deploy the Streamlit app effortlessly on Streamlit Community Cloud, showcasing how to publish applications quickly and reliably.

## Getting Started

Follow these instructions to set up and run the Exoplanet Explorer on your local machine.

### Prerequisites

Ensure you have the following installed:

- **Python 3.10+**
- **Git**

### Installation

1. **Clone the repository:**

```bash
    git clone https://github.com/sbugalski/egzoplanet-gpt-o1.git
    cd egzoplanet-gpt-o1.git
```

1. **Create a Virtual Environment:**

```bash
python -m venv venv
```

```cmd
.\venv\Scripts\activate
```

1. **Install dependencies:**

```pip install --upgrade pip
pip install -r requirements.txt
```

### Usage

Run the Streamlit application to explore exoplanet data interactively.

```bash
streamlit run app.py
```

Open your browser and navigate to <http://localhost:8501> to access the application.

### Testing

Exoplanet Explorer includes unit tests to ensure code reliability.

1. Run Tests with Coverage:

```bash
coverage run -m pytest
coverage report
```

1. View Coverage Report:

```bash
coverage html
```

### Code Quality

Project supports some features ensuring code quality that is integrated into githook

```bash
mypy .
flake8
black . -v
```

## Bugs

Testing mess cache file, that contains test data instead of real.