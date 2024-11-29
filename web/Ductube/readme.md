# Smart Content Filter Extension

A powerful Chrome extension that helps users filter unwanted content across various websites using customizable rules and automated filtering. Built with modern web technologies and following Chrome Extension Manifest V3 standards.

## Features

### Content Filtering
- **Keyword-based filtering**: Hide content containing specific words or phrases
- **Website-specific rules**: Create custom filters for different platforms
- **Element filtering**: Hide specific HTML elements using CSS selectors
- **Rating-based filtering**: Filter content based on ratings (e.g., YouTube videos)
- **Dynamic updates**: Filters apply to new content as it loads
- **Visual feedback**: Clear indication when content has been filtered with option to show/hide

### Site-Specific Configuration
- Global enable/disable switch
- Per-site settings
- Custom rules for popular platforms:
  - YouTube: Filter by title, duration, or channel
  - Netflix: Hide content below specified ratings
  - LinkedIn: Filter promotional posts
  - Google Search: Exclude results from specific domains

### User Interface
- Clean, modern popup interface
- Easy rule management
- Real-time preview of filter effects
- Dark mode support
- Responsive design

## Installation

### For Users
1. Download the latest release from the Chrome Web Store (coming soon)
2. Click "Add to Chrome"
3. Configure your filtering preferences via the extension popup

### For Developers
1. Clone the repository:
```bash
git clone https://github.com/yourusername/smart-content-filter
cd smart-content-filter
```

2. Install dependencies:
```bash
npm install
```

3. Build the extension:
```bash
# For development
npm run dev

# For production
npm run build
```

4. Load in Chrome:
- Open Chrome and navigate to `chrome://extensions/`
- Enable "Developer mode"
- Click "Load unpacked"
- Select the `dist` directory

## Usage

1. Click the extension icon in your browser
2. Toggle the extension on/off using the main switch
3. Add filter rules:
   - Select rule type (keyword, website, element, rating)
   - Enter the filter value
   - Choose target website (optional)
   - Enable/disable individual rules
4. View filtered content indicators and adjust as needed

## Development

### Tech Stack
- TypeScript
- React
- Chrome Extensions API (Manifest V3)
- Webpack
- Tailwind CSS

### Project Structure
```
smart-content-filter/
├── src/
│   ├── popup/
│   │   ├── Popup.tsx
│   │   └── components/
│   ├── content/
│   │   └── contentScript.ts
│   ├── background/
│   │   └── background.ts
│   └── types/
│       └── FilterTypes.ts
├── public/
│   ├── manifest.json
│   └── icons/
├── dist/
└── package.json
```

### Building and Testing
```bash
# Development build with watch mode
npm run dev

# Production build
npm run build

# Run type checking
npm run type-check

# Run linting
npm run lint

# Run tests
npm run test
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style
- Follow the TypeScript coding guidelines
- Use functional components and hooks for React
- Write unit tests for new features
- Maintain type safety throughout the codebase

## Privacy & Security

- All filtering happens locally in the browser
- No data is collected or transmitted
- Filter rules are stored in local browser storage
- Regular security updates and dependency maintenance

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

- Report bugs via GitHub Issues
- Request features through Pull Requests
- Check documentation in the `/docs` directory
- Contact us for additional support

## Acknowledgments

- Thanks to all contributors
- Built with modern web technologies
- Inspired by the need for better content filtering solutions

## Future Development

- AI-powered content classification
- Enhanced pattern matching
- Community-shared filter lists
- Additional platform support
- Performance optimizations
- Mobile browser support

---

For more information, visit our [documentation](./docs) or contact the development team.