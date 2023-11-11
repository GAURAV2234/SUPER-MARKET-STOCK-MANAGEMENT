# INVENTORY-MANAGEMENT


This repository contains a Python-based stock management system designed to handle various operations related to product, user, purchase, sales, and database management. The system leverages MySQL for database operations and integrates essential modules for its functionality.

Purpose
The purpose of this system is to efficiently manage stock-related tasks, including product additions, modifications, user management, purchase orders, sales tracking, and database maintenance.

Features
1. Database Management
Database Setup: Includes operations for database creation, listing databases, and formatting/resetting the database.
Tables: Manages tables such as Product, Orders, Sales, and User, facilitating organized data storage.
2. User Management
Add User: Capability to add new users to the system.
List User: Lists existing users within the system.
Remove User: Allows for the removal of users based on specified user ID.
3. Product Management
Add Product: Adds new products to the inventory.
List Products: Displays all available products.
Search Products: Enables search functionality based on product code or category.
Update Products: Supports updating the quantity of available products.
Delete Products: Capability to delete products from the inventory.
4. Purchase Management
Add Order: Facilitates adding new purchase orders, including details such as product code, quantity, price, supplier, and category.
List Orders: Displays a comprehensive list of all orders placed.
Check Demand: Provides information on products with zero quantity in demand.
5. Sales Management
Sale Items: Allows for the sale of products, updating quantities in stock, and recording sales details.
List Sales: Displays details of all sales transactions.
How to Use
To use this system:

Ensure you have Python installed and the necessary modules listed in the code.
Set up a MySQL database with the required configurations.
Run the Python script and follow the prompts to perform various stock management operations.
Note
This system is designed to interact with a MySQL database. Ensure proper configuration and credentials before use.

