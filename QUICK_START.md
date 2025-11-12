# 🚀 Quick Start Guide - TuneIQ UI Enhancements

## 5-Minute Setup

### Step 1: Run the App
```powershell
cd C:\PROJECT\tuneiq_app
streamlit run app.py
```

The dashboard opens at: `http://localhost:8501`

### Step 2: Access Web Scraping Feature
1. Click **"📊 Data Configuration"** button at top
2. Scroll down to **"🌐 Web Data Source"** section
3. See the artist dropdown (default: Burna Boy)

### Step 3: Scrape Web Data
1. **Select an artist** from dropdown (20 options available)
2. Click **"🔍 Scrape Web Data"** button
3. Wait for results (5-10 seconds)
4. See success message with result count

### Step 4: View Results
Click one of three tabs:
- **📰 All Sources** - Complete data table
- **🔗 By Source** - Breakdown + pie chart
- **📊 Source Statistics** - Stats & CSV export

### Step 5: Export (Optional)
1. Go to **"📊 Source Statistics"** tab
2. Click **"📥 Export Web Data as CSV"**
3. Download button appears
4. Click to save CSV file

## Available Artists

```
Burna Boy          Wizkid            Davido
Rema               Ayra Starr        Asake
Fireboy DML        Tems              Tiwa Savage
Olamide            Yemi Alade        CKay
Joeboy             Mr Eazi           Omah Lay
Oxlade             Simi              Ladipoe
Buju (BNXN)        Mayorkun
```

## Key Features At a Glance

| Feature | What It Does | Location |
|---------|-------------|----------|
| **Dropdown** | Select artist to scrape | Web Data Source |
| **Scrape Button** | Fetch web data | Web Data Source |
| **Tab 1** | View all results | Web Research Data |
| **Tab 2** | See source breakdown | Web Research Data |
| **Tab 3** | Export as CSV | Web Research Data |

## What Gets Scraped

The scraper fetches from **3 sources**:
1. 🎵 **Genius Lyrics** - Song & artist info
2. 📰 **Google News** - News & mentions
3. 🎸 **AllMusic** - Discography & info

**Results:** 5-15 items per scrape (typically 10-12)

## Common Tasks

### Task 1: Quick Artist Research
```
1. Click "📊 Data Configuration"
2. Select artist (e.g., "Rema")
3. Click "🔍 Scrape Web Data"
4. View Tab 1 for complete results
5. Done! ✅
```

### Task 2: Compare Two Artists
```
1. Scrape Artist A (e.g., Burna Boy)
2. View and download results
3. Select Artist B (e.g., Wizkid)
4. Scrape Artist B
5. Compare data side-by-side
```

### Task 3: Download Data for Analysis
```
1. Scrape your chosen artist
2. Go to "📊 Source Statistics" tab
3. Click "📥 Export Web Data as CSV"
4. Download opens in default folder
5. Open in Excel for analysis
```

### Task 4: View Source Breakdown
```
1. Scrape artist data
2. Click "🔗 By Source" tab
3. See source counts on left
4. See pie chart on right
5. Visual source distribution!
```

## Tips & Tricks

💡 **Tip 1:** Default artist is Burna Boy - just click scrape to see immediate results

💡 **Tip 2:** Artist selection persists - switching artists doesn't lose previous results (stored in session)

💡 **Tip 3:** Each source has different info:
   - **Genius:** Song lyrics & details
   - **Google:** Latest news & trending
   - **AllMusic:** Full discography

💡 **Tip 4:** CSV export filename includes timestamp - easy to organize multiple exports

💡 **Tip 5:** Scraping takes 5-10 seconds - be patient, loading spinner shows progress

💡 **Tip 6:** Works offline if data was scraped before - cached in session

## Troubleshooting

### ❌ "No results found"
- **Fix 1:** Check your internet connection
- **Fix 2:** Try a different artist
- **Fix 3:** Wait a few seconds and try again

### ❌ "Web scraping failed"
- **Fix 1:** Ensure internet is connected
- **Fix 2:** Check if websites are accessible
- **Fix 3:** Try again (servers may be busy)

### ❌ CSV download not working
- **Fix 1:** Check browser downloads folder
- **Fix 2:** Allow pop-ups in browser
- **Fix 3:** Try a different browser

### ❌ Data not showing
- **Fix 1:** Scroll down to see results
- **Fix 2:** Check if browser has JavaScript enabled
- **Fix 3:** Refresh page (F5)

## Feature Highlights

✨ **Smart Dropdown**
- No typing needed
- Pre-verified artist list
- Prevents invalid entries

✨ **Three Data Views**
- All results in one table
- Visual breakdown by source
- Detailed statistics

✨ **Professional Display**
- Modern design
- Smooth animations
- Easy to read

✨ **Data Export**
- Download as CSV
- Excel compatible
- Automatic filename

✨ **Responsive Design**
- Works on desktop
- Works on tablet
- Works on mobile

## System Requirements

✅ **Minimum:**
- Python 3.8+
- Streamlit installed
- Internet connection

✅ **Recommended:**
- Python 3.11+
- 4GB RAM
- Chrome/Firefox browser
- Broadband connection

## File Locations

| File | Purpose | Location |
|------|---------|----------|
| `app.py` | Main app | tuneiq_app/ |
| `nigerian_artists.py` | Artist list | tuneiq_app/ |
| `data_pipeline.py` | Scraping logic | tuneiq_app/ |
| `web_scraper.py` | Scraper module | tuneiq_app/ |

## Documentation References

Need more info? Check these files:

📖 **ENHANCEMENT_SUMMARY.md** - User-friendly overview
📖 **UI_VISUAL_GUIDE.md** - Visual mockups & design
📖 **IMPLEMENTATION_DETAILS.md** - Technical details
📖 **UI_ENHANCEMENTS.md** - Feature descriptions

## Getting Help

**Issue?** Check:
1. Troubleshooting section above
2. Documentation files
3. Browser console (F12) for errors
4. Internet connection

## Next Steps

1. ✅ Run the app (`streamlit run app.py`)
2. ✅ Try the web scraping feature
3. ✅ Export data as CSV
4. ✅ Explore different artists
5. ✅ Read documentation for details

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| F5 | Refresh page |
| F12 | Open developer console |
| Ctrl+Shift+P | Streamlit menu |
| Ctrl+L | Select dropdown |

## Contact & Feedback

**Found a bug?** Note it down and restart app
**Want a feature?** Check documentation for future roadmap
**Have feedback?** Keep using the app and enjoy!

---

## One-Liner to Get Started

```powershell
streamlit run app.py
```

Then click "📊 Data Configuration" → "🌐 Web Data Source" → Select artist → Click "🔍 Scrape Web Data"

**That's it! You're ready to explore Nigerian music data!** 🎵

---

**Version:** 2.0 (November 12, 2025)
**Status:** ✅ Production Ready
**Time to Learn:** 5 minutes
**Time to Use:** 30 seconds

Enjoy the enhanced TuneIQ experience! 🚀
