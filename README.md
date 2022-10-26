# Ubiwhere's Django Admin Interface

This package is a fork of [django-admin-interface](https://github.com/fabiocaccamo/django-admin-interface) for customization of Ubiwhere's Django Admin applications.

For documentation relative to the package itself, refeer to the original [repository](https://github.com/fabiocaccamo/django-admin-interface).

## Why this fork?

Original `django-admin-interface` logos are loaded in the interface and uploaded to Django **media** folder. In our case, we want themes that load logos by default. For this they must loaded from **static** folder instead.
Additionaly, we store custom pre-loaded themes for our various Django Admin applications, that can be loaded on demand by their correspondant application.

## To create a new theme

1. Add a logo (e.g. `svg`) for your theme inside `admin_interface/static/logos`. 
Example: `admin_interface/static/logos/rayt-white.svg`.
2. Go to `admin_interface/fixtures` folder, and create a new file called `<theme>.json`. **NOTE**: Replace <theme> with the name of your theme.
3. Inside the file create the following content:
```json
[
    {
        "model": "admin_interface.theme",
        "fields": { 
            "name": "PAYT",  
            "active": true,
            "title": "Smart RAYT administration",
            "title_color": "#FFFFFF",
            "title_visible": true,
            "logo": "/static/logos/rayt-white.svg",
            "logo_color": "#FFFFFF",
            "logo_visible": true,
            "css_header_background_color": "#8EC641",
            "css_header_text_color": "#FFFFFF",
            "css_header_link_color": "#FFFFFF",
            "css_header_link_hover_color": "#DEDAD1",
            "css_module_background_color": "#3F571D",
            "css_module_text_color": "#FFFFFF",
            "css_module_link_color": "#FFFFFF",
            "css_module_link_hover_color": "#DEDAD1",
            "css_module_rounded_corners": true,
            "css_generic_link_color": "#212E10",
            "css_generic_link_hover_color": "#517125",
            "css_save_button_background_color": "#0C4B33",
            "css_save_button_background_hover_color": "#0C3C26",
            "css_save_button_text_color": "#FFFFFF",
            "css_delete_button_background_color": "#BA2121",
            "css_delete_button_background_hover_color": "#A41515",
            "css_delete_button_text_color": "#FFFFFF",
            "related_modal_active": true,
            "related_modal_background_color": "#000000",
            "related_modal_background_opacity": 0.2,
            "related_modal_rounded_corners": true,
            "list_filter_dropdown": false,
            "recent_actions_visible": true
        }
    }
]
```
**DO NOT CHANGE `"model": "admin_interface.theme"`**. 

Everything inside `fields` is where you specify settings for your theme (mainly colours), and titles. In the `logo` field specify the path for the logo you created in **step 1**, excluding "admin_interface". 

4. Add this repository as app dependency instead of `django-admin-interface` from Pypi:
```txt
# Your requirements.txt
django-admin-interface @ git+https://github.com/urbanplatform/uw-admin-interface
```

5. Call the `check_theme <theme_name>` custom Django command everytime your app starts. A good place to put it is in `docker-entrypoint.sh`:
```sh
#!/bin/sh

set -eux

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations"
python manage.py migrate

# Load the theme if it does not exist
echo "Loading custom theme (if it does not exist)"
python manage.py check_theme <mytheme>

exec "$@"
```

