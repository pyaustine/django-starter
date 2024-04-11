import os
import sys
import shutil
from django.conf import settings
from django.core.management import execute_from_command_line

def create_django_project(project_name):
    """
    Function to create a Django project with the specified name
    and configure it with a core app, templates, and static files.
    """
    try:
        # Step 1: Create the Django project
        execute_from_command_line(['django-admin', 'startproject', project_name])

        # Step 2: Change directory to the newly created project
        os.chdir(project_name)

        # Step 3: Create a core app
        execute_from_command_line(['python', 'manage.py', 'startapp', 'core'])

        # Step 4: Create directories for templates and static files
        os.makedirs('templates')
        os.makedirs(os.path.join('core', 'static'))

        # Step 5: Copy sample template and static files
        copy_sample_files()

        print(f"Django project '{project_name}' created successfully!")

    except Exception as e:
        print(f"Error creating Django project: {e}")
        sys.exit(1)

def copy_sample_files():
    """
    Function to copy sample template and static files into the project directories.
    """
    try:
        # Create directories if they don't exist
        if not os.path.exists('templates'):
            os.makedirs('templates')

        if not os.path.exists('static'):
            os.makedirs('static')

        # Copy content
        with open('start_django/templates/sample_template.html', 'r') as source_file:
            template_content = source_file.read()

        with open('templates/index.html', 'w') as dest_file:
            dest_file.write(template_content)

        with open('start_django/static/css/sample_style.css', 'r') as source_file:
            style_content = source_file.read()

        with open('static/css/style.css', 'w') as dest_file:
            dest_file.write(style_content)

        with open('start_django/static/js/sample_script.js', 'r') as source_file:
            script_content = source_file.read()

        with open('static/js/script.js', 'w') as dest_file:
            dest_file.write(script_content)

        # Copy sample image file
        shutil.copy('start_django/static/img/sample_image.jpg', 'static/img/sample_image.jpg')

    except Exception as e:
        print(f"Error copying sample files: {e}")
        sys.exit(1)


def configure_templates():
    """
    Function to configure the templates directory in settings.py.
    """
    try:
        templates_dir = os.path.join(BASE_DIR, 'templates')
        settings.TEMPLATES[0]['DIRS'].append(templates_dir)
    except Exception as e:
        print(f"Error configuring templates: {e}")
        sys.exit(1)

def configure_static_files():
    """
    Function to configure the static files directory in settings.py.
    """
    try:
        static_dir = os.path.join(BASE_DIR, 'static')
        settings.STATICFILES_DIRS.append(static_dir)
    except Exception as e:
        print(f"Error configuring static files: {e}")
        sys.exit(1)

def main():
    """
    Main function to parse command-line arguments and start the Django project creation process.
    """
    try:
        if len(sys.argv) != 2:
            print("Usage: python main.py <project_name>")
            sys.exit(1)

        project_name = sys.argv[1]
        create_django_project(project_name)
    except Exception as e:
        print(f"Error in main function: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Get the base directory of the project
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Modify settings to include templates and static directories
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
        configure_templates()
        configure_static_files()
    except Exception as e:
        print(f"Error setting up Django environment: {e}")
        sys.exit(1)
    
    main()