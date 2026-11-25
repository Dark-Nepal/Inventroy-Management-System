Inventory Management System
A web-based Inventory Management System designed to help businesses manage products, categories, suppliers, purchases, sales, and stock movements from a centralized dashboard.
Dashboard
The dashboard provides a quick overview of inventory activity, including:
- Total products
- Total sales
- Low-stock products
Features
- Dashboard: Summary of inventory and sales activity.
- Categories: Organize products into categories.
- Suppliers: Maintain supplier information.
- Products: Manage product records.
- Purchases: Record incoming stock and purchases.
- Sales: Record sales transactions.
- Stock movements: Track stock changes.
- Log entries: Review system activity records.
- Product search: Quickly find products using the search bar.
Screenshots
Add your screenshots to the repository (for example, in a screenshots/ folder) and embed them here:
<!-- Example: ![Inventory Dashboard](screenshots/dashboard.png) -->Technology Stack
Update this section to match the technologies actually used in this repository.

- Python
- Django
- HTML, CSS, JavaScript
- Bootstrap (if used)
- SQLite (development database; if configured)
Getting Started
Prerequisites
Install the following:
- Python 3.10+ (use the version supported by your project)
- Git
1. Clone the repository
git clone https://github.com/Dark-Nepal/Inventroy-Management-System.git
cd Inventroy-Management-System
2. Create a virtual environment
Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
If the repository includes requirements.txt:
pip install -r requirements.txt
If no requirements file exists, install the project's dependencies according to its setup.
4. Apply database migrations
python manage.py migrate
5. Create an administrator account
python manage.py createsuperuser
6. Run the development server
python manage.py runserver
Open the app in your browser at:
http://127.0.0.1:8000/
Usage
1. Start the application and sign in with your account.
2. Add or manage product categories.
3. Register suppliers and products.
4. Record purchases and sales.
5. Review stock movements and dashboard statistics.
6. Check log entries to review recorded activity.
Project Structure
The exact directory structure may vary depending on the repository's implementation. Typical Django project files include:
project-root/
├── manage.py
├── requirements.txt
├── project_config/
├── app_name/
├── templates/
└── static/
Contributing
Contributions, suggestions, and bug reports are welcome.
1. Fork the repository.
2. Create a feature branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -m "Add your feature").
4. Push the branch (git push origin feature/your-feature).
5. Open a pull request.
License
No license has been specified yet. Add a LICENSE file before granting reuse permissions.
Author
Dark Nepal
- GitHub: Dark-Nepal
- Project repository: Inventory Management System
