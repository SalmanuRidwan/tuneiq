# TuneIQ Solution - UI Enhancement Visual Guide

## Dashboard Layout Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│  🎵 TuneIQ Solution                                              │
│  Making Nigeria's music economy visible through data-driven     │
│  analytics.                                                      │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────┬─────────────────────────────────┐
│  📊 Data Configuration      │  🔍 Filters & Analysis          │
└─────────────────────────────┴─────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Data Configuration Section - When Expanded]

  ☑️  Enable Live Data

  🎵 Platforms to Analyze:
    ☑️  Spotify      ☑️  YouTube      ☑️  Apple Music

  ───────────────────────────────────────────────────────

  🌐 Web Data Source

  [Select Artist for Web Scraping ▼]        [🔍 Scrape Web Data]
    Burna Boy (Selected)

  📋 Preview Web Data (n results) ▼
    ┌─────────────────────────────────────┐
    │ Artist | Title | Source | URL | Date │
    │   ...data table...                   │
    └─────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Dashboard KPI Cards]

┌──────────────┬──────────────┬──────────────┬──────────────┐
│   Streams    │   Revenue    │ Global Reach │ Alerts       │
│  1.2M        │  ₦45.3M      │  45 Countries│ 8 Regions    │
│ All Platforms│ +₦23.1M Ind. │ Cultural Exp.│ Investigation│
└──────────────┴──────────────┴──────────────┴──────────────┘

[Charts & Visualizations]
- Global Streaming Distribution (Choropleth Map)
- Streaming Trends (Bar Chart)
- Revenue Gap Analysis (Data Table)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 Web Research Data for [Artist Name]

┌────────────────────────────────────────────────────────────┐
│  [📰 All Sources] [🔗 By Source] [📊 Source Statistics]   │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  **Total sources found:** 15                               │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ Artist | Title | Source | URL | Date               │  │
│  ├─────────────────────────────────────────────────────┤  │
│  │ Burna Boy | Album Release | Genius Lyrics | 🔗 Link│  │
│  │ Burna Boy | New Single | AllMusic | 🔗 Link        │  │
│  │ Burna Boy | Chart #1 | Google News | 🔗 Link       │  │
│  │ ... (more results)                                  │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                             │
└────────────────────────────────────────────────────────────┘

[Tab 2: By Source]

┌──────────────────┐    ┌─────────────────────────┐
│ Total Sources: 3 │    │  Data Distribution      │
│                  │    │   by Source             │
│ Source | Count   │    │                         │
│ Genius | 7       │    │  [Pie Chart]            │
│ Google | 5       │    │  - Genius: 47%          │
│ AllMus │ 3       │    │  - Google: 33%          │
│                  │    │  - AllMusic: 20%        │
└──────────────────┘    └─────────────────────────┘

[Tab 3: Source Statistics]

┌──────────────────────────────────────────────────────┐
│ **Source Statistics**                                 │
├─────────────┬───────┬───────────────┬──────────────┤
│ Source      │ Count │ First Fetched │ Last Fetched │
├─────────────┼───────┼───────────────┼──────────────┤
│ Genius Lyr. │  7    │ 2025-11-12    │ 2025-11-12   │
│ Google News │  5    │ 2025-11-12    │ 2025-11-12   │
│ AllMusic    │  3    │ 2025-11-12    │ 2025-11-12   │
└─────────────┴───────┴───────────────┴──────────────┘

[📥 Export Web Data as CSV] → [Download CSV]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Economic Impact Analysis ▼

┌──────────────────────────────────┐
│ Metric                  │ Value  │
├─────────────────────────┼────────┤
│ Direct Streaming Rev.   │ ₦50.2M │
│ Indirect Revenue (Est.) │ ₦25.1M │
│ Cultural Export Value   │ ₦75.3M │
│ Total Economic Impact   │ ₦150.6M│
└──────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Color Scheme

**Primary Colors:**
- Neon Teal: `#068D9D` - Main accent and highlights
- Dark Accent: `#3C3744` - Secondary text and accents
- Light Background: `#F4F7F5` - Primary background

**States:**
- Success: Green (✓) with checkmark
- Warning: Yellow/Orange (⚠️) for alerts
- Error: Red (✗) for failures
- Loading: Blue (🔄) rotating spinner

## Typography

**Headers:**
- Page Title: 2.5rem, Bold (800), Gradient color
- Section Title: 1.3rem, Semi-bold (600)
- Regular Text: 1rem, Regular (400)
- Small Text: 0.875rem, Regular (400)

## Interactive Elements

### Buttons
```
Normal State:
┌─────────────────┐
│ 🔍 Scrape Data  │
└─────────────────┘

Hover State (with elevation):
┌─────────────────┐
│ 🔍 Scrape Data  │ ↑ (translate Y -2px)
└─────────────────┘
```

### Dropdown/Selectbox
```
┌──────────────────────────────┐
│ Burna Boy               ▼    │
├──────────────────────────────┤
│ Burna Boy                    │ ✓
│ Wizkid                       │
│ Davido                       │
│ Rema                         │
│ Ayra Starr                   │
│ ... (15 more artists)        │
└──────────────────────────────┘
```

## Responsive Design

### Desktop (≥1200px)
- Full sidebar (if enabled)
- 2-3 column layouts for data
- Full-size charts and visualizations

### Tablet (768px - 1199px)
- Collapsible sections
- 2-column layouts where applicable
- Adjusted chart sizes

### Mobile (<768px)
- Single column layout
- Stacked cards
- Touch-friendly buttons
- Scrollable tables

## Animations & Transitions

**Smooth Transitions:**
- Button hover: 0.12s ease
- Card elevation: 0.3s ease
- Background gradients: Smooth color shifts
- Opacity changes: 0.3s ease

**Loading States:**
- Spinner icon rotation
- Progress indicators
- Status messages
- Expandable sections

## Accessibility Features

✅ **Color Contrast** - WCAG AA compliant
✅ **Font Sizing** - Readable at all zoom levels
✅ **Touch Targets** - Minimum 44px buttons
✅ **Focus States** - Clear keyboard navigation
✅ **Alt Text** - Images have descriptions
✅ **Semantic HTML** - Proper heading hierarchy

## User Workflow Examples

### Example 1: Scrape and View Wizkid Data

```
1. Open "📊 Data Configuration"
   ↓
2. Click artist dropdown: "Wizkid" selected
   ↓
3. Click "🔍 Scrape Web Data" button
   ↓
4. See spinner: "🔄 Scraping web data for Wizkid..."
   ↓
5. Success message: "✓ Successfully scraped 12 results for Wizkid"
   ↓
6. Preview appears automatically
   ↓
7. Data displayed on dashboard in:
   - Tab 1: All 12 results
   - Tab 2: Source breakdown (Genius: 5, Google: 4, AllMusic: 3)
   - Tab 3: Statistics and export
```

### Example 2: Compare Multiple Artists

```
1. Scrape Burna Boy → View in Tab 1 (15 results)
2. Open Data Configuration
3. Select Davido from dropdown
4. Click "🔍 Scrape Web Data"
5. Dashboard updates → View Davido's 10 results
6. Switch back to previous artist data (stored in session)
7. Export both datasets as CSV
```

## Error Scenarios

### Network Error
```
✗ Web scraping failed: Connection timeout
[Retry button available]
```

### No Results Found
```
⚠️ No results found for [Artist Name]. 
   Try a different artist or check your internet connection.
```

### Invalid Selection
```
Please select a valid artist from the list.
```

## Data Format Examples

### CSV Export
```
artist,title,source,url,date_fetched
Burna Boy,Grammy Performance,Genius Lyrics,https://genius.com/...,2025-11-12T14:30:00
Burna Boy,Africa's Biggest Star,Google News,https://google.com/...,2025-11-12T14:30:01
Burna Boy,Discography,AllMusic,https://allmusic.com/...,2025-11-12T14:30:02
```

---

**Design System Version:** 2.0
**Last Updated:** November 12, 2025
**Component Status:** ✅ Production Ready
