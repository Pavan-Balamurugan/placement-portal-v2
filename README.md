# Placement Portal Application

A full-stack campus placement management system supporting Admin, Company, 
and Student roles — built as an extension of an earlier, simpler version 
of this project.

## What's different from a typical CRUD placement portal

- **JWT-based authentication** with role claims enforced on every route (not session-based)
- **Async background jobs** via Celery + Redis — interview reminder emails, 
  monthly placement reports, and on-demand CSV exports, all handled outside 
  the request/response cycle
- **Redis caching** on read-heavy endpoints (drive listings, search) with 
  TTL expiry and explicit invalidation on data changes
- **Auto-generated PDF offer letters** the moment a candidate is marked Selected
- **Vue.js 3 frontend** (CDN-based, no build step) with role-guarded routing

## Tech Stack
Backend: Flask, SQLAlchemy, Flask-JWT-Extended, Celery, Redis, ReportLab
Frontend: Vue.js 3, Vue Router, Axios, Bootstrap 5
Database: SQLite
