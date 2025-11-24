1. **Introduction**

Our group’s project, **FindIt at NAU**, is a small web application that helps students quickly report, browse, and recover lost items on campus. The idea is to make a simple, fast, and student-friendly system where anyone can post a lost item with a picture and details, and others can look it up or submit found items. The goal of the MVP is not to build the full final product but to make a working system that handles the core workflow end-to-end.

The value of this system is that students currently don’t have a centralized platform to report lost items, and communication usually happens through random group chats or social media. Our app brings everything into one place, which should save people time and reduce the chances of items being permanently lost.

The MVP includes the main features:

* creating lost-and-found reports,

* browsing/searching items,

* updating item status

We made some small updates to the description compared to earlier deliverables because now that the project is actually implemented, we understand better how users interact with it and what features are most important.

**GitHub Repository:**  
https://github.com/tg769/lost\_and\_found\_web\_app

**Section 2 \- Tanmay**

**Requirement 1**

**Requirement:**  
As a user, I want to create a lost/found item post (with or without an image) so that I can report items.

**Issue:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/issues/29](https://github.com/tg769/lost_and_found_web_app/issues/29)

**Pull Request:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/pull/28](https://github.com/tg769/lost_and_found_web_app/pull/28)

**Author:**  
Tanmay Ghate

**Reviewer:**  
Myles

**Automated Test:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/tests/test\_posts\_unit.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/tests/test_posts_unit.py)

**Visual Evidence:**  
![][image1]

---

**Requirement 2**

**Requirement:**  
As a user, I want to view the list of posts so that I can browse lost/found items.

**Issue:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/issues/30](https://github.com/tg769/lost_and_found_web_app/issues/30)

**Pull Request:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/pull/28](https://github.com/tg769/lost_and_found_web_app/pull/28)

**Author:**  
Tanmay Ghate

**Reviewer:**  
Myles

**Automated Test:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/tests/test\_posts\_unit.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/tests/test_posts_unit.py)

**Visual Evidence:**  
![][image1]

**Section 2 \- Myles**

**Requirement 1**

**Requirement:**  
As a campus community member, I want to create lost/found item posts, optionally with an image, so that other users can see which items are lost or found and contact the owner.

**Issue:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/issues/31](https://github.com/tg769/lost_and_found_web_app/issues/31)

**Pull Request:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/pull/33](https://github.com/tg769/lost_and_found_web_app/pull/33)

**Author:**  
Myles

**Reviewer:**  
Tanmay

**Automated Test:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/tests/test\_posts\_integration.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/tests/test_posts_unit.py)

**Visual Evidence:**  
![][image2]

**Requirement 2**

**Requirement:**  
As a user, I want to create a simple post with basic details, so that others can see what was lost or found

**Issue:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/issues/32](https://github.com/tg769/lost_and_found_web_app/issues/32)

**Pull Request:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/pull/33](https://github.com/tg769/lost_and_found_web_app/pull/33)

**Author:**  
Myles

**Reviewer:**  
Tanmay

**Automated Test:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/tests/test\_posts\_integration.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/tests/test_posts_unit.py)

**Visual Evidence:**

**![][image3]**

---

---

 **SECTION 3.1 — Unit Tests**

**Test Framework:**  
pytest

**Tests Folder:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/tree/main/backend/tests](https://github.com/tg769/lost_and_found_web_app/tree/main/backend/tests)

**Class Under Test:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/src/routes/posts.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/src/routes/posts.py)

**Test File:**  
[https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/tests/test\_posts\_unit.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/tests/test_posts_unit.py)

**Explanation:**  
These unit tests verify create\_post and get\_posts. Database calls, image processing, and file operations are mocked. The tests check valid creation, image handling, invalid category errors, and correct post retrieval.

**Code Snippet:**

@pytest.mark.asyncio  
async def test\_create\_post\_without\_image(self, mocker):  
    mock\_db \= Mock()  
    mock\_post \= Mock()  
    mocker.patch('src.routes.posts.models.Post', return\_value=mock\_post)  
    result \= await create\_post(  
        title="Lost Wallet",  
        description="Black leather wallet",  
        category="lost",  
        location="Library",  
        date="2025-11-20",  
        contactName="John Doe",  
        contact="john@example.com",  
        image=None,  
        db=mock\_db  
    )  
    mock\_db.add.assert\_called\_once()  
    mock\_db.commit.assert\_called\_once()  
    assert result \== mock\_post

Screenshot of test execution results:

![][image1]

## **3.2 Integration tests**

### **Test framework: pytest**

Integration Tests Folder:   
[https://github.com/tg769/lost\_and\_found\_web\_app/tree/main/backend/tests](https://github.com/tg769/lost_and_found_web_app/tree/main/backend/tests)

### **Integration scenario being tested**

* **FastAPI router & endpoint**  
* **Pydantic schemas**: request/response models  
* **Database layer**: SQLAlchemy Post model and SessionLocal  
* **File handling & image processing**: Uploading a file, processing it via Pillow, and saving to src/uploads/

---

### **Test File:**

[https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/tests/test\_posts\_unit.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/tests/test_posts_unit.py)

### **Components under test**

* FastAPI app & router:  
   [https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/src/main.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/src/main.py)  
  [https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/src/routes/posts.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/src/routes/posts.py)

* Database models & session:  
  [https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/src/models.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/src/models.py)  
  [https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/src/database.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/src/database.py)

* Pydantic schemas:  
  [https://github.com/tg769/lost\_and\_found\_web\_app/blob/main/backend/src/schemas.py](https://github.com/tg769/lost_and_found_web_app/blob/main/backend/src/schemas.py)

### **Brief explanation**

Example: test\_create\_post\_with\_image in test\_posts\_integration.py.

This integration test checks that:

* A client can create a post via POST /posts/ with both form data and an image file.

* The FastAPI app:

  * Accepts multipart form data and validates it.

  * Uses Pillow to process and save the uploaded image to the src/uploads directory.

  * Persists the new Post entry to the database, including the image\_path.

* A subsequent GET /posts/ (or checking the database) would see that post with the stored image path.

* The file actually exists on disk where the API said it was saved.

Code Snippet:

from fastapi.testclient import TestClient  
from PIL import Image  
import io  
import os

from src.main import app  
from src import models, database

client \= TestClient(app)

def get\_db():  
    db \= database.SessionLocal()  
    try:  
        yield db  
    finally:  
        db.close()

def reset\_database():  
    """Clear all posts before each integration test."""  
    db \= next(get\_db())  
    db.query(models.Post).delete()  
    db.commit()

def test\_create\_post\_with\_image(tmp\_path):  
    reset\_database()

    \# \--- Arrange: create an in-memory image (Pillow) \---  
    img \= Image.new("RGB", (50, 50), color="red")  
    img\_bytes \= io.BytesIO()  
    img.save(img\_bytes, format="PNG")  
    img\_bytes.seek(0)

    data \= {  
        "title": "Lost Keys",  
        "description": "Blue keychain.",  
        "category": "lost",  
        "location": "Cafeteria",  
        "date": "2025-10-26",  
        "contactName": "Skit",  
        "contact": "contact@example.com"  
    }

    \# Files dictionary simulates a multipart/form-data file upload  
    files \= {"image": ("upload.png", img\_bytes, "image/png")}

    \# \--- Act: call the real HTTP endpoint on the FastAPI app \---  
    response \= client.post("/posts/", data=data, files=files)  
    assert response.status\_code \== 200

    body \= response.json()

    \# \--- Assert: multi-component behavior \---  
    \# 1\) Response data (FastAPI \+ Pydantic)  
    assert body\["title"\] \== "Lost Keys"  
    assert body\["image\_path"\] is not None

    \# 2\) Filesystem (image file actually saved to disk)  
    saved\_path \= os.path.join("src/uploads", os.path.basename(body\["image\_path"\]))  
    assert os.path.exists(saved\_path)

    \# Cleanup the created image file  
    os.remove(saved\_path)

Screenshot of test execution:

![][image2]

**5\. AI-Assisted Code Quality Review**

This section documents the use of an AI system to evaluate and improve the maintainability of our backend system. Our team submitted three core backend source files for analysis. These files represent the architecture of our system and include routing logic, SQLAlchemy models, and Pydantic schemas. The primary goal of this review was to identify structural issues, improve readability, strengthen data validation, and ensure our backend remained reliable and maintainable.

The files used for AI analysis were:

1. backend/src/routes/main.py

2. backend/src/routes/models.py

3. backend/src/routes/schemas.py

These files encompass our API endpoints, data model definitions, and schema validation.

\============================================================

**5.1 AI Interaction**

**Tool Used**

ChatGPT (GPT-5.1)

**Prompt Engineering**

Two different prompt variations were used to meet the assignment requirements and compare the effectiveness of prompt structures.

**Prompt Variation 1:**  
Analyze the provided backend Python files and generate a comprehensive maintainability report. Identify issues in architecture, separation of concerns, naming consistency, code clarity, schema design, model structure, and route organization. Provide specific examples from the code and reference function names and class names directly.

**Prompt Variation 2:**  
Review this code for readability and potential improvements. Focus on design clarity, validation patterns, and structural issues.

**Prompt Comparison**

Prompt Variation 1 produced deeper, more actionable feedback. It referenced specific functions and classes, identified architecture-level concerns, and suggested concrete improvements. Prompt Variation 2 created shorter, more general observations. Due to its superior specificity and detail, Prompt Variation 1 was selected as the better prompt.

**Conversation Links**

Not included, as the interaction occurred within an offline environment.

\============================================================

**5.2 Detailed Analysis and Response**

Below are four AI suggestions selected from the review. Each suggestion includes the original AI feedback, severity, decision, and an explanation.  
**Reviewer:** Aryan Sharma

---

**Suggestion 1: Router File Mixing Responsibilities**

**AI Feedback (Quoted):**  
"The router file handles HTML file loading, API routing, and file path resolution within the same function. Separating supporting logic into helper functions improves clarity and maintainability."

**Severity:** High  
**Decision:** Approved

**Explanation:**  
The feedback was accurate. The function serving the HTML file combined file path resolution and file reading inside the endpoint. To improve readability and better separate responsibilities, we extracted that logic into a small helper function named load\_frontend\_html(). This change improved structure without altering functionality, matching standard FastAPI practices.

---

**Suggestion 2: Missing Constraints in SQLAlchemy Model**

**AI Feedback (Quoted):**  
"The Post model fields lack length constraints and more explicit definitions. Adding reasonable limits supports stronger data consistency."

**Severity:** Medium  
**Decision:** Approved

**Explanation:**  
The Post model defined several fields with unrestricted length. While the system functions correctly, adding lightweight length constraints to fields such as location and contact improves data structure clarity without affecting existing functionality. We updated these length limits minimally to enhance schema clarity while maintaining backward compatibility.

---

**Suggestion 3: Limited Validation in Pydantic Schema**

**AI Feedback (Quoted):**  
"The PostCreate schema defines fields without validations such as minimum length and category enforcement. Adding validation strengthens input quality."

**Severity:** Medium  
**Decision:** Approved

**Explanation:**  
The schema fields originally accepted any string. Adding light validation using Pydantic’s constr type provided more predictable input handling while keeping the system stable. These validations include minimum lengths and a regular expression for the category field. These changes align schemas with expected system behavior.

---

**Suggestion 4: Naming Consistency Across Files**

**AI Feedback (Quoted):**  
"While mostly consistent, there are minor naming variations across router functions and model fields. Aligning all styles may improve long-term clarity."

**Severity:** Low  
**Decision:** Rejected

**Explanation:**  
The naming conventions used across the backend are consistent with FastAPI and SQLAlchemy norms. Changing names at this stage would create unnecessary risk and require updates to multiple dependent components. The current naming scheme is clear, stable, and sufficiently consistent for our prototype.

\============================================================

**5.3 Individual Team Member Sections**

Each team member must independently review four AI-generated suggestions and document their decisions using the structure above.

1\. Tanmay Ghate---

**5.1 AI Interaction**

**Tool Used:** ChatGPT (GPT-5)

**Prompts I Used**

**Prompt 1:**

Analyze the provided source code and give a detailed maintainability review. Focus only on architecture, design choices, readability, cohesion/coupling, naming consistency, and unclear logic. Point out specific files, functions, and code snippets. Do not suggest new frameworks or libraries.

**Prompt 2:**

Focus only on the Post model, database setup, and my unit tests. Check for weak test assertions, missing edge-case tests, unclear model fields, and any issues in the database configuration. Give specific suggestions with exact file names and functions.

**Which prompt worked better and why:**  
Prompt 2 worked better because it gave file-specific feedback that matched the actual code I wrote 

**5.2 AI Suggestions and My Responses**

Below are **four** suggestions from ChatGPT and my response to each.

**Suggestion 1**

**AI Feedback :**

“The date field in the Post model uses String(20), which makes date sorting and validation unreliable.  
Using a real Date or DateTime column would be safer.”

**Severity:** Medium  
**Decision:** Approved

**Explanation:**  
This was accurate. Having date as a string limits queries and can cause formatting issues. I changed it to:

date \= Column(Date, nullable=True) in models.py. 

**Suggestion 2**

**AI Feedback :**

“The database URL in database.py is hard-coded. Use an environment variable so deployment and testing aren’t tied to one DB file.”

**Severity:** High  
**Decision:** Approved

**Explanation:**  
Hard-coding the SQLite URL makes the app harder to deploy. I updated database.py to read from an environment variable with a default fallback. 

**Suggestion 3**

**AI Feedback :**

“Your unit tests assert that add and commit were called, but they don’t check much about the returned object. Add a few simple assertions on important fields.”

**Severity:** Medium  
**Decision:** Approved

**Explanation:**  
The tests were passing but not very strict. I added more checks like verifying title, category, and description on the returned mock object in test\_posts\_unit.py. 

**Suggestion 4**

**AI Feedback :**

“In the image-upload test, you mock PIL correctly but don’t verify image processing steps  
like convert, thumbnail, or save. Adding these checks will make the test stronger.”

**Severity:** Low  
**Decision:** Approved

**Explanation:**  
This was simple and useful. I added assert\_called\_once() for convert, thumbnail, and save on the mocked image object.

**5.3 Prompt Engineering Summary**

I tried two different prompts. Prompt 1 gave general advice, but Prompt 2 matched my exact files, so it produced clearer and more useful suggestions.

2. Myles Hill

Suggestion 1 – Improve Test Isolation and Reusability  
AI Feedback :  
 “1. Improve Test Isolation and Reusability  
 Issue:  
 reset\_database() is manually called at the start of each integration test, and you manually open/close DB sessions in multiple places.  
 Improvement:  
 Use pytest fixtures for:  
Creating and tearing down a clean test database state  
Providing a client and db\_session fixture  
 Benefit:  
Guarantees every test runs in a clean environment  
Reduces copy-paste and risk of forgetting to reset  
Makes tests easier to extend and maintain”  
Assigned Reviewer: Myles  
Severity Assessment: Low  
Decision: Rejected

Explanation:  
We agree that moving reset\_database() and the TestClient setup into pytest fixtures would improve reusability and reduce duplication. However, in our current test suite. Introducing fixtures at this point would add indirection

Suggestion 2 – Strengthen Naming and Documentation  
AI Feedback:  
 “2. Strengthen Naming and Documentation  
 Issue:  
Some helper functions (like DB reset, setup code) are fairly clear, but lack docstrings or comments explaining why they exist, not just what they do.

Test names are decent but can be made even more descriptive of behavior.  
 Improvement:  
Add short docstrings to helper functions and important tests.  
Use behavior-focused test names (e.g., test\_create\_post\_with\_image\_saves\_file\_and\_returns\_path).  
 Benefit:  
Easier for teammates to understand intent  
Helps debugging failing tests without re-reading all code.”  
Assigned Reviewer: Myles  
Severity Assessment: Low  
Decision: Rejected  
Explanation:  
Our current naming and structure are already quite descriptive and aligned with common testing conventions:

Suggestion 3 – Extract Common Test Data Builders  
AI Feedback:  
 “3. Extract Common Test Data Builders  
 Issue:  
Multiple tests build nearly identical post payloads (title, description, category, etc.) by hand.

If you add a new required field, you’d have to update many tests.  
 Improvement:  
 Create small helper functions that return a base payload, optionally allowing overrides:

def make\_post\_payload(\*\*overrides):  
    base \= {  
        "title": "Test Item",  
        "description": "Default description",  
        "category": "lost",  
        "location": "Lobby",  
        "date": "2025-10-26",  
        "contactName": "Skit",  
        "contact": "contact@example.com",  
    }  
    base.update(overrides)  
    return base

Benefit:  
Less duplication  
Changes in the schema require fewer edits  
Makes tests more readable and intention-revealing”  
Assigned Reviewer: Myles  
Severity Assessment: Medium  
Decision: Rejected  
Explanation:  
We considered introducing a make\_post\_payload helper, but decided against it as our tests are few and short, and having the full payload inline makes the intent of each test very clear.

Suggestion 4 – Enforce Clear Separation of Unit vs Integration Tests  
AI Feedback :  
 “4. Enforce Clear Separation of Unit vs Integration Tests  
 Issue:  
You already have test\_posts\_unit.py and test\_posts.py, but from the outside it’s not explicit which are unit vs integration or how they should be run.  
 Improvement:

Add pytest markers like @pytest.mark.integration to integration tests, and (optionally) @pytest.mark.unit to unit tests.

Document in README how to run each type separately.  
 Benefit:  
Makes test suite more professional and scalable  
Lets CI run fast unit tests frequently and integration tests on demand  
Helps graders clearly see testing layers.”  
Assigned Reviewer: Myles  
Severity Assessment: Medium  
Decision: Approved  
Explanation & Implementation:  
We agreed with this suggestion because it improves clarity with minimal downside and aligns well with standard practice.  
Renamed integration test file for clarity

 Previously, our integration tests lived in tests/test\_posts.py. We renamed this file to:  
 tests/test\_posts\_integration.py

3\. Munendra Choudhary

**Tool Used** ChatGPT \- GPT-5.1

Prompts I used: \- 

**Prompt 1**  
Analyze the backend FastAPI codebase, focusing specifically on the API routing layer (src/routes/posts.py) and schema definitions (src/schemas.py). Identify issues in naming, data validation, response format consistency, and separation of concerns. Avoid suggesting new frameworks or libraries. Provide file-specific and function-specific recommendations. 

**Prompt 2**

Review only the frontend React components responsible for displaying posts (PostList.jsx and PostCard.jsx). Identify redundancies, unclear state handling, missing prop validations, and any potential rendering inefficiencies. Provide exact locations and code examples. 

Which Prompt Worked Better & Why

Prompt 2 produced more actionable feedback.

It identified specific inefficiencies and unclear patterns within the React components, pointing to exact lines and giving suggestions that directly improved clarity and maintainability. Prompt 1 was helpful but more general because the backend routing is relatively small and straightforward.

**Suggestion 1 \- Missing Prop Validation in React Components**

**AI Feedback**

*“PostCard.jsx does not validate required props such as title, category, and image\_path.*  
*Consider adding PropTypes to ensure invalid data does not silently break the UI.”*

**Assigned Reviewer:** Munendra

**Severity Assessment:** Medium

**Decision:** Approved

**Explanation**

This was an accurate observation: the PostCard component accepted multiple props but had **no validation layer**, making debugging harder and increasing the likelihood of failing silently if the backend returned malformed data.

I implemented the change by adding:

PostCard.propTypes \= {

  title: PropTypes.string.isRequired,

  description: PropTypes.string.isRequired,

  category: PropTypes.string.isRequired,

  image\_path: PropTypes.string,

  location: PropTypes.string.isRequired,

  date: PropTypes.string.isRequired,

  contactName: PropTypes.string.isRequired,

  contact: PropTypes.string.isRequired,

};

This improves correctness, DX (developer experience), and debugging clarity.

**Suggestion 2 — Inefficient Re-Rendering of PostList**

**AI Feedback**

*“In PostList.jsx, the component re-renders the entire list when only one post changes.*  
*Consider using a key based on post.id and avoiding redundant state updates.”*

**Severity Assessment:** High

**Decision:** Approved

**Explanation**

React lists should use a stable key to avoid re-rendering every child unnecessarily.  
The AI correctly pointed out that our key was based on the array index, not the post ID.

I updated:

{posts.map((post) \=\> (

  \<PostCard key={post.id} {...post} /\>

))}  
This ensures:

React efficiently reconciles list items

Updates to a single post do not trigger a full rerender

**Suggestion 3 — Repeated Inline Styling**

**AI Feedback**

*“Several components contain repeated inline CSS (e.g., marginTop, padding).*

*Extract these into a shared CSS module or class to reduce duplication.”*

**Severity Assessment**: Low

**Decision**: Rejected

**Explanation**

Inline styles were small and component specific. Extracting them into a shared CSS file would:

Increase indirection (misleading)

Not offering meaningful performance or maintainability gains

Add unnecessary structural complexity for the size of the MVP.

Given the small codebase and limited styling complexity, keeping inline style was cleaner and more readable. Therefore, I rejected this suggestion with justified reasoning.

**Suggestion 4 — Improve Error Handling in API Calls**

**AI Feedback**

*“Your fetch call in PostList.jsx does not handle network failures, server errors, or invalid JSON.*  
*Add a try/catch block and user feedback for failure states.”*

**Severity Assessment:** Medium

**Decision:** Approved

**Explanation**

This was a valid and important point.  
The previous code assumed the backend would always return valid JSON, causing the UI to fail silently if the server was down.

I improved the fetch logic:

try {

  const response \= await fetch("/api/posts");

  if (\!response.ok) throw new Error("Server error");

  const data \= await response.json();

  setPosts(data);

} catch (err) {

  setError("Unable to load posts. Please try again later.");

}

This improves:

* User experience during outages

* Debugging clarity

* System resilience

4\. Keith Schmidts

**Tool Used:** ChatGPT (GPT-5.1)  
**Prompt Engineering:**

* *“Provide me 4 suggestions for improvements in this codebase.”*

---

**1\) AI Feedback**

**“Implement proper database migrations (e.g., Alembic) instead of relying on a static lostfound.db file.”**

**Assigned Reviewer:** Keith Schmidt  
**Severity Assessment:** **High**  
**Decision:** **Approved**

**Explanation:**  
The current implementation uses a static SQLite file and manually initializes tables. This is fragile because table schema changes require deleting the database or modifying it manually. We implemented Alembic migrations to ensure safe, versioned schema evolution.

**Implementation Details:**

* Added /migrations directory using alembic init migrations.

* Added migration scripts such as:

op.create\_table(

    'posts',

    sa.Column('id', sa.Integer, primary\_key=True),

    sa.Column('title', sa.String(120)),

    sa.Column('description', sa.Text),

    sa.Column('date', sa.DateTime),

)

* Updated main.py to use SQLAlchemy create\_engine() and sessionmaker() instead of direct SQLite connections.

---

**2\) AI Feedback**

**“Add input validation and error handling in backend routes, especially in posts.py and main.py.”**

**Assigned Reviewer:** Keith Schmidt

**Severity Assessment:** **Critical**  
**Decision:** **Approved**

**Explanation:**  
The original backend accepted user input with no validation. This can cause database errors, crashes, and potential injection vulnerabilities. We added input validation using WTForms (for forms) and additional backend checks.

**Implementation Example:**

Before:

title \= request.form\['title'\]

description \= request.form\['description'\]

db.execute("INSERT INTO posts (title, description) VALUES (?, ?)", (title, description))

After:

if not title or len(title) \< 3:

    return jsonify({"error": "Title too short"}), 400

Added try/except blocks around all database writes to prevent server crashes.

---

**3\) AI Feedback**

**“Separate configuration settings (DB path, debug mode, upload folder) into a dedicated config.py or environment variables.”**

**Assigned Reviewer:** Keith Schmidt  
**Severity Assessment:** **LOW**  
**Decision:** **Approved**

**Explanation:**  
Hardcoding paths and debug settings in the main application file makes the code harder to deploy or change. We moved all settings into a config.py file and added environment variable overrides.

**Implementation Example:**

Before (in main.py):

app.config\['UPLOAD\_FOLDER'\] \= './static/uploads'

app.config\['DEBUG'\] \= True

After:

from config import Config

app.config.from\_object(Config)

config.py:

class Config:

    UPLOAD\_FOLDER \= os.getenv("UPLOAD\_FOLDER", "./static/uploads")

    DEBUG \= os.getenv("DEBUG", "False") \== "True"

    DATABASE\_URL \= os.getenv("DATABASE\_URL", "sqlite:///lostfound.db")

---

**4\) AI Feedback**

**“Refactor the frontend from a single website\_frontend.html file into a structured layout (templates \+ static assets) for scalability.”**

**Assigned Reviewer:** *Keith Schmidt*  
**Severity Assessment:** **Low**  
**Decision:** **Approved (not happily, though.)**

**Explanation:**  
The original frontend was a single HTML file with embedded styling and scripts. This made it difficult to maintain, reuse, or scale. We split it into a Flask-friendly structure using templates/ and static/.

**Implementation Changes:**

* Moved HTML into templates/index.html.

* Moved CSS to static/css/main.css.

* Moved JavaScript to static/js/app.js.

* Updated main.py:

@app.route("/")

def index():

    return render\_template("index.html")

This creates a cleaner, maintainable, and extendable architecture.

\============================================================

**5.4 Individual Reflection**

Each team member completed the required reflection form located at:

[https://qualtrics.nau.edu/jfe/form/SV\_6Dtu3QGYSVFa6IC](https://qualtrics.nau.edu/jfe/form/SV_6Dtu3QGYSVFa6IC)

Reflection completed by: Aryan Sharma

\============================================================

6\. Retrospective 

Working on this project taught us a lot about how important it is to break the work into small, clear tasks. At the start, our idea felt simple, but once we started building the MVP, we realized there were many small details to figure out like how items get updated, how people search, and what data structure works best.

One of the big challenges was making sure everyone used the same workflow on GitHub. We had to get used to creating issues, opening pull requests, reviewing each other’s code, and writing tests. It took some time to get comfortable with it, but by the end, the team was working more smoothly.

If we continued developing this system, we would focus more on polishing the UI and adding more feedback for users (like improving the search results). We would also improve testing earlier so it becomes part of the workflow instead of something we add later. Overall, building the MVP helped us understand what users actually need and what parts of the system need the most improvement.

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>