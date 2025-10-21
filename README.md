# SnowPro Certification Quiz

A static web-based MCQ quiz application for SnowPro certification preparation.

## Features

- **Interactive MCQ Quiz**: Navigate through 1,336 SnowPro certification questions
- **Progress Tracking**: Visual progress bar showing current position
- **Answer Validation**: 
  - Green highlighting for correct answers
  - Red highlighting for incorrect answers
  - Shows correct answer when wrong option is selected
- **Flexible Navigation**: 
  - End quiz anytime
  - Check answer before proceeding
  - Sequential question flow
- **Results Summary**: 
  - Score percentage
  - Correct/Total answers
  - Accuracy statistics
- **Responsive Design**: Works on desktop and mobile devices

## How to Use

### Option 1: Local Server (Recommended)
1. **Start the server**: Run one of these commands:
   - **Python**: `python3 start_server.py` (Mac/Linux) or `python start_server.py` (Windows)
   - **Windows**: Double-click `start_server.bat`
2. **Access**: The quiz will automatically open in your browser at `http://localhost:8000/quiz.html`

### Option 2: Standalone Version (Requires Server for Full Questions)
1. **For full questions**: Run `python3 serve_quiz.py` and visit `http://localhost:8000/quiz_standalone.html`
2. **Direct file access**: Opening `quiz_standalone.html` directly will show an error message due to CORS restrictions
3. **Note**: This version now loads all 1,336 questions from the external JSON file

### Option 3: Static Hosting
1. **Upload files**: Upload both `quiz.html` and `SnowProQuestions.json` to any web hosting service
2. **Access**: Open the quiz URL in your browser

3. **Quiz Flow**:
   - Select an answer option
   - Click "Check Answer" to validate
   - View correct/incorrect highlighting
   - Click "Next Question" to proceed
   - Use "End Quiz" to finish anytime

## File Structure

```
SnowPro/
├── quiz_standalone.html   # Main quiz application (loads from external JSON)
├── SnowProQuestions.json  # Questions database (1,336 questions)
├── serve_quiz.py         # Python server script for standalone version
└── README.md             # This file
```

## Technical Details

- **Static Web Application**: No server required
- **Pure HTML/CSS/JavaScript**: No external dependencies
- **JSON Data Source**: Questions loaded from local JSON file
- **Responsive Design**: Mobile-friendly interface
- **Modern UI**: Gradient backgrounds, smooth animations, and clean typography

## Browser Compatibility

- Chrome/Edge (recommended)
- Firefox
- Safari
- Mobile browsers

## Questions Database

The quiz includes 1,336 SnowPro certification questions covering:
- Snowflake architecture
- Virtual warehouses
- Data loading and unloading
- Security and access control
- Performance optimization
- And many more topics

## Customization

You can easily customize the quiz by:
- Modifying the CSS styles in the `<style>` section
- Changing the color scheme
- Adjusting the question flow logic
- Adding new features to the JavaScript

## Hosting Options

Since this is a static web application, you can host it on:
- GitHub Pages
- Netlify
- Vercel
- Any web hosting service
- Local file system (file:// protocol)
