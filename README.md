# FindIt @ NAU

A campus-wide Lost & Found web application designed for Northern Arizona University (NAU). **FindIt @ NAU** provides a centralized digital hub for reporting, searching, and recovering misplaced items on campus.  
It replaces inefficient methods like word-of-mouth and bulletin boards with a secure, searchable system that connects finders and owners quickly and reliably.

---

## Getting Started

### Prerequisites
Before running the application, ensure you have the following installed:
- **Python 3.9+**
- **SQLite**
- **Git**

---

### Installing
Follow these steps to set up the development environment:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/tg769/lost_and_found_web_app.git
   cd lost_and_found_web_app
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create Environment File**
   Create a `.env` file in the project root with the following keys:
   ```
   DATABASE_URL=sqlite:///lost_and_found.db
   SECRET_KEY=your_secret_key
   ```

4. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```
   The application will be available at [http://localhost:8000](http://localhost:8000)

5. **Example Demo**
   - Navigate to “Create Post” → Add details, upload image, and submit.  
   - Then go to “All Listings” → Search or filter by category/location.  
   - Use the contact option to reach the finder securely.

---

## Running the Tests

To ensure everything works correctly, run automated tests using:
```bash
pytest
```

### Test Coverage
- **Unit Tests:** Validate database operations, API endpoints, and form handling within Flask routes.  
- **Integration Tests:** Confirm that reporting and search workflows operate correctly end-to-end.

**Example:**  
- `tests/test_items.py` verifies that items are stored and retrieved as expected.  
- `tests/test_search.py` ensures filtering by category and location works properly.

---

## Deployment

**Status:** The app has been deployed through Render - https://lost-and-found-web-app-voh7.onrender.com/

---

## Built With

| Technology | Purpose |
|-------------|----------|
| **Python** | Backend framework |
| **SQLite** | Database and schema modeling |
| **JavaScript** | Dynamic rendering and interactivity |
| **CSS3** | Responsive design |
| **pytest** | Testing framework |
| **Render** | Deployment platform |
| **HTML5** | Structure |

---

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and pull request process.

---

## Development Workflow

1. Create a GitHub issue.  
2. Work on a feature branch.  
3. Submit a Pull Request (PR).  
4. Get review and approval before merging.

---

## Versioning

We use **Git Versioning** for this project.  
**Current Version:** `v1.0.0`

Tag this release in GitHub with:
```bash
git tag -a v1.0.0 -m "First prototype release"
git push origin v1.0.0
```

---

## Authors

- **Tanmay Ghate** – Deployment  
- **Aryan Sharma** – Documentation & Testing  
- **Munendra Choudhary** – UI Design & User Experience  
- **Myles Hill** – Documentation & Testing  
- **Rebecca Sommerville** – UI Design & Video Demonstration  
- **Keith Schmidt** – Backend & Database Integration  

See also the full list of contributors on GitHub.

---

## License

**MIT License**

Copyright (c) 2025  
Tanmay, Myles, Rebecca, Aryan, Munendra, Keith  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

