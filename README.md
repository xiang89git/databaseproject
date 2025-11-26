# Database_Final_Project
Final database project to build a backend system for a new streaming platform "Norm-Flex". 

For this README.md, it serves as a definitive plan before we can write any application code.  

#Database and Tools
* MongoDB
* PyMongo

Below is the semi-completed tables with the customer/user-facing routes tables and the admin routes tables. 

# Customer/User-Facing Routes (For the sake of space in the table, we're going to keep it short)
# 1. User Authentication & Account
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
POST    |/api/register     |JSON: { "first_name": string, "last_name": } |JSON: { "user_id": integer, "email": string }    |
Post    |/api/login        |JSON: { "email": string, "password": string }|JSON: { "user_id": integer, "token": string }    |
GET     |/api/logout       |Auth token                                   |JSON: { "message": "Logged out successfully" }   |

#2 Profile
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
POST    |/api/profiles     |JSON:{"user_id":integer,"profilename":string}|JSON: { "profile_id": int, "profile_name": str } |
GET     |/api/profiles     |Auth token                                   |JSON Array:[{"profileid":int, "profilename":str}]|
PUT     |/api/profiles/{id}|JSON: { "profile_name": string }             |JSON: { "profile_id": int, "profile_name": str } |
DELETE  |/api/profiles/{id}|Auth token                                   |JSON: { "message":"Profile deleted successfully"}|

#3 Wishlist
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
POST    |/api/p/{id}wishli |JSON: { "content_id": integer }              |JSON: { "message": "Added to wishlist"           |
GET     |/api/p/{id}wishli |Auth token                                   |JSON Array: [{"content_id": int, "title": str}]  |
DELETE  |/api/p/{id}wl{c_id}|Auth token                                  |JSON: { "message": "Removed from wishlist" }     |

#4 Viewing History
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
POST    |/api/p/{id}histor |JSON: { "content_id": integer }              |JSON: { "message": "view timestamp saved"        |
GET     |/api/p/{id}histor |Auth token                                   |JSON Array: [{"content_id": int }]               |

#5 Content Browsing
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
GET     |/api/content      |Optional query: `?type=Movie                 |TVShow&genre=Comedy`                             |
GET     |/api/cotent/{id   |Auth token                                   |JSON: { "content_id": int, "title": str,         |

# Admin Routes (For the sake of space in the tables, we're going to keep it short)
#1 Subscription Plans
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
POST    |/api/ad/subplan   |JSON: { "plan_name": string }                |JSON: { "subscription_id": integer               |
GET     |/api/ad/subplan   |None                                         |JSON Array of plans                              |
PUT     |/api/ad/subp/{id} |JSON: same as POST                           |JSON: updated plan                               |
DELETE  |/api/ad/subp/{id} |None                                         |JSON: { "message": "Subscription plan deleted" } |

#2 User Management
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
GET     |/api/admin/users  |None                                         |JSON Array of users                              |
DELETE  |/api/admin/users  |None                                         |JSON: { "message": "User deleted successfully" } |

#3 Content Management
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
POST    |/api/admin/content|JSON: { "title": str, "description": str }   |JSON: { "content_id": integer, "title": string } |
GET     |/api/admin/content|Same as POST                                 |JSON: updated content                            |
DELETE  |/api/admin/content|None                                         |JSON: { "message": "Content deleted success" }   |

#4 Genre Management
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
POST    |/api/admin/genres |JSON: { "genre_name": string }               |JSON: { "genre_id": integer, "genre_name": str } |
GET     |/api/admin/genres |None                                         |JSON Array of genres                             |
DELETE  |/api/admin/genres |None                                         |JSON: { "message": "Genre deleted successfully" }|

#5 Media File Management
Method  | Endpoint         | Parameters                                  | Return Value                                    |
--------|------------------|---------------------------------------------|-------------------------------------------------|
POST    |/api/admin/content|JSON: { "file_path": string, "lan": "string"}|JSON: "file_path": string }                      |
DELETE  |/api/admin/content|None                                         |JSON: { "message": "media deleted successfully" }|
