# Blog API Backend

A REST API for blog built using Django Rest Framework

## Installation

### Requirements
- Python
- Django

    Complete list available in requirements.txt file

### Quickstart
- Clone the repo.  
    ```bash
    git clone https://github.com/Dhruva-Poralla/Blog-Application.git
    ```

- Inside the backend folder, make a virtual environment and activate it 
    ```bash
    python -m venv env 
    source env/bin/activate
    ```

- Install requirements from requirements.txt
    ```
    pip install -r requirements.txt
    ```

- Makemigrations and migrate the project
    ```
    python manage.py makemigrations && python manage.py migrate
    ```

- Create a superuser
    ```
    python manage.py createsuperuser
    ```

- Runserver
    ```
    python manage.py runserver
    ```

## API
<details>
<summary> User model </summary> 

- User:
    - username: string(unique),
    - first_name: string,
    - last_name: string,
    - password: string

</details>

<details>
<summary> Post Model </summary>

- Post:
    - id: Post id(read only),
    - title: string,
    - author: user-id(read only),
    - content: string
    - published_at: datetime(read only)
    - updated_at: datetime(read only)
</details>

<details>
<summary>Comment Model </summary>

- Comment:
    - post: post id(read only),
    - author: user id(ready only),
    - content: string,
    - created_at: datetime(read only)
    - updated_at: datetime(read only)
</details>



### Endpoints

Here is the post collection 

postman collection url : https://documenter.getpostman.com/view/37117154/2sA3kUH2mA
