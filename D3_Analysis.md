**Format requirements for UML analysis**

* **User**  
  * userId  
  * Name  
  * email  
* **Visitor (inherits from User)**  
  * searchHistory  
* **Administrator (inherits from User)**  
  * Role  
  * privileges  
* **Item**  
  * itemId  
  * Description  
  * dateReported  
  * status  
* **Category**  
  * categoryId  
  * name  
* **Location**  
  * locationId  
  * Name  
  * details  
* **SearchRequest**  
  * searchId  
  * Date  
  * criteria  
* **Match**  
  * matchId  
  * confidenceScore  
* **Notification**  
  * notificationId  
  * Message  
  * dateSent

**Associations with Multiplicity**

* **User – SearchRequest:**  
  * 1..1 User makes 0.. SearchRequests\*  
* **SearchRequest – Item:**  
  * 0..1 SearchRequest returns 0.. Items\*  
* **Item – Category:**  
  * 1 Item belongs to 1 Category  
* **Item – Location:**  
  * 1 Item is associated with 1 Location  
* **Administrator – Item:**  
  * 1.. Administrators manage 0..\* Items\*  
* **Match – Item:**  
  * 1 Match involves 2 Items (lost vs found)  
* **Notification – User:**  
  * 0.. Notifications sent to 1..1 User\*

**Special Relationships**

* **Inheritance:**  
  * Visitor ⟶ User  
  * Administrator ⟶ User  
* **Composition:**  
  * Location is composed within Item (an Item cannot exist without a Location).

**System Description, Requirements:**

A User can access the system to *make* a SearchRequest, which includes *searchId*, *date*, and *criteria*. This request allows users to specify parameters such as category or location. When processed, the SearchRequest can *return* one or more Item results that match the search criteria. Each Item has *itemId*, *description*, *dateReported*, and *status* attributes, representing details of lost or found belongings stored in the system.

Every Item *belongs to* exactly one Category, identified by *categoryId* and *name*, and *is associated with* one Location, which includes *locationId*, *name*, and *details*. The Location class is composed within Item, meaning that an item cannot exist independently of its recorded location. These relationships ensure that listings are both precise and contextually meaningful to users searching by category or area.

The Visitor, a subclass of User, maintains *searchHistory* to easily revisit previous search queries or results. Visitors can repeatedly *make* SearchRequests to browse or filter items by date, location, or category, addressing the user stories related to searching and filtering. The Administrator, another subclass of User, has *role* and *privileges* attributes and is responsible for *managing* Items. Administrators can verify reports, approve found-item listings, and update an item’s *status* to “recovered” when ownership is confirmed.

A Match occurs when the system identifies a potential correlation between two Item objects—typically a lost and a found report. Each Match has *matchId* and *confidenceScore*, and *involves* exactly two items. When a match or user action requires communication, a Notification is created. Each Notification includes *notificationId*, *message*, and *dateSent*, and *is sent to* a User to inform them about claim requests, successful matches, or administrative updates.

**UML Analysis of Use cases and User stories**

**Actors:**

* Visitor  
* Administrator  
* System

**Use Cases:**

* Search Items  
* Report Item  
* Manage Items  
* Match Items  
* Send Notifications

**Classes (Nouns):**

* User (Visitor, Administrator)  
* SearchRequest  
* Item  
* Category  
* Location  
* Match  
* Notification

**Key Associations:**

* User–SearchRequest  
* SearchRequest–Item  
* Item–Category  
* Item–Location   
* Match–Item  
* User–Notification

The UML analysis of use cases and user stories have eight main classes — User, Visitor, Administrator, SearchRequest, Item, Category, Location, Match, and Notification with attributes and relationships defined for each.

Visitors can submit multiple SearchRequests that return one or more Items, each belonging to a Category and tied to a Location. The Administrator manages Items and can update their status. Matches link exactly two Items, triggering Notifications sent to Users.

This structure supports use cases for searching, reporting, managing, matching, and notifying, forming the foundation for constructing the UML class and use-case diagrams.

**Use Case Diagram**
![WhatsApp Image 2025-10-13 at 01 35 19_38b8a3fc](https://github.com/user-attachments/assets/468b50ac-1fa9-4c6d-987d-31db4493fa65)

