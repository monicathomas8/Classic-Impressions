# Django E-commerce Base

A reusable Django e-commerce foundation designed to speed up future projects while keeping the codebase clean, flexible, and easy to extend. This base focuses on **core shopping functionality** without locking the project into a specific payment provider or overly complex business logic.

---

## Project Purpose

This project acts as a **starter template** for small-to-medium e-commerce websites. It provides all essential shopping features out of the box while intentionally leaving advanced integrations (such as payment gateways and email automation) optional.

The goal is to allow rapid setup for client projects or personal builds, with a clear and predictable structure that can be customised as needed.

---

## Features Included

### Catalogue
- Product and category models
- Product listing and detail views
- Admin management for products and categories

### Cart
- Session-based shopping cart
- Add, update, and remove items
- Cart totals calculated dynamically

### Checkout
- Checkout flow connected to the cart
- Order creation on successful checkout
- Order confirmation / success page

### User Accounts
- User registration (sign up)
- Login and logout functionality
- Account dashboard
- View past orders

### Orders
- Orders stored in the database
- Order line items linked to products
- Users can view their own order history
- Admin users can manage orders via Django admin

### Admin Panel
- Full CRUD access for products, categories, and orders
- Clear separation between customer and admin functionality

---

## What Is Intentionally Not Included

These features are **deliberately excluded** from the base to keep it flexible and lightweight:

- Payment gateway integration (e.g. Stripe, PayPal)
- Webhooks
- Order confirmation emails
- Discount codes / vouchers
- Stock management
- Shipping rate calculations

These can be added per-project depending on requirements.

---

## Tech Stack

- Python
- Django
- HTML / CSS
- Bootstrap (for layout and styling)
- SQLite (development database)

---

## Project Structure Overview

- `catalogue` – products and categories
- `cart` – session-based cart logic
- `checkout` – checkout flow and order handling
- `accounts` – authentication and user dashboard
- `templates` – base and app templates
- `static` – CSS and static assets

---

## Usage

This project is intended to be:

- Cloned and reused as a starting point for new e-commerce builds
- Extended with payment processing and emails when required
- Adapted for different client needs without refactoring core logic

---

## Future Enhancements

Potential additions for specific projects:

- Stripe payment integration
- Email notifications for order confirmation
- Webhook handling
- Order status updates
- Stock and inventory management
- Shipping options

---

## Notes

This base prioritises **clarity, maintainability, and reusability** over feature bloat. Each project built on top of it can scale in complexity as required without compromising the underlying structure.
