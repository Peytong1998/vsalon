# V Salon Studio Website

## Overview
This is a static HTML website for V Salon Studio, a hair salon located in Carpentersville, IL. The website showcases hair services including coloring, styling, extensions, and treatments. Originally imported from GitHub, it has been successfully configured to run in the Replit environment.

## Project Architecture
- **Type**: Static HTML Website
- **Structure**: Multi-page site with navigation
- **Pages**: Home (index.html), Coloring, Styling, Extensions, Treatments
- **Styling**: CSS with Google Fonts (Montserrat, Allura, Dancing Script)
- **Server**: Python HTTP server for development and deployment
- **Port**: 5000 (configured for Replit environment)

## Files Structure
```
├── index.html              # Homepage with salon info and contact
├── coloring.html           # Hair coloring services and pricing
├── styling.html            # Styling services and pricing  
├── extensions.html         # Hair extension services
├── treatments.html         # Hair treatment services
├── styles/
│   └── main.css           # Main stylesheet with responsive design
├── images/
│   └── payment-icons-real/ # Payment method icons (SVG)
├── server.py              # Python HTTP server with cache control
└── .replit                # Replit configuration

```

## Development Setup
- **Server**: Python 3.11 HTTP server
- **Host**: 0.0.0.0:5000 (configured for Replit proxy)
- **Cache Control**: Disabled for development
- **Workflow**: "Static Website Server" configured and running

## Deployment Configuration
- **Target**: Autoscale (for static websites)
- **Command**: python3 server.py
- **Port**: 5000

## Recent Changes (September 12, 2025)
- Successfully imported from GitHub
- Configured Python HTTP server with proper host binding
- Set up Replit workflow for development
- Configured deployment settings for production
- All pages tested and confirmed working
- Navigation between pages functional

## Features
- Responsive design for mobile and desktop
- Mobile hamburger menu
- Google Maps integration
- Payment method icons
- Schema markup for SEO
- Contact information and business hours
- Service pricing and descriptions

## User Preferences
- Static website serving
- Maintains original design and structure
- SEO optimized with proper meta tags