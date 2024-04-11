# Django Project Starter

[![License](https://img.shields.io/github/license/pyaustine/django-starter)](LICENSE)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyaustine/django-starter)
![GitHub last commit](https://img.shields.io/github/last-commit/pyaustine/django-starter)
![GitHub issues](https://img.shields.io/github/issues/pyaustine/django-starter)
![GitHub pull requests](https://img.shields.io/github/issues-pr/pyaustine/django-starter)

Python wrapper that simplifies the process of setting up a new Django project with sample app, templates, assets, and media configured. It provides a convenient way for developers to bootstrap their Django projects quickly, allowing them to focus on building their applications rather than dealing with initial setup tasks.

## Features

- Initialize a new Django project with a specified project name.
- Create a sample Django app within the project.
- Configure settings for static files (assets) and media files.
- Include sample HTML templates and static assets as a starting point for the project.

## Installation

You can install `start_django` via pip:

```bash
pip install start_django
```

## Usage

To create a new Django project, simply run the `start_django` command followed by the desired project name:

```bash
start_django <project_name>
```

This will create a new Django project with the specified name, along with a core app, templates, and static files configured.

## Configuration

The package includes sample template (`sample_template.html`), CSS (`sample_style.css`), and JavaScript (`sample_script.js`) files located in the `start_django/templates` and `start_django/static` directories. These files serve as a starting point for your project's templates and static files.

## Contributing

Contributions to `start_django` are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/pyaustine/start_django).

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.
